"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import sys

import crud
import model
import server
from drivers import driver_data


os.system("dropdb f1")
os.system("createdb f1v1")

model.connect_to_db(server.app)
model.db.create_all()

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"  
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

model.db.session.commit()

driver_in_db = []

for i in driver_data.keys():
    driver_api_ref, number, code, forename, surname, dob, nationality, url, img_url = (
        driver_data[i]["driverRef"],
        driver_data[i]["number"],
        driver_data[i]["code"],
        driver_data[i]["forename"],
        driver_data[i]["surname"],
        driver_data[i]["dob"],
        driver_data[i]["nationality"],
        driver_data[i]["url"],
        driver_data[i]["img"],
    )
    
    db_driver = crud.create_driver(driver_api_ref, number, code, forename, surname, dob, nationality, url, img_url)
    driver_in_db.append(db_driver)

model.db.session.add_all(driver_in_db)
model.db.session.commit()

print(driver_in_db)

