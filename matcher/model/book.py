from sys import maxsize


class Book:

    def __init__(self):
        self.book = {'buy': {}, 'sell': {}}

    def event_message(self, order):
        print(f'{order}')


    def add_order(self, order):
        self.event_message(order)
        if not self.is_deal(order):
            side = order.side
            price = order.price
            order.status = 'Placed'
            if price in self.book[side]:
                self.book[side][price].append(order)
            else:
                self.book[side][price] = [order]
            self.event_message(order)
        else:
            self.deal_processing(order)

    def del_order(self, order, status='Canceled'):
        side = order.side
        price = order.price
        order.status = status
        if price in self.book[side]:
            self.book[side][price].pop(self.book[side][price].index(order))
            if not len(self.book[side][price]):
                del self.book[side][price]
        # записать удаление ордера из базы, пока просто принт
        self.event_message(order)

    def is_deal(self, order):
        side = order.side
        price = order.price
        if side == 'sell' and price <= self.best_buy_price() \
                or side == 'buy' and price >= self.best_sell_price():
            return True

    def deal_processing(self, deal_order):
        side = 'buy' if deal_order.side == 'sell' else 'sell'
        order = self.book[side][self.best_price(side)][0]

        deal_order_size = deal_order.size
        order_size = order.size
        if deal_order_size > order_size:
            self.del_order(order, 'Filled')
            deal_order.change_order_size(deal_order_size - order_size)
            #отправляем информацию о сделки
        else:
            self.del_order(deal_order, 'Filled')
            deal_order.change_order_size(0)
            if order_size - deal_order_size == 0:
                self.del_order(order, 'Filled')
            else:
                order.change_order_size(order_size - deal_order_size)
            #отправляем информацию о сделки
        if deal_order.size > 0:
            self.add_order(deal_order)

    def best_price(self, side):
        return self.best_sell_price() if side == 'sell' else self.best_buy_price()

    def best_sell_price(self):
        price_list = list(self.book['sell'].keys())
        return maxsize if not len(price_list) else min(price_list)

    def best_buy_price(self):
        price_list = list(self.book['buy'].keys())
        return 0 if not len(price_list) else max(price_list)

    def __repr__(self):
        empty_message = '         '
        sell = sorted(list(self.book['sell'].keys()), reverse=True)
        buy = sorted(list(self.book['buy'].keys()), reverse=True)
        mess = '''-----------------------\n покупка  цена  продажа\n'''
        for s in sell:
            c = sum([i.size for i in self.book['sell'][s]])
            str_s = str(s)
            while len(str_s) < 5:
                str_s = ' ' + str_s + ' '
            mess += f'{empty_message}{str_s} {c}\n'
        for s in buy:
            c = str(sum([i.size for i in self.book['buy'][s]]))
            while len(c) < 8:
                c = ' ' + c
            str_s = str(s)
            while len(str_s) < 7:
                str_s = ' ' + str_s + ' '
            mess += f'{c}{str_s}{empty_message}\n'


        return f'{mess}'

