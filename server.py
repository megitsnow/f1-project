"""Server for F-1 app."""

from flask import Flask, render_template, request, flash, session, redirect
from model import connect_to_db, db
import crud
import os

app = Flask(__name__)
app.secret_key = "dev"

API_KEY = os.environ["NEWS_API_KEY"]

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)