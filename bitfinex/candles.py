# import requests
# import time
#
# url = 'https://api.bitfinex.com/v2/candles/trade:1m:tBTCUSD/last'
# while True:
#     response = requests.get(url)
#     print(response.json())
#     time.sleep(10)


import requests as requests
import time

url = 'https://api.bitfinex.com/v2/tickers?symbols={}'

key = [
    'SYMBOL',
    'BID',
    'BID_SIZE',
    'ASK',
    'ASK_SIZE',
    'DAILY_CHANGE',
    'DAILY_CHANGE_PERC',
    'LAST_PRICE',
    'VOLUME',
    'HIGH',
    'LOW'
]

def get_tikers(symbols=('tBTCUSD','tETHUSD',)):
    result = []
    try:
        response = requests.get(url.format(','.join(symbols)))
        if response.status_code == 200:
            result = [dict(zip(key, item)) for item in response.json()]
    except:
        return result
    print(result, id(result))
    return result


def get_last_price(symbols=('tBTCUSD','tETHUSD',)):
    key_list = ('SYMBOL', 'LAST_PRICE')
    result = ({key:item for key, item in tiker.items() if key in key_list} for tiker in get_tikers(symbols))
    return result


while True:
    for coin_params in get_last_price():
        print("{}: {}".format(coin_params['SYMBOL'][1:], coin_params['LAST_PRICE']))
    time.sleep(1)


# url = 'https://api.kraken.com/0/public/Ticker/c'
# response = requests.get(url)
# if response.status_code == 200:
#     print(response.json())