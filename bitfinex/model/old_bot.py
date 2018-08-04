from bitfinex.api.data import get_last_price, put_order
from bitfinex.model.order import Order
from bitfinex.states.states import OrderStates
from bitfinex.states.states import OrderDir

class Bot:

    def __init__(self, tiker, spread, step, depth, order_size):
        self.tiker = tiker
        self.spread = spread
        self.step = step
        self.depth = depth
        self.order_size = order_size

        self.order = {}
        self.order[OrderDir.sell] = []
        self.order[OrderDir.buy] = []


        self.long_orders = [None]
        self.short_orders = [None]


    def get_last_orders(self):
        self.last_long = self.long_orders[-1]
        self.last_short = self.short_orders[-1]


    def calculate_price(self):
        last_price = get_last_price()
        return last_price + self.spread - (last_price + self.spread) % self.spread - self.step


    def get_short_price(self, dir):
        if self.last_short is None:
            last_price = get_last_price()
            price = last_price + self.spread - (last_price + self.spread) % self.spread - self.step
        else:
            price = self.last_short.price

        if dir == OrderDir.sell:
            return price + self.step
        else:
            return price - self.spread


    def set_order(self, dir):
        price = self.get_short_price(dir)
        order = {'1':'2'}
        if not put_order(**order):
            return False
        if dir == OrderDir.sell:
            self.short_orders.append(Order(price, self.order_size, dir))
        else:
            self.long_orders.append(Order(price, self.order_size, dir))


    def del_order(self, dir):
        if dir == OrderDir.sell:
            self.short_orders.pop()
        else:
            self.long_orders.pop()


    def updating(self):
        self.get_last_orders()
        if self.last_short is None:
            # ставим первый ордер (он шорт)
            self.set_order(OrderDir.sell)
        elif self.last_short.status == OrderStates.filled:
            # ставим новый ласт ордер
            # ставим новый шорт ордер
            self.set_order(OrderDir.sell)
            self.set_order(OrderDir.buy)
        elif self.last_long is not None and self.last_long.status == OrderStates.filled:
            # удаляем два ордера в продажу и сведенный в покупку
            self.del_order(OrderDir.sell)
            self.del_order(OrderDir.sell)
            self.del_order(OrderDir.buy)
            # обновляем состояние и выставляем новый ордер на прожажу
            self.get_last_orders()
            self.set_order(OrderDir.sell)


