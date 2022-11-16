from parsed_data import driver_data, races, constructor_data, results, sprint_results, status
import crud

status_in_db = []

for key,value in status.items():
    status_id, status = (
        key,
        value['status']
    )
    
    db_status = crud.create_status(status_id, status)
    status_in_db.append(db_status)

print(status_in_db)



