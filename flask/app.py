from flask import Flask
import sys
sys.path.append('../')
from database.model import Trade
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def query_to_dataset():
    trades = list(Trade.objects.aggregate([
        {'$group': {'_id': '$symbol', 'total': {'$sum': '$quantity'}}}
    ]))
    sort_trades = sorted(trades, key=lambda x: -x['total'])[:10]
    return jsonify(sort_trades)


app.run()
