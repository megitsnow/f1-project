from parsed_data import races
import crud

print(races.items())

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

print(races_in_db)
