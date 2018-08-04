import uuid
from bitfinex.states.states import OrderStates


class Order:

    def __init__(self, price, size, dir):
        self.id = uuid.uuid4()
        self.price = price
        self.size = size
        self.dir = dir
        self.status = OrderStates.create


    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


    def __repr__(self):
        return 'order: {}, ' \
               'price: {}, ' \
               'size: {}, ' \
               'dir: {}, ' \
               'status: {}'.format(self.id,
                                   self.price,
                                   self.size,
                                   self.dir,
                                   self.status)

    def __repr__(self):
        return 'status: {}, price: {}, dir: {} '.format(self.status, self.price, self.dir)

