class Order:

    def __init__(self, id, custom_id, account_id, symbol, side, price, size):
        self.id = id
        self.custom_id = custom_id
        self.account_id = account_id
        self.symbol = symbol
        self.side = side
        self.price = price
        self.size = size
        self.status = 'Pending'

    def __repr__(self):
        return f'({self.custom_id}, {self.symbol}, {self.price}, {self.size}, {self.status})'

