from flask import *
from flask_pymongo import *


app=Flask(__name__)

app.config['MONGO_DBNAME']='startrek'
app.config['MONGO_URI']='mongodb://gebbz:gebbz4ever@ds245523.mlab.com:45523/startrek'

mongo=PyMongo(app)






@app.route('/framework',methods=['GET'])
def get_all_frameworks():
    #127.0.0.1:5000/framework
    framework=mongo.db.framework

    output=[]

    for q in framework.find():
        output.append({'name':q['name'],'code':q['code']})

    return jsonify({'result':output})    






@app.route('/framework/<name>',methods=['GET'])
def get_one_framework(name):
    #127.0.0.1:5000/framework/Flask
    framework=mongo.db.framework
    q=framework.find_one({'name':name})

    if q:
        output={'name':q['name'],'code':q['code']}
    else:
        output ='No results found'    

    return jsonify({'result':output})





@app.route('/framework',methods=['POST'])
def add_framework():
    #POST -> BODY -> RAW
    #{"name":"JAVAFX","code":"Java"}
    framework=mongo.db.framework

    name=request.json['name']
    code=request.json['code']
    framework_id=framework.insert({'name':name,'code':code})
    new_framework=framework.find_one({'_id':framework_id})

    output={'name': new_framework['name'],'code':new_framework['code']}

    return jsonify({'result':output})



if __name__ == '__main__':
    app.run(debug=True) 