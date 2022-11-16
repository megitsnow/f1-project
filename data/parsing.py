
raw_data = open("sprint_results.txt")

sprint_results = {}

for line in raw_data:
    line = line.rstrip().replace('"', '')
    result_id, race_id, driver_id, constructor_id ,number, grid, position, position_text, position_order, points, laps, time, milliseconds, fastest_lap, fastest_lap_time, status_id = line.split(",")
    sprint_results[result_id] = {"result_id": result_id, "race_id": race_id, "driver_id": driver_id, "constructor_id": constructor_id ,"number": number, "grid": grid, "position": position, "position_text": position_text, "position_order": position_order, "points": points,"laps": laps, "time": time, "milliseconds": milliseconds, "fastest_lap": fastest_lap, "fastest_lap_time": fastest_lap_time, "status_id": status_id}

    
print(sprint_results)

