from bitfinex.model.bot import Bot
from bitfinex.api.data import Ticker, Candles
from bitfinex.states.states import OrderDir


def find_bot_params():
    symbol = 'tBTCUSD'
    bot_list = []
    for spread in range (100, 105, 5):
        for step in range (100, 105, 10):
            bot_list.append(Bot(tiker=symbol, spread=spread, step=step, depth=10, order_size=0.005, min_price=7000))

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


def get_current_price():
    symbol = 'tBTCUSD'
    a = Bot(tiker=symbol, spread=100, step=100, depth=10, order_size=0.005, min_price=7000)
    tiker = Ticker()

    # i = tiker.get_last_price()
    for i in (7000, 6900, 6800, 6700, 6600):
        a.updating(i)
        print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])


if __name__ == "__main__":
    get_current_price()



