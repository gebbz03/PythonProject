# https://pythonhosted.org/Flask-MongoAlchemy/

from flask import Flask
from  import MongoAlchemy


app=Flask(__name__)

app.config['MONGOALCHEMY_DATABASE']='datagebbz'
app.config['MONGOALCHEMY_CONNECTION_STRING']='mongodb://gebbz:gebbz4ever@ds143683.mlab.com:43683/datagebbz'

db=MongoAlchemy(app)



class User(db.Document):
     namex=db.StringField()
     password=db.StringField()

     



#RUN
#user=User(namex='User',password='password')
       