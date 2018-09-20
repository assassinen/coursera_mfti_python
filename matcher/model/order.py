class Order:

    def __init__(self, id, custom_id, account_id, symbol, side, price, size):
        self.id = id
        self.custom_id = custom_id
        self.account_id = account_id
        self.symbol = symbol
        self.side = side
        self.price = price
        self.size = size
        self.status = 'Arrived'

    def change_order_size(self, size):
        self.size = size

    def __repr__(self):
        return f'({self.custom_id}, {self.status}, {self.symbol}, {self.side}, {self.price}, {self.size})'

