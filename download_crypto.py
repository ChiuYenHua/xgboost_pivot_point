import datatable as dt
import os
import gc
import glob
from time import time
import zipfile
from concurrent.futures import ThreadPoolExecutor
import requests, io
from tqdm import tqdm
from requests_future import get_future_historical_data_link

# Class of margin
class Download_crypto():
    ################################################################################################
    # Get all coin historical data
    @staticmethod
    def get_all_coin_historical_data(coins=[], start='2018-01-01', end='2024-01-01', interval='1m'):
        Download_crypto.__get_coin_historical_data(coins, start, end, interval)

    # Get coin historical data # Input can be 'str' or 'list'
    @staticmethod
    def __get_coin_historical_data(coins, start, end, interval):
        ############################## Define (folder name) + (url) ##############################
        future_folder = 'data_future'

        print('Getting all coins download links...')
        future_list_of_url_to_be_download = get_future_historical_data_link(coins, start, end, interval)

        ############################## Create folder ##############################
        print('Creating folder...')
        os.makedirs(future_folder, exist_ok=True) 

        ############################# Download file (function) ##############################
        def download_files(folder_path):
            # Download link of data
            if folder_path==future_folder:
                list_of_url_to_be_download = future_list_of_url_to_be_download

            # Download data + unzip (multithreading)
            def multithreading_download_func(url):
                r = requests.get(url)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(folder_path)

            # Multithreading
            with ThreadPoolExecutor(max_workers=60) as executor:
                executor.map(multithreading_download_func, list_of_url_to_be_download)

        # Future + Margin
        print('Download future files...')   
        download_files(future_folder)
        
        ############################## Combine csv into 1 csv ##############################
        # If future, then read without header. If margin, then just combine all file + add header when write file
        def combine_csv(folder_path):
            if folder_path==future_folder:
                list_of_files_in_csv = [folder_path + '/' + url.split("/")[-1][:-3] + 'csv' for url in future_list_of_url_to_be_download]
            # Define columns_names + file_name
            column_names = ['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_volume', 'count', 'taker_buy_volume', 'taker_buy_quote_volume', 'ignore']

            # Loop through every coins
            for every_coin in tqdm(coins):
                file_name = f'{folder_path}/{every_coin}_{folder_path[5:].upper()}_{start}@{end}@{interval}.csv'

                with open(file_name,"wb") as fout:
                    # Write csv header
                    fout.write((','.join(column_names)+'\n').encode('utf-8'))                
                    # Combine files only with 'this' coin's files
                    certain_list_of_files_in_csv = list(filter(lambda file_name: every_coin in file_name, list_of_files_in_csv))

                    for csv_file in certain_list_of_files_in_csv:
                        try:
                            with open(csv_file, "rb") as f:
                                # Future cotains header in every csv, so skip header
                                if folder_path==future_folder:
                                    next(f)
                                fout.write(f.read())
                        except: pass

        # future, margin
        print('Combine future files...')  
        combine_csv(future_folder)

        ############################## Delete file except (combined file) ##############################
        def clean_up_except_combined(folder_path):
            for clean_up in glob.glob(f'./{folder_path}/*'):  
                if not '@' in clean_up:
                    os.remove(clean_up)
        
        # future, margin
        print('Delete all files except combined files...')
        clean_up_except_combined(future_folder)

        ############################## Change data type (csv to feather) ##############################
        def csv_to_feather(folder_path):
            # Create feather
            def multithreading_change_type_func(file_name):
                # Write to feather (read as datatable -> dataframe -> feather)
                dt.fread(file_name).to_pandas().to_feather(file_name[:-3]+'feather')
                # Perform garbage collection
                gc.collect()
            
            # Multithreading
            tasks = [file for file in glob.glob(f'./{folder_path}/*') if file.endswith('csv')]
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(multithreading_change_type_func, tasks)
                            
            # Delete csv
            for clean_up in glob.glob(f'./{folder_path}/*'):
                if clean_up.endswith('csv'):
                    os.remove(clean_up)
            
        # future, margin
        print('Csv to Feather in future folder...')
        csv_to_feather(future_folder)


if __name__ == '__main__':
    coins=['BTCUSDT']
    Download_crypto.get_all_coin_historical_data(coins=coins,start='2021-01-01', end='2024-01-01', interval='5m')