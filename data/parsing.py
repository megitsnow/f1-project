
raw_data = open("circuits.txt")


circuits = {}

for line in raw_data:
    line = line.rstrip().replace('"', '')
    circuit_id,circuit_ref,name,location,country,lat,lng,alt,url= line.split(",")
    circuits[circuit_id] = {"circuit_ref": circuit_ref,"name": name,"location": location, "country": country,"lat": lat,"lng": lng,"alt": alt,"url": url}

    
print(circuits)
