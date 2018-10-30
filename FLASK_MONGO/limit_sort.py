from flask import *
from flask_pymongo import *
import pymongo

app=Flask(__name__)

app.config['MONGO_DBNAME']='startrek'
app.config['MONGO_URI']='mongodb://gebbz:gebbz4ever@ds245523.mlab.com:45523/startrek'

mongo=PyMongo(app)



@app.route('/add')

def add():
    user=mongo.db.number
    user.insert({'number':2})
    user.insert({'number':3})
    user.insert({'number':4})
    user.insert({'number':5})
    user.insert({'number':6})
    user.insert({'number':7})
    

    return 'Added data!'


@app.route('/')
def index():
    people=mongo.db.people
    results=people.find().sort('name',pymongo.DESCENDING).limit(5)
    
    output=''
    for r in results:
        output+=r['name'] + '<br>'
    return output


if __name__ == '__main__':
    app.run(debug=True)
