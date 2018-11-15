from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://questions:questions1@ds121321.mlab.com:21321/connect_to_mongo'
mongo = PyMongo(app)
@app.route('/framework',methods=['GET'])
def get_all_frameworks():
    user = mongo.db.users
    output =[]
    for q in user.find():
        output.append({'name': q['name'], 'language': q['language']})
    return jsonify({'result': output})
@app.route('/framework/<name>', methods=['GET'])
def get_one_framework(name):
    user = mongo.db.framework
    q = user.find_one({'name': name})
    output = {'name': q['name']}
    return jsonify({'result' : output})
@app.route('/framework', methods=['POST'])
def add_framework():
    user = mongo.db.framework
    name = request.json['name']
    language = request.json['language']
    user_id= user.insert({'name': name, 'language': language})
    new_user = user.find_one({'_id': user_id})
    output = {'name': new_user['name'],'language': new_user['language']}
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)