def convert_to_float(order_book):
    new_order_book = [[float(value) for value in order] for order in order_book]
    return new_order_book


