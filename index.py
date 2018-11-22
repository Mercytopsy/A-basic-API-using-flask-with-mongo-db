from flask import Flask,jsonify,request
from bson.objectid import ObjectId
from pymongo import MongoClient
import os
app = Flask(__name__)
client = MongoClient("mongodb://127.0.0.1:27017") #host uri  
db = client.my_data   #Select the database  
new_data = db.questions #Select the collection name 

#All the names and languages can be gotten here
@app.route('/language', methods=['GET'])
def find_all():
    output =[]
    for q in new_data.find():
        output.append({'name': q['name'], 'language': q['language']})
    return jsonify({'result': output}), 200

#The name of each person according to the input can be gotten here
@app.route('/language/<string:name>', methods=['GET'])
def find(name):
    q = new_data.find_one({'name': name})
    output = {'name': q['name']}
    return jsonify({'result' : output}), 200


#All names and languages are added here
@app.route("/language", methods=['POST'])
def add_task():
    #Adding a Task 
    data = request.get_json()
    if data.get('name', None) is not None and data.get('language', None) is not None:
        new_data.insert_one(data)
        return jsonify({'ok': True, 'message': 'User created successfully!'}), 200
    else:
        return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400

#Update names
@app.route("/language", methods=['PUT'])  
def update ():  
     task=new_data.find_one({'name': 'kelly'})
     task['language'] = 'Ruby'
     new_data.save(task)  
     return jsonify({'ok': True, 'message': 'record updated'}), 200

#Delete name and language
@app.route("/language", methods=['DELETE'])  
def remove ():  
    #Deleting a Task with various references 
    name=request.json['name']
    language=request.json['language']
    key=new_data.find_one({'name': name, 'language': language})
    new_data.remove(key)  
    return jsonify({'ok': True, 'message': 'record deleted'})

    
if __name__ == '__main__':
    app.run(debug=True)