from bitfinex.model.bot import Bot
from bitfinex.states.states import OrderStates
from bitfinex.states.states import OrderDir
from bitfinex.api.data import Ticker, Candles
import random
import time
import requests


if __name__ == "__main__":
    tiker = 'tBTCUSD'
    bot_list = []
    for spread in range (100, 105, 5):
        for step in range (100, 105, 10):
            bot_list.append(Bot(tiker=tiker, spread=spread, step=step, depth=10, order_size=0.005))

    time_frame = '15m'
    start = '2018-07-03 00:00:00'
    end = '2018-08-03 23:59:00'
    candels = Candles()
    for candle in candels.get_candles(symbol='tBTCUSD', time_frame=time_frame, start=start, end=end):
        if 'HIGH' in candle and 'LOW' in candle:
            # with open('test.txt', 'a') as f:
            for i in bot_list:
                i.updating(candle['HIGH'])
                # f.write('{}, {}, {}'.format(candle['HIGH'], candels.unix_time_to_time(candle['MTS'] / 1000), '\n'))
                # f.write('{}, {}, {}'.format(i.orders[OrderDir.sell], i.orders[OrderDir.buy], '\n'))
                i.updating(candle['LOW'])
                # f.write('{}, {}, {}'.format(candle['LOW'], candels.unix_time_to_time(candle['MTS'] / 1000), '\n'))
                # f.write('{}, {}, {}'.format(i.orders[OrderDir.sell], i.orders[OrderDir.buy], '\n'))

    # bot_list = [i for i in bot_list if i.max_depth < 25]

    for bot in sorted(bot_list, key=lambda x: x.margin, reverse=True):
        print(bot)




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

    # time_frame = '5m'
    # start = '2018-08-03 00:00:00'
    # end = '2018-08-03 23:59:00'
    # candels = Candles()
    # for candle in candels.get_candles(time_frame=time_frame, start=start, end=end):
    #     if 'HIGH' in candle and 'LOW' in candle:
    #         # print(candels.unix_time_to_time(candle['MTS'] / 1000))
    #         # print(candle['HIGH'], candels.unix_time_to_time(candle['MTS'] / 1000))
    #         a.updating(candle['HIGH'])
    #         # print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])
    #         # time.sleep(2)
    #         # print(candle['LOW'], candels.unix_time_to_time(candle['MTS'] / 1000))
    #         a.updating(candle['LOW'])
    #         # print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])
    #         # time.sleep(2)
    # print(a.marge)
