"""Server for F-1 app."""

from flask import Flask, render_template, request, flash, session, redirect, jsonify
from model import connect_to_db, db
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
def handle_login():
    """Create a new user."""
    fname = request.json.get("fname")
    lname = request.json.get("lname")
    email = request.json.get("email")
    password = request.json.get("password")

    user = crud.create_user(fname = fname, lname = lname, email = email, password = password)
    db.session.add(user)
    db.session.commit()


    return jsonify(user)
        

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)