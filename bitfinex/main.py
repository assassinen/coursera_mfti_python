from bitfinex.model.bot import Bot
from bitfinex.states.states import OrderStates
from bitfinex.states.states import OrderDir
from bitfinex.api.data import Ticker, Candles
import random
import time
import requests


if __name__ == "__main__":
    tiker = 'tBTCUSD'
    a = Bot(tiker=tiker, spread=50, step=100, depth=10, order_size=0.01)

    # for price in (7400, 7500, 7600, 7050):
    #     print(price)
    #     a.updating(price)
    #     print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])
    #     time.sleep(5)
    # print(a.marge)
    # last_price = Ticker()
    # while True:
    #     price = last_price.get_last_price(tiker)
    #     print(price)
    #     a.updating(price)
    #     print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])
    #     time.sleep(10)

    time_frame = '5m'
    start = '2018-08-03 22:05:00'
    end = '2018-08-03 22:20:00'
    candels = Candles()
    for candle in candels.get_candles(time_frame=time_frame, start=start, end=end):
        if 'HIGH' in candle and 'LOW' in candle:
            # print(candels.unix_time_to_time(candle['MTS'] / 1000))
            print(candle['HIGH'], candels.unix_time_to_time(candle['MTS'] / 1000))
            a.updating(candle['HIGH'])
            print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])
            # time.sleep(2)
            print(candle['LOW'], candels.unix_time_to_time(candle['MTS'] / 1000))
            a.updating(candle['LOW'])
            print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])
            # time.sleep(2)
    print(a.marge)
