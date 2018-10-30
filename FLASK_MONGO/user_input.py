from flask import *
from flask_pymongo import *
from bson.json_util import dumps
import pymongo

app=Flask(__name__)

app.config['MONGO_DBNAME']='mongo_numbers'
app.config['MONGO_URI']='mongodb://gebbz:gebbz4ever@ds145053.mlab.com:45053/mongo_numbers'

mongo=PyMongo(app)

@app.route('/',methods=['POST'])
def index():
    #postman query
    #{"q":{"number":{"$lt":6}},"s":"desc"}
    query=request.json['q']
    sort_direction=request.json['s']
    numbers=mongo.db.numbers

    if sort_direction == 'asc':
        result=numbers.find(query)
    else:
        result=numbers.find(query).sort('number',pymongo.DESCENDING)



    return dumps(result)




if __name__ == '__main__':
    app.run(debug=True)    