"""Models for a F1 App"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from json import JSONEncoder

db = SQLAlchemy()

## Adding along tables and eventually relationships as I build additional functionality 

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = password = db.Column(db.String)
    lname = password = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    img = db.Column(db.String, nullable = True)

    def to_dict(self):
        return {'user_id': self.user_id,
                'fname': self.fname,
                'lname': self.lname,
                'email': self.email,
                'password': self.password,
                'img': self.img}

    likes = db.relationship("Like", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"

class Like(db.Model):
    """Table storing all likes for individual users"""

    __tablename__ = "likes"

    like_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))

    def to_dict(self):
        return {'like_id': self.like_id,
                'user_id': self.user_id,
                'driver_id': self.driver_id,
                }

    user = db.relationship("User", back_populates="likes")
    driver = db.relationship("Driver", back_populates="likes")

    def __repr__(self):
        return f"<Like like_id={self.like_id} user_id={self.user_id}>"

class Driver(db.Model):
    """Information on individual drivers"""

    __tablename__ = "drivers"

    driver_id = db.Column(db.Integer, primary_key=True, nullable = False)
    driver_api_ref = db.Column(db.String(255), unique = True)
    number = db.Column(db.String, nullable = True)
    code = db.Column(db.String(3), nullable = True)
    forename = db.Column(db.String(255), nullable = False)
    surname = db.Column(db.String(255), nullable = False)
    dob = db.Column(db.String, nullable = True) 
    nationality = db.Column(db.String(255), nullable = True) 
    url = db.Column(db.String(255), nullable = False)
    img_url = db.Column(db.String(400), nullable = False)
    active = db.Column(db.Boolean, nullable = True, default = False)

    results = db.relationship("Result", back_populates="driver")
    sprint_results = db.relationship("SprintResult", back_populates="driver")
    likes = db.relationship("Like", back_populates="driver")

    def to_dict(self):
        return {'driver_id': self.driver_id,
                'driver_api_ref': self.driver_api_ref,
                'number': self.number,
                'code': self.code,
                'forename': self.forename,
                'surname': self.surname,
                'dob': self.dob,
                'nationality': self.nationality,
                'url': self.url,
                'img_url': self.img_url,
                'active': self.active,}

    def __repr__(self):
        return f"<Driver driver_id={self.driver_id} surname={self.surname}>"

class Race(db.Model):
    """F1 Race information"""

    __tablename__ = "races"

    race_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer)
    round = db.Column(db.Integer)
    circuit_id = db.Column(db.Integer, db.ForeignKey("circuits.circuit_id"))
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

    sprint_results = db.relationship("SprintResult", back_populates="race")
    results = db.relationship("Result", back_populates="race")
    circuit = db.relationship("Circuit", back_populates="race")


    def __repr__(self):
        return f"<Race race_id={self.race_id} name={self.name}>"

class Constructor(db.Model):
    """Information for individual constructors"""

    __tablename__ = "constructors"

    constructor_id = db.Column(db.Integer, primary_key=True,nullable = False)
    constructor_api_ref = db.Column(db.String(300), nullable = False)
    name = db.Column(db.String(255))
    nationality = db.Column(db.String(300))
    url = db.Column(db.String(300))
    img = db.Column(db.String(300), nullable = True)

    results = db.relationship("Result", back_populates="constructor")
    sprint_results = db.relationship("SprintResult", back_populates="constructor")
    # qualifying_laps = db.relationship("QualifyingLap", back_populates="constructor")

    def to_dict(self):
        return {'constructor_id': self.constructor_id,
                'constructor_api_ref': self.constructor_api_ref,
                'name': self.name,
                'nationality': self.nationality,
                'url': self.url,
                'img': self.img,}

    def __repr__(self):
        return f"<Constructor constructor_id={self.constructor_id} name={self.name}>"


class Result(db.Model):
    """A melon."""

    __tablename__ = "results"

    result_id = db.Column(db.Integer, primary_key=True, nullable = False)
    race_id = db.Column(db.Integer, db.ForeignKey('races.race_id'))
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.driver_id'))
    constructor_id = db.Column(db.Integer, db.ForeignKey('constructors.constructor_id'))
    number = db.Column(db.String, nullable = True)
    grid = db.Column(db.String, nullable = False)
    position = db.Column(db.String, nullable = True)
    position_text = db.Column(db.String(255), nullable = False)
    position_order = db.Column(db.String, nullable = False )
    points = db.Column(db.String, nullable = False)
    laps = db.Column(db.String, nullable = False)
    time = db.Column(db.String(255), nullable = True)
    milliseconds = db.Column(db.String, nullable = True)
    fastest_lap = db.Column(db.String, nullable = True)
    rank = db.Column(db.String)
    fastest_lap_time = db.Column(db.String(255))
    fastest_lap_speed = db.Column(db.String(255))
    status_id = db.Column(db.String)

    driver = db.relationship("Driver", back_populates="results")
    constructor = db.relationship("Constructor", back_populates="results")
    race = db.relationship("Race", back_populates="results")

    def __repr__(self):
        return f"<Result result_id={self.result_id} race_id={self.race_id}>"

class SprintResult(db.Model):
    """A melon."""

    __tablename__ = "sprint_results"

    result_id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey("races.race_id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("drivers.driver_id"))
    constructor_id = db.Column(db.Integer, db.ForeignKey("constructors.constructor_id"))
    number = db.Column(db.String, nullable = True)
    grid = db.Column(db.String)
    position = db.Column(db.String, nullable = True)
    position_text = db.Column(db.String)
    position_order = db.Column(db.String)
    points = db.Column(db.String)
    laps = db.Column(db.String)
    time = db.Column(db.String, nullable = True)
    milliseconds = db.Column(db.String, nullable = True)
    fastest_lap = db.Column(db.String, nullable = True)
    fastest_lap_time = db.Column(db.String, nullable = True)
    status_id = db.Column(db.String)

    race = db.relationship("Race", back_populates="sprint_results")
    driver = db.relationship("Driver", back_populates="sprint_results")
    constructor = db.relationship("Constructor", back_populates="sprint_results")

    def __repr__(self):
        return f"<SprintResult result_id={self.result_id} race_id={self.race_id}>"

class Circuit(db.Model):
    """Table for circuits"""

    __tablename__ = "circuits"

    circuit_id = db.Column(db.Integer, primary_key = True, nullable = False)
    circuit_ref = db.Column(db.String(255), nullable = False)
    name = db.Column(db.String(255), nullable = False)
    location = db.Column(db.String(255), nullable = True)
    country = db.Column(db.String(255), nullable = True)
    lat = db.Column(db.String, nullable = True)
    lng = db.Column(db.String, nullable = True)
    alt = db.Column(db.String, nullable = True)
    url = db.Column(db.String(255), nullable = False)

    race = db.relationship("Race", back_populates="circuit")

    def __repr__(self):
        return f"<Circuit circuit_id={self.circuit_id} name={self.name}>"


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