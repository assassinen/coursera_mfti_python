from bitfinex.model.bot import Bot
from bitfinex.states.states import OrderStates


def get_step():
    return 100

def get_spread():
    return 50

def get_last_price():
    return 7364.4

def basket_init():
    # запрашиваем текущую цену
    last_price = get_last_price()
    spread = get_spread()
    step = get_step()
    # вычисляем цену ордера на продажу (текущая цена + шаг/2 с округлением до шага)
    # вычисляем цену ордера на покупку (цена продажи - шаг)
    short_price = last_price + spread - (last_price + spread) % spread
    long_price = short_price - spread
    nex_short_price = short_price + step
    print(short_price, long_price, nex_short_price)
    pass

def basket_change():
    pass

def get_basket_orders():
    return None


def get_would_be_orders():
    # вернуть содержание корзины
    # если корзина пуста, запустить первоночальную инициализацию корзины, иначе меняем ее
    if get_basket_orders() is None:
        basket_init()
    else:
        basket_change()

def set_orders():
    pass

def clear_orders():
    pass


def main():
    # определяем какие ордера нужно выставить
    # вернуть typle(тикер, направление, цена)
    get_would_be_orders()
    # выставить ордера
    set_orders()
    # удалить ордера
    clear_orders()


if __name__ == "__main__":
    # main()
    # basket_init()
    # a = [1,2,3]
    # print(a[-1])

    # a = Bot(tiker, spread, step, depth, order_size)
    a = Bot(tiker='', spread=50, step=100, depth=10, order_size=0.1)
    a.updating()
    ord = a.short_orders[-1].set_status(OrderStates.filled)
    for i in (a.short_orders, a.long_orders):
        print(i)
    a.updating()
    print('short filled')
    for i in (a.short_orders, a.long_orders):
        print(i)


    ord = a.short_orders[-1].set_status(OrderStates.filled)
    for i in (a.short_orders, a.long_orders):
        print(i)
    a.updating()
    print('short filled')
    for i in (a.short_orders, a.long_orders):
        print(i)

    ord = a.short_orders[-1].set_status(OrderStates.filled)
    for i in (a.short_orders, a.long_orders):
        print(i)
    a.updating()
    print('short filled')
    for i in (a.short_orders, a.long_orders):
        print(i)

    print('before long filled')
    a.long_orders[-1].set_status(OrderStates.filled)
    for i in (a.short_orders, a.long_orders):
        print(i)
    a.updating()
    print('after long filled')
    for i in (a.short_orders, a.long_orders):
        print(i)

    print('before long filled')
    a.long_orders[-1].set_status(OrderStates.filled)
    for i in (a.short_orders, a.long_orders):
        print(i)
    a.updating()
    print('after long filled')
    for i in (a.short_orders, a.long_orders):
        print(i)

    print('before long filled')
    a.long_orders[-1].set_status(OrderStates.filled)
    for i in (a.short_orders, a.long_orders):
        print(i)
    a.updating()
    print('after long filled')
    for i in (a.short_orders, a.long_orders):
        print(i)

