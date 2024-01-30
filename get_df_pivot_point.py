from matplotlib import pyplot as plt
import numba
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def get_pivot_point(df):
    # Get price
    price = df['close'].to_numpy()

    @numba.njit
    def smooth_price(price, length=2, iterations_left=1):
        if iterations_left <= 0:
            return price

        new_price = np.zeros_like(price)
        new_price[:] = price[:]

        for p in range(length, price.shape[0]-length):
            window = price[p-length:p+length+1]
            only_up = np.mean(window[1:] >= window[:-1])

            if only_up != 0 and only_up != 1:
                new_price[p] = (new_price[p-1] + new_price[p+1]) / 2

        return smooth_price(new_price, length+1, iterations_left-1)

    def get_extrema(smoothed, price, length=2, extrema_length=3):
        maxima = []
        maxima_x = []
        minima = []
        minima_x = []
        for p in range(max(length, extrema_length), smoothed.shape[0]-max(length, extrema_length)):
            window_before = smoothed[p-length:p+1]
            window_after = smoothed[p:p+length+1]
            only_up = np.mean(window_before[1:] >= window_before[:-1])
            only_down = np.mean(window_after[1:] <= window_after[:-1])
            if only_up == 1 and only_down == 1:
                arg_max = np.argmax(price[p-extrema_length:p+1+extrema_length])
                max_i = p-extrema_length+arg_max
                maxima.append(price[max_i])
                maxima_x.append(max_i)
            if only_up == 0 and only_down == 0:
                arg_min = np.argmin(price[p-extrema_length:p+1+extrema_length])
                min_i = p-extrema_length+arg_min
                minima.append(price[min_i])
                minima_x.append(min_i)
        return minima, minima_x, maxima, maxima_x

    smoothed = smooth_price(price, 2, 30)

    # get_extrema will be discussed in a minute
    minima, minima_x, maxima, maxima_x = get_extrema(smoothed, price, 2, 10)

    # Add data to dataframe
    df['pivot_point'] = 0
    df.loc[maxima_x,'pivot_point'] = 1
    df.loc[minima_x,'pivot_point'] = 2

    return df
