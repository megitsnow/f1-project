"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import sys

import crud
import model
import server
from parsed_data import driver_data, races


os.system("dropdb f1")
os.system("createdb f1")

model.connect_to_db(server.app)
model.db.create_all()

# Create 10 users; each user will make 10 ratings
for n in range(10):
    fname = f'user{n}'
    lname = 'test'
    email = f"user{n}@test.com"  
    password = "test"

    user = crud.create_user(fname, lname, email, password)
    model.db.session.add(user)
    
model.db.session.commit()

# Seed drivers table 

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

# Seed races table

races_in_db = []

for i in races.keys():
    year, round, circuit_id, name, date, time, url , fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time = (
        races[i]["year"],
        races[i]["round"],
        races[i]["circuit_id"],
        races[i]["name"],
        races[i]["date"],
        races[i]["time"],
        races[i]["url"],
        races[i]["fp1_date"],
        races[i]["fp1_time"],
        races[i]["fp2_date"],
        races[i]["fp2_time"],
        races[i]["fp3_date"],
        races[i]["fp3_time"],
        races[i]["quali_date"],
        races[i]["quali_time"],
        races[i]["sprint_date"],
        races[i]["sprint_time"]
    )

    db_race = crud.create_race(year, round, circuit_id, name, date, time, url , fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time)
    races_in_db.append(db_race)

model.db.session.add_all(races_in_db)
model.db.session.commit()

