"""Server for F-1 app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db, Constructor, Driver
import json
import crud
import os

app = Flask(__name__)
app.secret_key = "dev"

API_KEY = os.environ["NEWS_API_KEY"]

@app.route("/")
def login():
    """Returns login page."""

    return render_template('index.html')

@app.route("/api/sign-up", methods=["POST"])
def handle_signup():
    """Create a new user."""
    fname = request.json.get("fname")
    lname = request.json.get("lname")
    email = request.json.get("email")
    password = request.json.get("password")

    user = crud.create_user(fname = fname, lname = lname, email = email, password = password)
    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict())

@app.route("/api/log-in", methods=["POST"])
def handle_login():
    """Create a new user."""

    email = request.json.get("email")
    password = request.json.get("password")
    
    user = crud.get_user_by_email(email)
    print("*******************************")
    print(user)

    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")

    return jsonify(user.to_dict())

@app.route("/api/constructors")
def constructor_logos():
    """Get constructor logos"""
    constructors = Constructor.query.filter(Constructor.img !=None).all()
    return jsonify({constructor.constructor_id: constructor.to_dict() for constructor in constructors})

@app.route("/constructors/<constructor_id>")
def constructor_indiv_info(constructor_id):
    """Get individual constructor information"""
    constructor_id = request.args.get("constructorId")
    print(constructor_id)
    constructor = crud.get_constructor_by_id(constructor_id)
    return jsonify(constructor.to_dict())  

@app.route("/api/active_drivers")
def active_driver_data():
    """Get active drivers"""
    active_drivers = Driver.query.filter_by(active = 'True').all()
    return jsonify({active_driver.driver_id: active_driver.to_dict() for active_driver in active_drivers})

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)