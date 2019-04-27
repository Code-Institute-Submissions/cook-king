import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cooking'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb+srv://root:zqdtjBMRmkAtPWhe@cluster0-milxz.mongodb.net/cooking?retryWrites=true')
mongo = PyMongo(app)

class BaseObject(object):
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
		# This is going to be passed into mongo
        new_recipe = {'author': session['username'],}
		# This is to hold allergens and then added to new_recipe 
		# which we just created above
        recipe_allergens = []
		
		# Get the data from the form
        recipe=request.form
        print(recipe)
        # Loop through the keys
        for key in recipe:
            print(key, request.form[key])
			# Checks if key == your name fields that are not allergens
            if key == 'recipe_description' or key == 'recipe_name' or key == 'cuisine' or key == 'recipe_instructions' or key == 'recipe_image':
				# adds them to the dictionary created above
                new_recipe[key]=request.form[key]
            else:
				# recipe_allergens: ['egg', 'milk']
				# second one gives
				# recipe_allergens: [{'milk': milk} {'egg': egg}]
				
                recipe_allergens.append(request.form[key])
                # recipe_allergens.append({key: request.form[key]})
        
		# Then recipe_allergens is added to the new_recipe dict
        new_recipe['allergens']=recipe_allergens
        print(new_recipe)
		# Then for your insert just pass in new_recipe
        recipes.insert_one(new_recipe)
        flash("Recipe successfully added")
        return redirect(url_for('recipes'))
    else:
        allergens = mongo.db.allergens.find()
        return render_template('add_recipe.html',
                                cuisine=mongo.db.cuisine.find(),
                                allergens=allergens)
# open recipes
@app.route('/open_recipes/<recipe_id>')
def open_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
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
    return render_template('edit_recipe.html', recipe=the_recipe, cuisine=mongo.db.cuisine.find(), allergens=allergens)
    
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipe = mongo.db.recipes
    if request.method == 'POST':
		# This is going to be passed into mongo
        new_recipe = {'author': session['username'],}
		# This is to hold allergens and then added to new_recipe 
		# which we just created above
        recipe_allergens = []
		
		# Get the data from the form
        recipe=request.form
        print(recipe)
        # Loop through the keys
        for key in recipe:
            print(key, request.form[key])
			# Checks if key == your name fields that are not allergens
            if key == 'recipe_description' or key == 'recipe_name' or key == 'cuisine' or key == 'recipe_instructions' or key == 'recipe_image':
				# adds them to the dictionary created above
                new_recipe[key]=request.form[key]
            else:
				# recipe_allergens: ['egg', 'milk']
				# second one gives
				# recipe_allergens: [{'milk': milk} {'egg': egg}]
				
                recipe_allergens.append(request.form[key])
                # recipe_allergens.append({key: request.form[key]})
        
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