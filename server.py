"""Server for F-1 app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, Constructor, Driver, Race, Result, Like, User
import json
import cloudinary.uploader
import crud
import os
import requests 

app = Flask(__name__)
app.secret_key = "dev"

API_KEY = os.environ["NEWS_API_KEY"]
CLOUDINARY_KEY = os.environ["CLOUDINARY_API_KEY"]
CLOUDINARY_SECRET = os.environ["CLOUDINARY_API_SECRET"]
CLOUD_NAME = "dzqtjox0u"

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

    if crud.get_user_by_email(email) is None and password == password_confirm:
        print("user does not exist!!")
        user = crud.create_user(fname = fname, lname = lname, email = email, password = password)
        db.session.add(user)
        db.session.commit()
        session["user_email"] = user.email
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
        print("****************************** LOG IN")
        print(session["user_email"])
        print(f"Welcome back, {user.email}!")

    return jsonify(user.to_dict())

# Constructor routes

@app.route("/api/user-information")
def user_information():
    """Get user information"""
    user_email = session["user_email"]
    user = User.query.filter_by(email = user_email).first()
    return jsonify(user.to_dict())

@app.route("/api/constructors")
def constructor_logos():
    """Get constructor logos"""
    constructors = Constructor.query.filter(Constructor.img !=None).all()
    return jsonify({constructor.constructor_id: constructor.to_dict() for constructor in constructors})

@app.route("/constructors/<constructor_id>")
def constructor_indiv_info(constructor_id):
    """Get individual constructor information"""
    print(constructor_id)
    constructor = crud.get_constructor_by_id(constructor_id)
    return jsonify(constructor.to_dict())  

# Driver routes. To include route for each individual driver like we have for the constructors

@app.route("/drivers/<driver_id>")
def driver_indiv_info(driver_id):
    """Get individual driver information"""
    print(driver_id)
    race_results = (
    db.session.query(Race.race_id, Driver.forename, Driver.surname, Driver.nationality, Race.name, Result.points, Result.position, Driver.img_url)
    .join(Result, Result.race_id == Race.race_id)
    .join(Driver, Driver.driver_id == Result.driver_id)
    .filter(Driver.driver_id == driver_id).all()
    )

    driver_race_results = {}

    for i, value in enumerate(race_results):
        list_items = list(value)
        for i, item in enumerate(list_items):
            race = {}
            race_id = str(list_items[0])
            if i == 0: 
                driver_race_results[race_id] = {}
            elif i == 1:
                driver_race_results[race_id]['fname'] = item
            elif i == 2:
                driver_race_results[race_id]['lname'] = item
            elif i == 3:
                driver_race_results[race_id]['nationality'] = item
            elif i == 4:
                driver_race_results[race_id]['race_name'] = item
            elif i == 5:
                driver_race_results[race_id]['points'] = item
            elif i == 6:
                driver_race_results[race_id]['position'] = item
            elif i == 7:
                driver_race_results[race_id]['img_url'] = item

    return jsonify(driver_race_results)  

@app.route("/api/driver-like", methods=["POST"])
def create_user_like():
    """Sign in a user and add to the session if already a user"""

    driver_id = request.json.get("driverId")
    logged_in_email = session.get("user_email")
    print(f"LINE 128 {driver_id}")
    print(logged_in_email)

    user = crud.get_user_by_email(logged_in_email)
    like = crud.create_like(user.user_id, driver_id)
    db.session.add(like)
    db.session.commit()

    return jsonify(like.to_dict())

@app.route("/api/user-like")
def render_user_likes():
    """Sign in a user and add to the session if already a user"""

    logged_in_email = session.get("user_email")

    user = crud.get_user_by_email(logged_in_email)
    likes_by_user = Like.query.filter_by(user_id = user.user_id).all()
    
    driver_info_per_like = (
    db.session.query(Like.like_id, Driver.forename, Driver.surname, Driver.img_url, Driver.nationality, Driver.driver_id)
    .join(Like, Like.driver_id == Driver.driver_id)
    .filter(Like.user_id == '1').all()
    )
    
    user_likes = {}

    for i, value in enumerate(driver_info_per_like):
        list_items = list(value)
        for i, item in enumerate(list_items):
            like = {}
            like_id = str(list_items[0])
            if i == 0: 
                user_likes[like_id] = {}
            elif i == 1:
                user_likes[like_id]['fname'] = item
            elif i == 2:
                user_likes[like_id]['lname'] = item
            elif i == 3:
                user_likes[like_id]['img'] = item
            elif i == 4:
                user_likes[like_id]['nationality'] = item
            elif i == 5:
                user_likes[like_id]['id'] = item

    return jsonify(user_likes)

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

# @app.route("/api/cloudinary")
# def handle_cloudinary():
#     """Handle cloudinary"""

#     picture = request.json.get("my-file")
#     user_email = session["user_email"]
#     user = crud.get_user_by_email(user_email)
#     user.img = picture

#     return jsonify(user.to_dict())
    


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)