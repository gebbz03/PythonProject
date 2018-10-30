from flask import *
from flask_pymongo import *
import pymongo

app=Flask(__name__)

app.config['MONGO_DBNAME']='pagination'
app.config['MONGO_URI']='mongodb://gebbz:gebbz4ever@ds245523.mlab.com:45523/pagination'

mongo=PyMongo(app)

@app.route('/numbers',methods=['GET'])
def numbers():
    #http://127.0.0.1:5000/numbers?limit=5&offset=15
    number=mongo.db.number
    
    offset=int(request.args['offset'])
    limit=int(request.args['limit'])

    starting_id=number.find().sort('_id',pymongo.ASCENDING)
    last_id=starting_id[offset]['_id']

    numbers=number.find({'_id':{'$gte':last_id}}).sort('_id',pymongo.ASCENDING).limit(limit)

    output=[]

    for i in numbers:
        output.append({'number':i['number']})

    next_url='/numbers?limit='+str(limit)+'&offset='+str(offset+limit)
    prev_url='/numbers?limit='+str(limit)+'&offset='+str(offset-limit)    
        
    return jsonify({'result':output,'prev_url':prev_url,'next_url':next_url})    


if __name__ == '__main__':
    app.run(debug=True)