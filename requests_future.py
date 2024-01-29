import requests

# Get future historical data
""" Input: ex. coin='BTCUSDT', start='2019-01-01', end='2023-01-01', interval='1m'
    Output: (list of url) ['http://...zip', 'http://...zip', 'http://...zip', ...]

    # Input: 1. type(coin)==str 2. type(coin)==list
"""
def get_future_historical_data_link(coin, start, end, interval):
    cookies = {
        '__BINANCE_USER_DEVICE_ID__': '{"23a01325b9408e345170166d60778f03":{"date":1638385570737,"value":"1638385570620IhDAGBV3vuI6j3HsjXJ"}}',
        '__BNC_USER_DEVICE_ID__': '{"6fc64eb04eef62cdc2e9c5ce33422f81":{"date":1704545476702,"value":"1704545476301h5LDRNPso8nGOONCFrh"}}',
        '_ga_3WP50LGEEC': 'GS1.1.1704947691.55.0.1704947691.60.0.0',
        'bnc-uuid': 'f59ae583-231b-4116-b333-753a9418ea2c',
        'source': 'organic',
        'campaign': 'www.google.com',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%22344193503%22%2C%22first_id%22%3A%221882997992796a-057d15d7afa739c-412d2c3d-1930176-188299799281429%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4Mjk5Nzk5Mjc5NmEtMDU3ZDE1ZDdhZmE3MzljLTQxMmQyYzNkLTE5MzAxNzYtMTg4Mjk5Nzk5MjgxNDI5IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMzQ0MTkzNTAzIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%22344193503%22%7D%2C%22%24device_id%22%3A%221882997992796a-057d15d7afa739c-412d2c3d-1930176-188299799281429%22%7D',
        '_ga': 'GA1.1.406793526.1684324981',
        'userPreferredCurrency': 'USD_USD',
        'BNC_FV_KEY': '32478a1bb201a7d2817861eb1b892a6c197524e6',
        'BNC_FV_KEY_EXPIRE': '1704969291872',
        'fiat-prefer-currency': 'TWD',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Thu+Jan+11+2024+12%3A34%3A51+GMT%2B0800+(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)&version=202303.2.0&isIABGlobal=false&hosts=&consentId=456c3c3c-94b1-4394-a223-771d4dfba8c8&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1&AwaitingReconsent=false&browserGpcFlag=0&geolocation=TW%3BTPE',
        '_uetvid': '59b193c0125411edb36aab2759661fb3',
        'g_state': '{"i_l":2,"i_p":1704261116255}',
        'se_gd': 'xQVFhXgcOQTCQsIQCDBsgZZVlABlTBQUlYD5QWkdlVQUgAVNXWMU1',
        'se_gsd': 'YyEnPAF+NTYiBgEsJAw7GjIzWw5WAwMSWV1AUl1aW1VWJ1NS1',
        'BNC-Location': 'BINANCE',
        'changeBasisTimeZone': '',
        'BNC_FV_KEY_T': '101-OAswshWcEXAq%2BLfm%2FiKaN9F3EcSs6Nh%2B0i5gvgR9j%2BbKhgTKLgI%2Fv0KSveB2LMNH0LftRy75EdpLxoh57wPDTQ%3D%3D-bK8FlL73WB4VtCnpVvK8vQ%3D%3D-e0',
        'OptanonAlertBoxClosed': '2023-10-27T13:30:46.637Z',
        'se_sd': 'BsOVQVQ4NGFWAkI0CDQ0gZZAwUwpXETUVQGNfUkJlVVVAVlNWUMe1',
        'isAccountsLoggedIn': 'y',
        'futures-layout': 'pro',
        'd1og': 'web.344193503.9D2AF78B911C855CAC5826590D2601D6',
        'r2o1': 'web.344193503.B5D039CF972FAEA8D65828CE842A92D4',
        'f30l': 'web.344193503.5C4CEC103B54DB0594414892C3447532',
        'p20t': 'web.344193503.0DCEE41B38363A73EC7F11F930276061',
        'theme': 'dark',
        '_gac_UA-162512367-1': '1.1704780398.CjwKCAiA1-6sBhAoEiwArqlGPiaWQ2vdSZF84Q4zkE57bMxuAk1O1jR3Btdt3outd-ggiMbAJWxxkhoCNB4QAvD_BwE',
        'lang': 'en',
        '_gid': 'GA1.2.164980096.1704892865',
        '_gat_UA-162512367-1': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:121.0) Gecko/20100101 Firefox/121.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer': 'https://www.binance.com/en/landing/data',
        'lang': 'en',
        'x-ui-request-trace': 'c205a0ec-cf58-437c-aa7b-dd83b3f7dba0',
        'x-trace-id': 'c205a0ec-cf58-437c-aa7b-dd83b3f7dba0',
        'bnc-uuid': 'f59ae583-231b-4116-b333-753a9418ea2c',
        'content-type': 'application/json',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE3MjgsMTExNyIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE3MjgsMTA4NSIsInN5c3RlbV92ZXJzaW9uIjoiTWFjIE9TIDEwLjE1IiwiYnJhbmRfbW9kZWwiOiJ1bmtub3duIiwic3lzdGVtX2xhbmciOiJ6aC1UVyIsInRpbWV6b25lIjoiR01UKzA4OjAwIiwidGltZXpvbmVPZmZzZXQiOi00ODAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoTWFjaW50b3NoOyBJbnRlbCBNYWMgT1MgWCAxMC4xNTsgcnY6MTIxLjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvMTIxLjAiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6ImQyNzEzOTUyIiwid2ViZ2xfdmVuZG9yIjoiQXBwbGUiLCJ3ZWJnbF9yZW5kZXJlciI6IkFwcGxlIE0xIiwiYXVkaW8iOiIzNS43NDk5NjYyNjAwNDU3NyIsInBsYXRmb3JtIjoiTWFjSW50ZWwiLCJ3ZWJfdGltZXpvbmUiOiJBc2lhL1RhaXBlaSIsImRldmljZV9uYW1lIjoiRmlyZWZveCBWMTIxLjAgKE1hYyBPUykiLCJmaW5nZXJwcmludCI6IjBlY2NlMzFiMGJmMDA2ODI0ZmY0NWJiY2E2NjNlODViIiwiZGV2aWNlX2lkIjoiIiwicmVsYXRlZF9kZXZpY2VfaWRzIjoiMTcwNDU0NTQ3NjMwMWg1TERSTlBzbzhuR09PTkNGcmgifQ==',
        'clienttype': 'web',
        'fvideo-id': '32478a1bb201a7d2817861eb1b892a6c197524e6',
        'fvideo-token': 'nojh52x5KHJlQL1eVbTecVBP2s64XV5YIfzNe68Qdicgsav4O4xZmz9fHzPSwd/1oDc/cXzeUcz7qo/iRtd5ZppigrR4xkK0iatnQpM77+Y1CZRuD1zmu+Uhov2tLGCr/IFUcRym2m1m/RDRSR2qKllD/M+9QAZ7sH6LV+HaFXs1Qs8L91Iq2YLcLfiuzxc8k=01',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'Origin': 'https://www.binance.com',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }

    if isinstance(coin, str):
        json_data = {
            'bizType': 'FUTURES_UM',
            'productName': 'klines',
            'symbolRequestItems': [
                {
                    'endDay': end,
                    'granularityList': [
                        interval,
                    ],
                    'interval': 'monthly',
                    'startDay': start,
                    'symbol': coin,
                },
            ],
        }
        response = requests.post(
                    'https://www.binance.com/bapi/bigdata/v1/public/bigdata/finance/exchange/listDownloadData2',
                    cookies=cookies,
                    headers=headers,
                    json=json_data,
                ).json()['data']['downloadItemList']
        return [i['url'] for i in response]

    elif isinstance(coin, list):
        def make_symbolRequestItems(coin):
            symbolRequestItem = {
                    'endDay': end,
                    'granularityList': [
                        interval,
                    ],
                    'interval': 'monthly',
                    'startDay': start,
                    'symbol': coin,
                }

            return symbolRequestItem
        
        total_response = []

        # Max requests coin is 5, so iterate every 5 coins
        for every_5_index in range(0, len(coin), 5):
            json_data = {
                'bizType': 'FUTURES_UM',
                'productName': 'klines',
                'symbolRequestItems': [make_symbolRequestItems(i) for i in coin[every_5_index:every_5_index+5]],
            }
            response = requests.post(
                    'https://www.binance.com/bapi/bigdata/v1/public/bigdata/finance/exchange/listDownloadData2',
                    cookies=cookies,
                    headers=headers,
                    json=json_data,
                ).json()['data']['downloadItemList']
            total_response += [i['url'] for i in response]
        
        return total_response

    else:
        return None