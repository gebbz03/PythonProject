from flask import *
from flask_pymongo import *


app=Flask(__name__)

app.config['MONGO_DBNAME']='startrek'
app.config['MONGO_URI']='mongodb://gebbz:gebbz4ever@ds245523.mlab.com:45523/startrek'

mongo=PyMongo(app)

@app.route('/add_episode/<code>/<name>/<season>')
def add_episode(code,name,season):
    #sample in browser
    #http://127.0.0.1:5000/add_episode/SP4/Spiderman/5
    series=mongo.db.series
    the_series=series.find_one({'code':code})

    episodes=mongo.db.episodes
    episodes.insert({'name':name,'season':season,'series_id':the_series['_id']})

    return 'Added ' + name + ' to the collection!'


@app.route('/get_episodes/<code>')
def get_episodes(code):
    series=mongo.db.series
    the_series=series.find_one({'code':code})    

    episodes=mongo.db.episodes
    series_episodes=episodes.find({'series_id':the_series['_id']})
    
    episode_list=''

    for e in series_episodes:
        episode_list += e['name'] + '---------'

    return episode_list    


if __name__ == '__main__':
    app.run(debug=True)