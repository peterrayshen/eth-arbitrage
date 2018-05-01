import requests
from ..utils.helpers import convert_to_float
from ..utils.settings import timeout_limit


api_root = 'https://www.okex.com/api/v1'
pairs = {'ethusdt': 'eth_usdt'}


def order_book(pair_symbol):
    pair_arg = pairs.get(pair_symbol)
    url = api_root + '/depth.do?symbol={}&size=100'.format(pair_arg)

    r = requests.get(url, timeout=timeout_limit)

    if r.status_code == 200:
        data = r.json()
        asks = data['asks']
        bids = data['bids']

        if type(asks[0][0]) != float or type(asks[0][1]):
            asks = convert_to_float(asks)
            bids = convert_to_float(bids)

        return asks, bids
    else:
        print('404 error okex')
        return [], []


if __name__ == '__main__':
    asks, bids = order_book('ethusdt')
    print(asks)
    print(bids)
