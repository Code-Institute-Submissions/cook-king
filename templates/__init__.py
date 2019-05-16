import app
app = Flask(__name__)

# def country(recipe.author, users):

@app
def user_country(recipe.author, users):
    recipes = mongo.db.users.find({'$and':[filter_by,{'allergens': {'$nin' : filter_allergen}}]})

app.jinja_env.globals.update(user_country=user_country)