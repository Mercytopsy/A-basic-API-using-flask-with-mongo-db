# A basic API using_flask_with-mongoDB

This is a basic Api showing a list of people and the frameworks each person specialize in using for development

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install flask and PyMongo.

```bash
pip install Flask
pip install pymongo
```

## Usage

```python

from flask import Flask, jsonify, request
from flask_pymongo import PyMongo


```

## MONGODB-INTEGRATION
app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://questions:questions1@ds121321.mlab.com:21321/connect_to_mongo'



## TESTING_API
if __name__ == '__main__':
    app.run(debug=True)
