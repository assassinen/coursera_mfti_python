from bitfinex.model.bot import Bot
from bitfinex.api.data import Ticker, Candles
from bitfinex.states.states import OrderDir


def find_bot_params():
    symbol = 'tETHBTC'
    bot_list = []
    for spread in range (10, 25, 5):
        for step in range (1, 2, 2):
            bot_list.append(Bot(tiker=symbol, spread=spread / 10000, step=step / 10000, depth=10, order_size=0.1))

    time_frame = '15m'
    start = '2018-06-03 00:00:00'
    end = '2018-08-03 23:59:00'
    candels = Candles()
    for candle in candels.get_candles(symbol=symbol, time_frame=time_frame, start=start, end=end):
        if 'HIGH' in candle and 'LOW' in candle:
            # with open('test.txt', 'a') as f:
            for i in bot_list:
                i.updating(candle['HIGH'])
                # print(candle['HIGH'], candels.unix_time_to_time(candle['MTS'] / 1000))
                # print(i.orders[OrderDir.sell], i.orders[OrderDir.buy])
                # f.write('{}, {}, {}'.format(candle['HIGH'], candels.unix_time_to_time(candle['MTS'] / 1000), '\n'))
                # f.write('{}, {}, {}'.format(i.orders[OrderDir.sell], i.orders[OrderDir.buy], '\n'))
                i.updating(candle['LOW'])
                # print(candle['LOW'], candels.unix_time_to_time(candle['MTS'] / 1000))
                # print(i.orders[OrderDir.sell], i.orders[OrderDir.buy])
                # f.write('{}, {}, {}'.format(candle['LOW'], candels.unix_time_to_time(candle['MTS'] / 1000), '\n'))
                # f.write('{}, {}, {}'.format(i.orders[OrderDir.sell], i.orders[OrderDir.buy], '\n'))

    # bot_list = [i for i in bot_list if i.max_depth < 25]

    for bot in sorted(bot_list, key=lambda x: x.margin, reverse=True):
        print(bot, int(bot.margin * 437))


def get_current_price():
    symbol = 'tBTCUSD'
    a = Bot(tiker=symbol, spread=100, step=100, depth=10, order_size=0.005, min_price=7000)
    tiker = Ticker()

    # i = tiker.get_last_price()
    for i in (7000, 6900, 6800, 6700, 6600):
        a.updating(i)
        print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])


if __name__ == "__main__":
    find_bot_params()



