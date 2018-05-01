from django.http import JsonResponse
import threading
from queue import Queue
from .utils.config import exchange_list
from .utils.exchange import Exchange
from .utils.config import supported_exchanges_by_pair
import datetime as dt


def index(request):
    json_data = get_data()
    return JsonResponse(json_data)


def get_data():

    def threader():
        while True:
            worker_info = update_queue.get()
            if worker_info is None:
                break
            exchange = worker_info[0]
            pair = worker_info[1]
            print('updating book for ', exchange.name)
            exchange.update_book(pair)
            print('done book for ', exchange.name)
            update_queue.task_done()

    exchange_objects = {}

    for exchange_name in exchange_list:
        exchange_objects[exchange_name] = Exchange(exchange_name)

    update_queue = Queue()

    threads = []
    for x in range(10):
        t = threading.Thread(target=threader)
        t.start()
        threads.append(t)

    #pair_name = 'ethusd'
    pair_names = ['ethusd', 'ethusdt']

    for pair_symbol in pair_names:
        for exchange_name in supported_exchanges_by_pair[pair_symbol]:
            update_queue.put([exchange_objects[exchange_name], pair_symbol])

    update_queue.join()

    for i in range(10):
        update_queue.put(None)
    for t in threads:
        t.join()

    data = []

    for pair_symbol in pair_names:
        for exchange_name in supported_exchanges_by_pair[pair_symbol]:
            lowest_ask = exchange_objects[exchange_name].lowest_ask(pair_symbol)[0]
            highest_bid = exchange_objects[exchange_name].highest_bid(pair_symbol)[0]
            lowest_ask = round(lowest_ask, 2)
            highest_bid = round(highest_bid, 2)
            exchange_data = [exchange_name, highest_bid, lowest_ask]
            data.append(exchange_data)

    exchanges = []

    for pair_symbol in pair_names:
        for exchange_name in supported_exchanges_by_pair[pair_symbol]:
            exchanges.append(exchange_name)

    return {'exchanges': exchanges, 'data': data, 'time': dt.datetime.utcnow().time()}


