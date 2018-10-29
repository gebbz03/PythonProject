from flask import Flask
from flask_pymongo import PyMongo

app=Flask(__name__)

app.config['MONGO_DBNAME']='gebbzpymongo'
app.config['MONGO_URI']='mongodb://gebbz:gebbz4ever@ds143451.mlab.com:43451/gebbzpymongo'

mongo=PyMongo(app)

@app.route('/add')

def add():
    user=mongo.db.users
    user.insert({'name':'Unknow','language':'PyJasdadCasd'})

    
    user.insert({'name':'Person 2','language':'Java'})
    user.insert({'name':'Person 3','language':'C'})
    user.insert({'name':'Person 4','language':'PHP'})
    

    return 'Added User!'


@app.route('/find')
def find():
    user=mongo.db.users
    person2=user.find_one({'name':'Person 2'})    
    return 'You found '+ person2['name'] + '. His favorite language is '+ person2['language']

@app.route('/update')
def update():
    user=mongo.db.users
    person2x=user.find_one({'name':'Person 2'})
    person2x['language']='Javascript, Java and Python'
    user.save(person2x)
    return 'Updated!'


@app.route('/delete')
def delete():
    user=mongo.db.users
    unk=user.find_one({'name':'Unknow'})
    user.remove(unk)
    return 'Removed Successfully'


if __name__=='__main__':
    app.run(debug=True)    


#run
#  http://127.0.0.1:5000/add    