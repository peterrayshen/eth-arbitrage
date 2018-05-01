import requests
from ..utils.helpers import convert_to_float
from ..utils.settings import timeout_limit

api_root = 'https://bittrex.com/api/v1.1'
pairs = {'ethusdt': 'USDT-ETH'}


def order_book(pair_symbol):
    pair_arg = pairs.get(pair_symbol)
    url = api_root + '/public/getorderbook?market={}&type=both'.format(pair_arg)

    r = requests.get(url, timeout=timeout_limit)

    if r.status_code == 200:
        data = r.json()['result']

        asks = [[x['Rate'], x['Quantity']] for x in data['sell']]
        bids = [[x['Rate'], x['Quantity']] for x in data['buy']]

        if type(asks[0][0]) != float or type(asks[0][1]):
            asks = convert_to_float(asks)
            bids = convert_to_float(bids)

        return asks, bids
    else:
        print('404 error bittrex')
        return [], []


if __name__ == '__main__':
    asks, bids = order_book('ethusdt')
    print(asks)
    print(bids)
