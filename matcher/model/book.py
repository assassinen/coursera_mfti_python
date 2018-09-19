class Book:

    def __init__(self):
        self.book = {'buy': {}, 'sell': {}}

    def add_order(self, order):
        if not self.is_deal(order):
            side = order.side
            price = order.price
            order.status = 'Placed'
            if price in self.book[side]:
                self.book[side][price].append(order)
            else:
                self.book[side][price] = [order]
        #записать добавление ордера в базу, пока просто принт
        print(f'add {order}')

    def del_order(self, order):
        side = order.side
        price = order.price
        order.status = 'Canceled'
        self.book[side][price].pop(self.book[side][price].index(order))
        # записать удаление ордера из базы, пока просто принт
        print(f'cancel {order}')

    def is_deal(self, order):
        True

    def __repr__(self):
        return f'{self.book}'


