"""CRUD operations."""

from model import db, User, Driver, connect_to_db

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

if __name__ == "__main__":
    from server import app

    connect_to_db(app)