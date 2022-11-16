"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
import sys

import crud
import model
import server
from parsed_data import driver_data, races, constructor_data, results, sprint_results, status
from model import Constructor, Driver


os.system("dropdb f1")
os.system("createdb f1")

model.connect_to_db(server.app)
model.db.create_all()

# Create 10 users
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
    driver_id, driver_api_ref, number, code, forename, surname, dob, nationality, url, img_url = (
        i,
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
    db_driver = crud.create_driver(driver_id, driver_api_ref, number, code, forename, surname, dob, nationality, url, img_url)
    driver_in_db.append(db_driver)

model.db.session.add_all(driver_in_db)
model.db.session.commit()

# Seed races table

races_in_db = []

for i in races.keys():
    race_id, year, round, circuit_id, name, date, time, url , fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time = (
        i,
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

    db_race = crud.create_race(race_id, year, round, circuit_id, name, date, time, url , fp1_date, fp1_time, fp2_date, fp2_time, fp3_date, fp3_time, quali_date, quali_time, sprint_date, sprint_time)
    races_in_db.append(db_race)

model.db.session.add_all(races_in_db)
model.db.session.commit()

# Seed constructors to the db

constructor_in_db = []

for i in constructor_data.keys():
    constructor_id, constructor_api_ref, name, nationality, url = (
        i,
        constructor_data[i]["constructorRef"],
        constructor_data[i]["name"],
        constructor_data[i]["nationality"],
        constructor_data[i]["url"]
    )
    db_constructor = crud.create_constructor(constructor_id, constructor_api_ref, name, nationality, url)
    constructor_in_db.append(db_constructor)

model.db.session.add_all(constructor_in_db)
model.db.session.commit()


# seed the results table

result_in_db = []

for i in results.keys():
    result_id, race_id, driver_id, constructor_id ,number, grid, position, position_text, position_order, points, laps, time, milliseconds, fastest_lap, rank, fastest_lap_time, fastest_lap_speed, status_id = (
        i,
        results[i]["race_id"],
        results[i]["driver_id"],
        results[i]["constructor_id"],
        results[i]["number"],
        results[i]["grid"],
        results[i]["position"],
        results[i]["position_text"],
        results[i]["position_order"],
        results[i]["points"],
        results[i]["laps"],
        results[i]["time"],
        results[i]["milliseconds"],
        results[i]["fastest_lap"],
        results[i]["rank"],
        results[i]["fastest_lap_time"],
        results[i]["fastest_lap_speed"],
        results[i]["status_id"],
    )

    db_result = crud.create_result(result_id, race_id, driver_id, constructor_id ,number, grid, position, position_text, position_order, points, laps, time, milliseconds, fastest_lap, rank, fastest_lap_time, fastest_lap_speed, status_id)
    result_in_db.append(db_result)

model.db.session.add_all(result_in_db)
model.db.session.commit()

# seed the results table

sprint_result_in_db = []

for i in sprint_results.keys():
    result_id, race_id, driver_id, constructor_id ,number, grid, position, position_text, position_order, points, laps, time, milliseconds, fastest_lap, fastest_lap_time, status_id = (
        i,
        sprint_results[i]["race_id"],
        sprint_results[i]["driver_id"],
        sprint_results[i]["constructor_id"],
        sprint_results[i]["number"],
        sprint_results[i]["grid"],
        sprint_results[i]["position"],
        sprint_results[i]["position_text"],
        sprint_results[i]["position_order"],
        sprint_results[i]["points"],
        sprint_results[i]["laps"],
        sprint_results[i]["time"],
        sprint_results[i]["milliseconds"],
        sprint_results[i]["fastest_lap"],
        sprint_results[i]["fastest_lap_time"],
        sprint_results[i]["status_id"],
    )

    db_sprint_result = crud.create_sprint_result(result_id, race_id, driver_id, constructor_id ,number, grid, position, position_text, position_order, points, laps, time, milliseconds, fastest_lap, fastest_lap_time, status_id)
    sprint_result_in_db.append(db_sprint_result)

model.db.session.add_all(sprint_result_in_db)
model.db.session.commit()

# seed statuses in DB

# status_in_db = []

# for key,value in status.items():
#     status_id, status = (
#         key,
#         value['status']
#     )
    
#     db_status = crud.create_status(status_id, status)
#     status_in_db.append(db_status)

# model.db.session.add_all(status_in_db)
# model.db.session.commit()


# Update photos for active drivers to F1 Website photo & set as active
## To Update to to include lists and one function to loop over Drivers and one function to loop 
## over constructors. Use the below to also confirm that I was grabbing the correct ID as a lot of 
## drivers have the same last name 

verstappen = Driver.query.filter_by(driver_id = "830").first()
verstappen.img_url = '/static/imgs/drivers/Verstappen.jpeg'
verstappen.active = True
model.db.session.add(verstappen)
model.db.session.commit()

perez = Driver.query.filter_by(driver_id = "815").first()
perez.img_url = '/static/imgs/drivers/Perez.jpeg'
perez.active = True
model.db.session.add(perez)
model.db.session.commit()

russell = Driver.query.filter_by(driver_id = "847").first()
russell.img_url = '/static/imgs/drivers/Russel.jpeg'
russell.active = True
model.db.session.add(russell)
model.db.session.commit()


hamilton = Driver.query.filter_by(driver_id = "1").first()
hamilton.img_url = '/static/imgs/drivers/Hamilton.jpeg'
hamilton.active = True
model.db.session.add(hamilton)
model.db.session.commit()

sainz = Driver.query.filter_by(driver_id = "832").first()
sainz.img_url = '/static/imgs/drivers/Sainz.jpeg'
sainz.active = True
model.db.session.add(sainz)
model.db.session.commit()

ocon = Driver.query.filter_by(driver_id = "839").first()
ocon.img_url = '/static/imgs/drivers/Ocon.jpeg'
ocon.active = True
model.db.session.add(ocon)
model.db.session.commit()

alonso = Driver.query.filter_by(driver_id = "4").first()
alonso.img_url = '/static/imgs/drivers/Alonso.jpeg'
alonso.active = True
model.db.session.add(alonso)
model.db.session.commit()

bottas = Driver.query.filter_by(driver_id = "822").first()
bottas.img_url = '/static/imgs/drivers/Bottas.jpeg'
bottas.active = True
model.db.session.add(bottas)
model.db.session.commit()

vettel = Driver.query.filter_by(driver_id = "20").first()
vettel.img_url = '/static/imgs/drivers/Vettel.jpeg'
vettel.active = True
model.db.session.add(vettel)
model.db.session.commit()

ricciardo = Driver.query.filter_by(driver_id = "817").first()
ricciardo.img_url = '/static/imgs/drivers/Ricardo.jpeg'
ricciardo.active = True
model.db.session.add(ricciardo)
model.db.session.commit()

magnussen = Driver.query.filter_by(driver_id = "825").first()
magnussen.img_url = '/static/imgs/drivers/Magnessun.jpeg'
magnussen.active = True
model.db.session.add(magnussen)
model.db.session.commit()

leclerc = Driver.query.filter_by(driver_id = "844").first()
leclerc.img_url = '/static/imgs/drivers/Leclerc.jpeg'
leclerc.active = True
model.db.session.add(leclerc)
model.db.session.commit()

gasly = Driver.query.filter_by(driver_id = "842").first()
gasly.img_url = '/static/imgs/drivers/Gasly.jpeg'
gasly.active = True
model.db.session.add(gasly)
model.db.session.commit()

stroll = Driver.query.filter_by(driver_id = "840").first()
stroll.img_url = '/static/imgs/drivers/Stroll.jpeg'
stroll.active = True
model.db.session.add(stroll)
model.db.session.commit()

schumacher = Driver.query.filter_by(driver_id = "854").first()
schumacher.img_url = '/static/imgs/drivers/Schumaker.jpeg'
schumacher.active = True
model.db.session.add(schumacher)
model.db.session.commit()

tsunoda = Driver.query.filter_by(driver_id = "852").first()
tsunoda.img_url = '/static/imgs/drivers/Tsuonada.jpeg'
tsunoda.active = True
model.db.session.add(tsunoda)
model.db.session.commit()

zhou = Driver.query.filter_by(driver_id = "855").first()
zhou.img_url = '/static/imgs/drivers/Guanyu.jpeg'
zhou.active = True
model.db.session.add(zhou)
model.db.session.commit()

albon = Driver.query.filter_by(driver_id = "848").first()
albon.img_url = '/static/imgs/drivers/Albon.jpeg'
albon.active = True
model.db.session.add(albon)
model.db.session.commit()

latifi = Driver.query.filter_by(driver_id = "849").first()
latifi.img_url = '/static/imgs/drivers/Latifi.jpeg'
latifi.active = True
model.db.session.add(latifi)
model.db.session.commit()










#Update the photos for the constructors that are active 
haas = Constructor.query.filter_by(constructor_id = "210").first()
haas.img = '/static/imgs/Haas_F1_Team_logo.png'
model.db.session.add(haas)
model.db.session.commit()

ferrari = Constructor.query.filter_by(constructor_id = "6").first()
ferrari.img = '/static/imgs/Scuderia_Ferrari_Logo.svg'
model.db.session.add(ferrari)
model.db.session.commit()

aston_martin = Constructor.query.filter_by(constructor_id = "117").first()
aston_martin.img = '/static/imgs/Aston_Martin_Aramco_Cognizant_F1_Team.jpg'
model.db.session.add(aston_martin)
model.db.session.commit()

alpine = Constructor.query.filter_by(constructor_id = "214").first()
alpine.img = '/static/imgs/Alpine_F1_Team_Logo.svg'
model.db.session.add(alpine)
model.db.session.commit()

alpha_tauri = Constructor.query.filter_by(constructor_id = "213").first()
alpha_tauri.img = '/static/imgs/Scuderia_Alpha-Tauri.svg'
model.db.session.add(alpha_tauri)
model.db.session.commit()

red_bull = Constructor.query.filter_by(constructor_id = "9").first()
red_bull.img = '/static/imgs/RedBull.svg'
model.db.session.add(red_bull)
model.db.session.commit()

williams = Constructor.query.filter_by(constructor_id = "3").first()
williams.img = '/static/imgs/Williams_Racing_2020_logo.png'
model.db.session.add(williams)
model.db.session.commit()

mclaren = Constructor.query.filter_by(constructor_id = "1").first()
mclaren.img = '/static/imgs/McLaren_Racing_logo.svg'
model.db.session.add(mclaren)
model.db.session.commit()

alfa_romeo = Constructor.query.filter_by(constructor_id = "51").first()
alfa_romeo.img = '/static/imgs/Alfa_Romeo_F1_Team_ORLEN_logo.svg'
model.db.session.add(alfa_romeo)
model.db.session.commit()

mercedes = Constructor.query.filter_by(constructor_id = "131").first()
mercedes.img = '/static/imgs/Mercedes-Benz_in_Formula_One_logo.svg'
model.db.session.add(mercedes)
model.db.session.commit()


