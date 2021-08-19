from mongoengine import *


class Trade(Document):
    symbol = StringField(max_length=200, required=True)
    baseAsset = StringField(max_length=200, required=True)
    quoteAsset = StringField(max_length=200, required=True)
    quantity = FloatField(required=True)
