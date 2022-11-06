"""CRUD operations."""

from model import db, User, Driver, Race, connect_to_db

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    return user

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_driver(driver_api_ref, number, code, forename, surname, dob, nationality, url, img_url):
    """Create and return a new driver."""

    driver = Driver(
        driver_api_ref=driver_api_ref,
        number=number,
        code=code,
        forename=forename,
        surname = surname,
        dob = dob,
        nationality = nationality,
        url = url,
        img_url = img_url,
    )

    return driver

def create_race(year, round, circuit_id, name, date, time, url , fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time):
    """Create and return a new driver."""

    race = Race(
        year=year,
        round=round,
        circuit_id=circuit_id,
        name=name,
        date = date,
        time = time,
        url = url,
        fp1_date = fp1_date,
        fp1_time = fp1_time,
        fp2_date = fp2_date,
        fp2_time = fp2_time,
        fp3_date = fp3_date,
        fp3_time = fp3_time,
        quali_date = quali_date,
        quali_time = quali_time,
        sprint_date = quali_date,
        sprint_time = quali_time,
    )

    return race

if __name__ == "__main__":
    from server import app

    connect_to_db(app)