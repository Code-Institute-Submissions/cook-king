import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cooking'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:goodbowie44@myfirstcluster-milxz.mongodb.net/cooking?retryWrites=true')
mongo = PyMongo(app)

@app.route('/')
@app.route('/recipes')
def recipes():
    return render_template("recipes.html", 
                           tasks=mongo.db.recipes.find())
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)