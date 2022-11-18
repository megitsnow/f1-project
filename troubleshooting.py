from parsed_data import driver_data, races, constructor_data, results, sprint_results, status
import crud

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

print(result_in_db)



