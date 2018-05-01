from ..exchange_wrappers import binance
from ..exchange_wrappers import huobi
from ..exchange_wrappers import okex
from ..exchange_wrappers import bittrex
from ..exchange_wrappers import hitbtc
from ..exchange_wrappers import poloniex
from ..exchange_wrappers import bitfinex
from ..exchange_wrappers import gdax
from ..exchange_wrappers import kraken
from ..exchange_wrappers import zb
from ..exchange_wrappers import bitstamp

global_pair_list = {'binance': ['ethusdt'],
                     'huobi': ['ethusdt'],
                     'okex': ['ethusdt'],
                     'bittrex': ['ethusdt'],
                     'hitbtc': ['ethusdt'],
                     'poloniex': ['ethusdt'],
                    'bitfinex': ['ethusd'],
                    'gdax': ['ethusd'],
                    'kraken': ['ethusd'],
                    'zb': ['ethusdt'],
                    'bitstamp': ['ethusd'],
                    }

supported_exchanges_by_pair = {'ethusdt': ['binance',
                                            'huobi',
                                            'okex',
                                            'bittrex',
                                            'hitbtc',
                                            'poloniex',
                                           'zb',],

                               'ethusd': ['bitfinex', 'gdax', 'kraken', 'bitstamp']}


order_books_funcs = {'binance': binance.order_book, 'huobi': huobi.order_book, 'okex': okex.order_book,
               'bittrex': bittrex.order_book, 'hitbtc': hitbtc.order_book, 'poloniex': poloniex.order_book,
                     'bitfinex': bitfinex.order_book, 'gdax': gdax.order_book, 'kraken': kraken.order_book,
                     'zb': zb.order_book, 'bitstamp': bitstamp.order_book}

exchange_list = ['huobi', 'okex', 'binance', 'hitbtc', 'bittrex', 'poloniex', 'bitfinex', 'gdax', 'kraken',
                 'zb', 'bitstamp']




