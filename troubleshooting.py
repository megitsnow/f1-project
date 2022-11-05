from drivers import driver_data
import crud

driver_in_db = []

print(driver_data["1"]["driverRef"])

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

print(driver_in_db)
