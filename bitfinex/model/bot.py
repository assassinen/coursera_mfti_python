from bitfinex.api.data import Ticker, put_order
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
        self.price = Ticker()
        self.marge = 0

        self.orders = {}
        self.orders[OrderDir.sell] = []
        self.orders[OrderDir.buy] = []


    def get_price(self, dir):
        last_order = self.get_last_order(OrderDir.sell)
        if last_order is None:
            price = self.last_price + self.spread - (self.last_price + self.spread) % self.spread - self.step
        else:
            price = last_order.price
        return price + self.step if dir == OrderDir.sell else price - self.step - self.spread


    def add_order(self, dir):
        price = self.get_price(dir)
        order = {'1':'2'}
        if not put_order(**order):
            return False
        self.orders[dir].append(Order(price, self.order_size, dir))


    def del_order(self, dir):
        # проверку на удаления у контрагента
        self.orders[dir].pop()


    def get_last_order(self, dir):
        return self.orders[dir][-1] if self.orders[dir] else None


    def update_orders_status(self, price, orders):
        for order in orders:
            if price > order.price: # добавить проверку статуса у контрагента
                order.status = OrderStates.filled


    def margin_calculate(self):
        last_sell_order = self.get_last_order(OrderDir.sell)
        last_buy_order = self.get_last_order(OrderDir.buy)
        self.marge = self.marge + \
                     last_sell_order.price * self.order_size - \
                     last_buy_order.price * self.order_size - \
                     last_sell_order.price * self.order_size * 0.001 - \
                     last_buy_order.price * self.order_size * 0.001


    def correction_orders(self):
        filled_buy_orders = len([order for order in self.orders[OrderDir.buy] if order.status == OrderStates.filled])
        for order in range(filled_buy_orders):
            self.del_order(OrderDir.sell)
            self.margin_calculate()
            self.del_order(OrderDir.sell)
            self.del_order(OrderDir.buy)
            # self.margin_calculate()
            # обновляем состояние и выставляем новый ордер на прожажу
            self.add_order(OrderDir.sell)


    def check_orders_status(self):
        for dir in (OrderDir.sell, OrderDir.buy):
            if dir == OrderDir.sell:
                for order in (order for order in self.orders[OrderDir.sell]):
                    if self.last_price >= order.price:  # добавить проверку статуса у контрагента
                        order.status = OrderStates.filled
            else:
                for order in (order for order in self.orders[OrderDir.buy]):
                    if self.last_price <= order.price:  # добавить проверку статуса у контрагента
                        order.status = OrderStates.filled


    def replace_order(self):
        last_sell_order = self.get_last_order(OrderDir.sell)
        if self.last_price < last_sell_order.price - self.spread:
            self.del_order(OrderDir.sell)
            self.add_order(OrderDir.sell)


    def updating(self, price=None):
        try:
            self.last_price = float(self.price.get_last_price((self.tiker))) if price is None else float(price)
        except:
            return False
        self.check_orders_status()
        last_sell_order = self.get_last_order(OrderDir.sell)
        last_buy_order = self.get_last_order(OrderDir.buy)

        if last_sell_order is None:
            self.add_order(OrderDir.sell)
        elif last_sell_order.status == OrderStates.create and last_buy_order is None:
            self.replace_order()
        elif last_sell_order.status == OrderStates.filled:
            # ставим новый ласт ордер
            # ставим новый шорт ордер
            self.add_order(OrderDir.sell)
            self.add_order(OrderDir.buy)
        else:
            self.correction_orders()


        # elif last_buy_order is not None \
        #         and last_buy_order != [] \
        #         and last_buy_order.status == OrderStates.filled:
        #     # удаляем два ордера в продажу и сведенный в покупку
        #     self.del_order(OrderDir.sell)
        #     self.del_order(OrderDir.sell)
        #     self.del_order(OrderDir.buy)
        #     # обновляем состояние и выставляем новый ордер на прожажу
        #     self.add_order(OrderDir.sell)




    # for i in range(10):
    #     a.updating(random.randint(7000, 8000))
    #     print(a.orders[OrderDir.sell], a.orders[OrderDir.buy])



