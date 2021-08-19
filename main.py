import json
import time

from binance_websocket.stream import Stream
from utils.binance import get_all_symbols_pair
from database.model import Trade


def stream_to_mongo(stream):
    msg = stream.receive()
    msg_dict = json.loads(msg)
    if msg_dict.get('e') == 'trade':
        symbol = msg_dict.get('s')
        quantity = msg_dict.get('q')
        baseAsset = symbol_pairs[symbol]['base']
        quoteAsset = symbol_pairs[symbol]['quote']

        Trade(symbol=baseAsset, quantity=quantity, baseAsset=baseAsset, quoteAsset=quoteAsset).save()
        Trade(symbol=quoteAsset, quantity=quantity, baseAsset=baseAsset,
              quoteAsset=quoteAsset).save()
        print(symbol)
    else:
        print(msg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        try:
            symbol_pairs = get_all_symbols_pair()
            pairs_list = list(symbol_pairs.keys())
            stream1 = Stream()
            stream2 = Stream()

            with stream1, stream2:

                stream1.subscribe(symbols=pairs_list[:1024], stream_name='trade')
                stream2.subscribe(symbols=pairs_list[1024:], stream_name='trade')
                stream1.list_subscriptions()
                stream2.list_subscriptions()

                while True:
                    stream_to_mongo(stream1)
                    stream_to_mongo(stream2)
        except Exception as e:
            print(e)
