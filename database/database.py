from model import Trade


class Database:
    def __init__(self, new_document):
        self.trade_collection = Trade()
        self.document = new_document

    def insert_to_mongo(self):
        self.trade_collection.symbol = self.document[0]
        self.trade_collection.baseAsset = self.document[1]
        self.trade_collection.quoteAsset = self.document[2]
        self.trade_collection.quantity = self.document[3]
        self.trade_collection.save()
