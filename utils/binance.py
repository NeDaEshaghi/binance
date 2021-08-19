import requests
import json


def get_all_symbols_pair():
    request = requests.get('https://api.binance.com/api/v3/exchangeInfo')
    response = request.content
    exchange_info = json.loads(response)
    symbol_pair_list = {symbol['symbol']: {'base': symbol['baseAsset'], 'quote': symbol['quoteAsset']} for symbol in
                        exchange_info['symbols']}
    return symbol_pair_list
