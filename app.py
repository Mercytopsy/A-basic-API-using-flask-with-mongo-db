import os
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
app = Flask(__name__)
stores= [
    {
        'name': 'My Wonderful Stores',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]
app.config['MONGO_URI'] = os.environ.get('DB')
mongo = PyMongo(app)
@app.route('/store', methods=['POST'])
def create_store():
    request_data =request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    mongo.db.users.insert_many(new_store)
    return jsonify(new_store), 400

@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name']==name:
            mongo.db.users.find_one(store)
            return jsonify(store)
@app.route('/store')
def get_stores():
    mongo.db.users.find_one(store)
    return jsonify({'stores':stores}), 200

@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']== name:
            new_items = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_items)
            mongo.db.users.insert_many(new_items)
            return jsonify(new_items), 400
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
             mongo.db.users.insert_one(store)
             return jsonify({'items':store['items']}), 200
    return jsonify({'message': 'store not found'})
app.run(port=5000)
