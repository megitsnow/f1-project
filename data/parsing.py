def parse_data(file, name):
    raw_data = open(file)

    name = {}

    for line in raw_data:
        line = line.rstrip().replace('"', '')
        driverStandings_id,race_id,driver_id,points,position,position_text,wins  = line.split(",")
        name[driverStandings_id] = {"race_id": race_id,"driver_id": driver_id,"points": points,"position": position,"position_text": position_text,"wins":wins}
    
    return name


print(parse_data('driver_standings.txt', "driver_standings"))

