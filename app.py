import os
from flask import Flask
app = Flask(__name__)
# app.config["MONGO_DBNAME"] = 'cooking'
# app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:goodbowie44@myfirstcluster-milxz.mongodb.net/cooking?retryWrites=true')
# # mongo = PyMongo(app)

@app.route('/')
def hello():
    return "hello world"
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)