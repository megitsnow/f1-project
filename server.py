"""Server for F-1 app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, Constructor, Driver
import json
import crud
import os
import requests 

app = Flask(__name__)
app.secret_key = "dev"

API_KEY = os.environ["NEWS_API_KEY"]

@app.route("/")
def login():
    """Returns login page."""

    return render_template('index.html')

# Sign Up Routes
## Need to update this so that it looks up more than just the passwords matching
## Need to have it check if the user already exixts, if it is a valid email etc

@app.route("/api/sign-up", methods=["POST"])
def handle_signup():
    """Create a new user."""
    fname = request.json.get("fname")
    lname = request.json.get("lname")
    email = request.json.get("email")
    password = request.json.get("password")
    password_confirm = request.json.get("passwordConfirm")

    if password == password_confirm:
        user = crud.create_user(fname = fname, lname = lname, email = email, password = password)
        print("******** SIGN UP")
        print(user)
        db.session.add(user)
        db.session.commit()
    else:
        return {'Status': 400, "Message": "Passwords do not match"}

    return jsonify(user.to_dict())

# Log-In Routes 

@app.route("/api/log-in", methods=["POST"])
def handle_login():
    """Sign in a user and add to the session if already a user"""

    email = request.json.get("email")
    password = request.json.get("password")
    
    user = crud.get_user_by_email(email)

    if not user or user.password != password:
        print("The email or password you entered was incorrect.")
    else:
        session["user_email"] = user.email
        print(f"Welcome back, {user.email}!")

    return jsonify(user.to_dict())

# Constructor routes

@app.route("/api/constructors")
def constructor_logos():
    """Get constructor logos"""
    constructors = Constructor.query.filter(Constructor.img !=None).all()
    return jsonify({constructor.constructor_id: constructor.to_dict() for constructor in constructors})

@app.route("/constructors/<constructor_id>")
def constructor_indiv_info(constructor_id):
    """Get individual constructor information"""
    print("*************************")
    print(constructor_id)
    constructor = crud.get_constructor_by_id(constructor_id)
    return jsonify(constructor.to_dict())  

# Driver routes. To include route for each individual driver like we have for the constructors

@app.route("/api/active_drivers")
def active_driver_data():
    """Get active drivers"""
    active_drivers = Driver.query.filter_by(active = 'True').all()
    return jsonify({active_driver.driver_id: active_driver.to_dict() for active_driver in active_drivers})

# Route for recent news 

@app.route("/api/recent-news")
def get_recent_articles():
    """Get recent articles"""
    url =f'https://newsapi.org/v2/everything?q=F1 Racing&from=2022-11-12&sortBy=popularity&apiKey={API_KEY}'

    response = requests.get(url)
    data = response.json()
    news_list = data['articles']

    news_articles = []

    for i in range(len(news_list)):
        article= {
        "title": data['articles'][i]['title'],
        "description": data['articles'][i]['description'],
        "url": data['articles'][i]['url'],
        "url_to_img": data['articles'][i]['urlToImage']
        }
        news_articles.append(article)
    
    return jsonify(news_articles)
    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)