import requests
from ..utils.helpers import convert_to_float
from ..utils.settings import timeout_limit

api_root = 'http://api.zb.com'
pairs = {'ethusdt': 'eth_usdt'}


def order_book(pair_symbol):
    pair_arg = pairs.get(pair_symbol)
    url = api_root + '/data/v1/depth?market={}'.format(pair_arg)

    r = requests.get(url, timeout=timeout_limit)

    if r.status_code == 200:
        data = r.json()

        asks = [[x[0], x[1]] for x in data['asks']]
        bids = [[x[0], x[1]] for x in data['bids']]

        if type(asks[0][0]) != float or type(asks[0][1]):
            asks = convert_to_float(asks)
            bids = convert_to_float(bids)

        return asks, bids
    else:
        print('404 error zb')
        return [], []


if __name__ == '__main__':
    asks, bids = order_book('ethusdt')
    print(asks)
    print(bids)
