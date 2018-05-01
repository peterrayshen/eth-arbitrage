from ..utils.config import global_pair_list
from ..utils.config import order_books_funcs


class Exchange:

    def __init__(self, name):
        self.name = name
        if self.name not in order_books_funcs.keys() or self.name not in global_pair_list.keys():
            print('exchange name not found, exiting')
            raise ValueError
        self.order_book_call = order_books_funcs[name]
        self.pair_list = global_pair_list[name]
        self.order_book = {}

    def highest_bid(self, pair):
        # return price and volume of lowest ask of certain pair
        return self.order_book[pair]['bids'][0][0], self.order_book[pair]['bids'][0][1]

    def lowest_ask(self, pair):
        # return price and volume of lowest ask of certain pair
        return self.order_book[pair]['asks'][0][0], self.order_book[pair]['asks'][0][1]

    def update_book(self, pair):
        #print('updating order book for ', self.name)
        asks, bids = self.order_book_call(pair)
        asks.sort(reverse=False, key=lambda x: x[0])
        bids.sort(reverse=True, key=lambda x: x[0])
        self.order_book[pair] = {'asks': asks, 'bids': bids}
        #print('DONE for ', self.name)


