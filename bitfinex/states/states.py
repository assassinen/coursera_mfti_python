class OrderStates:
    create = "NEW"
    active = "ACTIVE"
    filled = "EXECUTED"
    part_filled = "PARTIALLY FILLED"
    cancelled = "CANCELED"
    rejected = "rejected"


class OrderDir:
    sell = 'ask'
    buy = 'bid'

    #Positive for buy, Negative for sell