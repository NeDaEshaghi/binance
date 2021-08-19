import time

from websocket import create_connection
import json
import requests


class Stream:
    BASE_URL = 'wss://stream.binance.com:9443/ws'

    def __init__(self):
        self.ws = None

    def connect(self):
        print(f'Connecting to {self.BASE_URL}')
        self.ws = create_connection(self.BASE_URL)

    def subscribe(self, symbols, stream_name):
        step = 128
        timout = 0.5
        while symbols:
            subscription_list = symbols
            if len(symbols) > step:
                subscription_list = symbols[:step]
            request = {
                "method": "SUBSCRIBE",
                "params": [(symbol.lower() + '@' + stream_name) for symbol in subscription_list],
                "id": 1
            }
            json_request = json.dumps(request)
            self.ws.send(json_request)
            symbols = symbols[len(subscription_list):]
            time.sleep(timout)

    def list_subscriptions(self):
        request = {
            "method": "LIST_SUBSCRIPTIONS",
            "id": 3
        }
        json_request = json.dumps(request)
        self.ws.send(json_request)

    def receive(self):
        results = self.ws.recv()
        return results

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ws.close()

    def __enter__(self):
        self.connect()
