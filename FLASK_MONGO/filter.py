from flask import Flask
from flask_pymongo import *

app=Flask(__name__)

app.config['MONGO_DBNAME']='mongo_numbers'
app.config['MONGO_URI']='mongodb://gebbz:gebbz4ever@ds145053.mlab.com:45053/mongo_numbers'

mongo=PyMongo(app)

@app.route('/add')
def add():
    numbers=mongo.db.numbers
    numbers.insert({'name':'seven','number':7})
    numbers.insert({'name':'eight','number':8})
    numbers.insert({'name':'nine','number':9})
    numbers.insert({'name':'ten','number':10})
    numbers.insert({'name':'eleven','number':11})
    numbers.insert({'name':'twelve','number':12})
    
    return 'Added successfully'

@app.route('/')
def index():
    numbers=mongo.db.numbers

    # find() - all

    # single search or filter
    #results=numbers.find({'name':'two'})

    # $lt - less than
    #results=numbers.find({'number':{'$lt':4}})

    # $lte - less than equal
    #results=numbers.find({'number':{'$lt':4}})

    # $gt - greater than
    #results=numbers.find({'number':{'$gt':4}})

    # $gte - greater than equal
    #results=numbers.find({'number':{'$gte':4}})

    # $eq - equal
    #results=numbers.find({'number':{'$eq':4}})

    # $ne - not equal
    #results=numbers.find({'number':{'$ne':4}})
    #results=numbers.find({'name':{'$ne':'two'}})

    # double filter
    #results=numbers.find({'number':{'$lt':4}, 'name':{'$gt':'g'}})

    # $or - OR function
    #results=numbers.find({'$or': [{'number' : {'$gt' : 5}},{'number' : {'$lt' : 5}}]})

    results=numbers.find({'$or': [{'number' : {'$gt' : 5}},{'number' : {'$lt' : 5}}]})

    output=''
    for r in results:
        output += r['name'] + ' - ' + str(r['number']) + '<br>'

    return output


if __name__ == '__main__':
    app.run(debug=True)