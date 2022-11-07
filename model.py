"""Models for movie ratings app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = password = db.Column(db.String)
    lname = password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Driver(db.Model):
    """Information on Drivers"""

    __tablename__ = "drivers"

    driver_id = db.Column(db.Integer, primary_key=True, autoincrement = True, nullable = False)
    driver_api_ref = db.Column(db.String(255), unique = True)
    number = db.Column(db.String, nullable = True)
    code = db.Column(db.String(3), nullable = True)
    forename = db.Column(db.String(255), nullable = False)
    surname = db.Column(db.String(255), nullable = False)
    dob = db.Column(db.String, nullable = True) 
    nationality = db.Column(db.String(255), nullable = True) 
    url = db.Column(db.String(255), nullable = False)
    img_url = db.Column(db.String(400), nullable = False)

    def __repr__(self):
        return f"<Driver driver_id={self.driver_id} surname={self.surname}>"

class Race(db.Model):
    """F1 Race information"""

    __tablename__ = "races"

    race_id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    year = db.Column(db.Integer)
    round = db.Column(db.Integer)
    circuit_id = db.Column(db.Integer)
    name = db.Column(db.String(255))
    date = db.Column(db.String(255))
    time = db.Column(db.String(255)) 
    url = db.Column(db.String(255))
    fp1_date = db.Column(db.String(255))
    fp1_time = db.Column(db.String(255))
    fp2_date = db.Column(db.String(255))
    fp2_time = db.Column(db.String(255))
    fp3_date = db.Column(db.String(255))
    fp3_time = db.Column(db.String(255))
    quali_date = db.Column(db.String(255))
    quali_time = db.Column(db.String(255))
    sprint_date = db.Column(db.String(255))
    sprint_time = db.Column(db.String(255))


    def __repr__(self):
        return f"<Race race_id={self.race_id} name={self.name}>"


def connect_to_db(flask_app, db_uri="postgresql:///f1", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__ == "__main__":
    from server import app

    connect_to_db(app)