import requests
from ..utils.helpers import convert_to_float
from ..utils.settings import timeout_limit


api_root = 'https://api.hitbtc.com/api/2'
pairs = {'ethusdt': 'ETHUSD'}


def order_book(pair_symbol):
    pair_arg = pairs.get(pair_symbol)
    url = api_root + '/public/orderbook/{}'.format(pair_arg)

    r = requests.get(url, timeout=timeout_limit)

    if r.status_code == 200:
        data = r.json()

        asks = [[x['price'], x['size']] for x in data['ask']]
        bids = [[x['price'], x['size']] for x in data['bid']]

        if type(asks[0][0]) != float or type(asks[0][1]):
            asks = convert_to_float(asks)
            bids = convert_to_float(bids)

        return asks, bids
    else:
        print('404 error hitbtc')
        return [], []


if __name__ == '__main__':
    asks, bids = order_book('ethusdt', 20)
    print(asks)
    print(bids)
