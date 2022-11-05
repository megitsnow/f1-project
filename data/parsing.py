
# constructors_txt = open('constructors.txt')

# constructors = {}

# for line in constructors_txt:
#     line = line.rstrip().replace('"', '')
#     constructorId, constructorRef, name, nationality, url  = line.split(",")
#     constructors[constructorId] = {"constructorRef": constructorRef, 
#     "name": name, "nationality": nationality, "url": url}


# print(constructors)

# constructors_txt = open('status.txt')

# status = {}

# for line in constructors_txt:
#     line = line.rstrip().replace('"', '')
#     statusId, status_desc  = line.split(",")
#     status[statusId] = {"status": status_desc}


# print(status)

# constructors_txt = open('sprint_results.txt')

# sprint_results = {}

# for line in constructors_txt:
#     line = line.rstrip().replace('"', '')
#     result_id,race_id,driver_id,constructor_id,number,grid, position,position_text,position_order,points,laps,time,milliseconds, fastest_lap,fastest_lap_time,status_id  = line.split(",")
#     sprint_results[result_id] = {"race_id": race_id, "constructor_id": constructor_id, "number": number, "grid": grid, "position": position, "position_text": position_text, "position_order": position_order, "points": points, "laps": laps, "time": time,"milliseconds":milliseconds, "fastest_lap": fastest_lap,"fastest_lap_time": fastest_lap_time,"status_id": status_id}


# print(sprint_results)

# raw_data = open('results.txt')

# results = {}

# for line in raw_data:
#     line = line.rstrip().replace('"', '')
#     result_id,race_id,driver_id,constructor_id,number,grid,position,position_text,position_order,points,laps,time,milliseconds,fastest_lap,rank,fastest_lap_time,fastest_lap_speed,status_id  = line.split(",")
#     results[result_id] = {"race_id": race_id, "driver_id": driver_id,"constructor_id": constructor_id,"number": number,"grid": grid,"position": position,"position_text": position_text,"position_order": position_order,"points": points, "laps": laps,"time": time,"milliseconds": milliseconds,"fastest_lap": fastest_lap,"rank": rank,"fastest_lap_time": fastest_lap_time, "fastest_lap_speed": fastest_lap_speed,"status_id": status_id}


# print(results)

# raw_data = open('races.txt')

# races = {}

# for line in raw_data:
#     line = line.rstrip().replace('"', '')
#     raceId,year,round,circuit_id,name,date,time,url,fp1_date,fp1_time,fp2_date,fp2_time,fp3_date,fp3_time,quali_date,quali_time,sprint_date,sprint_time  = line.split(",")
#     races[raceId] = {"year":year,"round":round,"circuit_id": circuit_id,"name": name,"date": date,"time": time,"url": url,"fp1_date": fp1_date,"fp1_time": fp1_time,"fp2_date": fp2_date,"fp2_time": fp2_time,"fp3_date": fp3_date,"fp3_time": fp3_time,"quali_date": quali_date,"quali_time": quali_time,"sprint_date": sprint_date,"sprint_time": sprint_time}


# print(races)



# constructors_txt = open('results.txt')

# results = {}

# for line in constructors_txt:
#     line = line.rstrip().replace('"', '')
#     result_id,race_id,driver_id,constructor_id,number,grid,position,position_text,position_order,points,laps,time,milliseconds,fastest_lap,rank,fastest_lap_time,fastest_lap_speed,status_id  = line.split(",")
#     results[result_id] = {"race_id": race_id,"driver_id": driver_id,"constructor_id": constructor_id,"number": number,"grid": grid,"position": position,"position_text": position_text,"position_order": position_order,"points": points,"laps": laps,"time": time,"milliseconds": milliseconds,"fastest_lap": fastest_lap, "rank": rank,"fastest_lap_time": fastest_lap_time,"fastest_lap_speed": fastest_lap_speed,"status_id": status_id}


# print(results)


# raw_data = open('qualifying.txt')

# qualifying = {}

# for line in raw_data:
#     line = line.rstrip().replace('"', '')
#     qualify_id,race_id,driver_id,constructor_id,number,position,q1,q2,q3  = line.split(",")
#     qualifying[qualify_id] = {"qualify_id": qualify_id,"race_id": race_id,"driver_id": driver_id,"constructor_id": constructor_id,"number": number,"position": position,"q1": q1,"q2": q2,"q3": q3}


# print(qualifying)

raw_data = open('qualifying.txt')

qualifying = {}

for line in raw_data:
    line = line.rstrip().replace('"', '')
    qualify_id,race_id,driver_id,constructor_id,number,position,q1,q2,q3  = line.split(",")
    qualifying[qualify_id] = {"qualify_id": qualify_id,"race_id": race_id,"driver_id": driver_id,"constructor_id": constructor_id,"number": number,"position": position,"q1": q1,"q2": q2,"q3": q3}


print(qualifying)

