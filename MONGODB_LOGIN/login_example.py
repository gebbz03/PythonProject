from flask import *
from flask_pymongo import PyMongo
import bcrypt


app=Flask(__name__)

app.config['MONGO_DBNAME']='login_test'
app.config['MONGO_URI']='mongodb://gebbz:gebbz4ever@ds121686.mlab.com:21686/login_test'

mongo=PyMongo(app)


#---------------------------index---------------------------
@app.route('/')
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('index.html')




#---------------------------login---------------------------
@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'name' : request.form['username']})

    if login_user:
        hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())

        if bcrypt.hashpw(bytes(request.form['pass'], 'utf-8'), hashpass) == hashpass:
        #if bcrypt.hashpw(bytes(request.form['pass'], 'utf-8'), bytes(request.form['pass'], 'utf-8')) == bytes(request.form['pass'], 'utf-8'):
        #if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('index'))

    return 'Invalid username/password combination'




#---------------------------register---------------------------
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        
        return 'That username already exists!'

    return render_template('register.html')




if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(debug=True)