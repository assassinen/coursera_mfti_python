from .model.order import Order
from .model.book import Book


def test_print():
    print()
    older_list = []
    book = Book()
    order = {'id': 1, 'custom_id': 'gen_1', 'account_id': 'ZZZYYXX', 'symbol': 'BTC/USD', 'side': 'buy', 'price': 20,'size': 7}
    older_list.append(Order(**order))
    book.add_order(older_list[-1])
    print(book)

    order = {'id': 2, 'custom_id': 'gen_2', 'account_id': 'ZZZYYXX', 'symbol': 'BTC/USD', 'side': 'buy', 'price': 15, 'size': 7}
    older_list.append(Order(**order))
    book.add_order(older_list[-1])
    print(book)

    order = {'id': 0, 'custom_id': 'gen_0', 'account_id': 'ZZZYYXX', 'symbol': 'BTC/USD', 'side': 'buy', 'price': 15, 'size': 10}
    older_list.append(Order(**order))
    book.add_order(older_list[-1])
    print(book)

    order = {'id': 3, 'custom_id': 'gen_3', 'account_id': 'ZZZYYXX', 'symbol': 'BTC/USD', 'side': 'sell', 'price': 35, 'size': 10}
    older_list.append(Order(**order))
    book.add_order(older_list[-1])
    print(book)

    order = {'id': 30, 'custom_id': 'gen_3', 'account_id': 'ZZZYYXX', 'symbol': 'BTC/USD', 'side': 'sell', 'price': 45, 'size': 10}
    older_list.append(Order(**order))
    book.add_order(older_list[-1])
    print(book)

    order = {'id': 4, 'custom_id': 'gen_4', 'account_id': 'ZZZYYXX', 'symbol': 'BTC/USD', 'side': 'sell', 'price': 20, 'size': 6}
    older_list.append(Order(**order))
    book.add_order(older_list[-1])

    # order = {'id': 5, 'custom_id': 'gen_5', 'account_id': 'ZZZYYXX', 'symbol': 'BTC/USD', 'side': 'buy', 'price': 25, 'size': 10}
    # older_list.append(Order(**order))
    # book.add_order(older_list[-1])
    # print(book)

    del_order = older_list.pop(1)
    print(book)
    # print(del_order)
    # book.del_order(del_order)
    # print(book)
    # print(book.best_buy_price(), book.best_sell_price())


if __name__ == "__main__":
    test_print()
