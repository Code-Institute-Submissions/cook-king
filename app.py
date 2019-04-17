import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cooking'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:zqdtjBMRmkAtPWhe@cluster0-milxz.mongodb.net/cooking?retryWrites=true')
mongo = PyMongo(app)

class BaseObject(object):
    app.secret_key='%\xdf\xca*\x03\xf3\xdf3\xf6)\xe31\xcd\xbb)\x17'
@app.route('/')
@app.route('/recipes')
def recipes():
    if 'username1' in session:
        return 'You are logged in as ' + session['username1']
    return render_template("recipes.html", 
                           recipes=mongo.db.recipes.find())
     
@app.route('/login', methods=['POST', 'GET'])
def login():
    users = mongo.db.users
    user_login = users.find.one({'name' : request.form['username']})
    if user_login:
        session['username'] = request.form['username']
        return redirect(url_for('recipes'))
    return "Invalid Log In"

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'name' : request.form['username']})
        if existing_user is None:
            username = request.form["username"]
            country = request.form.get("country_name")
            print(country)
            users.insert_one({'name' : username, 'user_country' : country})
            session['username1'] = request.form['username']
            return redirect(url_for('recipes'))
        return "That username already exists!"
    return render_template('create_user.html',
                           countries=mongo.db.countries.find())
                           
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)