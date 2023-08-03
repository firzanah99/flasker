from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') 

# safe
# capitalize = capitalize the first alphabet in each word
# lower = lowercase 
# upper = uppercase
# title = capitalize
# trim
# striptags

def index():
    first_name="John"
    stuff = "This is bold text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html", 
                           first_name=first_name, 
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

# localhost:5000/user/John
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)

# Create custom Error Page

#Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

#Internal server url
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html")