import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cooking'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:zqdtjBMRmkAtPWhe@cluster0-milxz.mongodb.net/cooking?retryWrites=true')
mongo = PyMongo(app)

app.secret_key='%\xdf\xca*\x03\xf3\xdf3\xf6)\xe31\xcd\xbb)\x17'

@app.route('/')
@app.route('/recipes')
def recipes():
    # check if there is a user in session then flashes
    if 'username' in session:
        flash('You were successfully logged in')
    recipes=mongo.db.recipes.find()
    print(recipes)
    return render_template("recipes.html", 
                           recipes=recipes)
     
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        users = mongo.db.users
        # finds the user in the database
        user_login = users.find_one({'name' : request.form['username']})
        if user_login:
            session['username'] = request.form['username']
            return redirect(url_for('recipes'))
        # if there is no user by that name and invalid user flash happens   
        flash("Invalid Log In")
    return render_template('login.html')
    
@app.route('/logout')
def logout():
    # session is false, and user is logged out
    session['username'] = False
    flash("You were successfully logged out")
    return render_template('login.html') 

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        # checks for existing user
        existing_user = users.find_one({'name' : request.form['username']})
        # if there is no existing use, registration goes ahead
        if existing_user is None:
            username = request.form["username"]
            country = request.form.get("country_name")
            users.insert_one({'name' : username, 'user_country' : country})
            session['username'] = request.form['username']
            return redirect(url_for('recipes'))
        flash("That username already exists!")
            
        
    return render_template('create_user.html',
                           countries=mongo.db.countries.find())



@app.route('/add_recipe', methods=['GET','POST'])
def add_recipe():
    recipes = mongo.db.recipes
    if request.method == 'POST':
        new_recipe = {'author': session['username'],}
        recipe_allergens = []
        # ingredients = []
        recipe=request.form
        # import pdb; pdb.set_trace()
        print(recipe)
        for key in recipe:
            print(key, request.form[key])
            if key in ['recipe_description','recipe_name','cuisine','recipe_instructions','recipe_image']:
                new_recipe[key]=request.form[key]
            elif key in ['5cb78b681c9d440000423101', '5cb78b841c9d440000423102', '5cb78b9c1c9d440000423103', '5cb78baa1c9d440000423104', '5cb78bb41c9d440000423105', '5cb78bbf1c9d440000423106', '5cb78bc91c9d440000423107', '5cb78bdc1c9d440000423108', '5cb78be71c9d440000423109', '5cb78bf31c9d44000042310a', '5cb78bfe1c9d44000042310b', '5cb78c081c9d44000042310c', '5cb78c141c9d44000042310d', '5cb78c211c9d44000042310e']:
                recipe_allergens.append(key)
                
            else:
                ingredients=request.form.getlist('ingredients-select')
                
        # print('ingredients',recipe_ingredients)
		# Then recipe_allergens is added to the new_recipe dict
        new_recipe['allergens']=recipe_allergens
        new_recipe['ingredients']=ingredients
        # import pdb; pdb.set_trace()
        print(new_recipe)
		# Then for your insert just pass in new_recipe
        recipes.insert_one(new_recipe)
        flash("Recipe successfully added")
        return redirect(url_for('recipes'))
    else:
        allergens = mongo.db.allergens.find()
        ingredients = mongo.db.ingredients.find()
        print(ingredients)
        return render_template('add_recipe.html',
                                cuisine=mongo.db.cuisine.find(),
                                allergens = allergens,
                                ingredients = ingredients)
# open recipes
@app.route('/open_recipes/<recipe_id>')
def open_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    recipe_allergens = []
    recipe_ingredients = []
    # import pdb; pdb.set_trace()
    for ingredient_id in the_recipe["ingredients"]:
        recipe_ingredients.append(mongo.db.ingredients.find_one({"_id": ObjectId(ingredient_id)}))
    for allergen_id in  the_recipe["allergens"]:
        recipe_allergens.append(mongo.db.allergens.find_one({"_id": ObjectId(allergen_id)}))
    the_recipe["allergens"] = recipe_allergens
    the_recipe["ingredients"] = recipe_ingredients
    return render_template('open_recipe.html', recipe=the_recipe)
    
    
# deletes the recipes
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('recipes'))
    
#  edit recipe 
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    allergens = mongo.db.allergens.find()
    ingredients = mongo.db.ingredients.find()
    return render_template('edit_recipe.html', recipe=the_recipe, cuisine=mongo.db.cuisine.find(), allergens=allergens, ingredients=ingredients)
    
@app.route('/user/<name>')
def user_recipes(name):
    name = session['username']
    # user = mongo.db.users.find_one(name = session['username'])
    recipes =   mongo.db.recipes.find({ 'author' : {  name } })
    return render_template('user_recipes.html',  name=name, recipes=recipes)
    
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    if request.method == 'POST':
		# This is going to be passed into mongo
        new_recipe = {'author': session['username'],}
        recipe_allergens = []
        # ingredients = []
        recipe=request.form
        # import pdb; pdb.set_trace()
        print(recipe)
        for key in recipe:
            print(key, request.form[key])
            if key in ['recipe_description','recipe_name','cuisine','recipe_instructions','recipe_image']:
                new_recipe[key]=request.form[key]
            elif key in ['5cb78b681c9d440000423101', '5cb78b841c9d440000423102', '5cb78b9c1c9d440000423103', '5cb78baa1c9d440000423104', '5cb78bb41c9d440000423105', '5cb78bbf1c9d440000423106', '5cb78bc91c9d440000423107', '5cb78bdc1c9d440000423108', '5cb78be71c9d440000423109', '5cb78bf31c9d44000042310a', '5cb78bfe1c9d44000042310b', '5cb78c081c9d44000042310c', '5cb78c141c9d44000042310d', '5cb78c211c9d44000042310e']:
                recipe_allergens.append(key)
                
            else:
                ingredients=request.form.getlist('ingredients-select')
                
        # print('ingredients',recipe_ingredients)
		# Then recipe_allergens is added to the new_recipe dict
        new_recipe['allergens']=recipe_allergens
        new_recipe['ingredients']=ingredients
		# Then recipe_allergens is added to the new_recipe dict
        new_recipe['allergens']=recipe_allergens
        print(new_recipe)
        # pushes the edit to database
        mongo.db.recipes.update( {'_id': ObjectId(recipe_id)}, new_recipe)
    flash('Recipe succesfully edited')
    return redirect(url_for('recipes'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)