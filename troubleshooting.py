from parsed_data import circuits 
import crud

circuit_in_db = []

for i in circuits.keys():
    circuit_id,circuit_ref,name,location,country,lat,lng,alt,url = (
        i,
        circuits[i]["circuit_ref"],
        circuits[i]["name"],
        circuits[i]["location"],
        circuits[i]["country"],
        circuits[i]["lat"],
        circuits[i]["lng"],
        circuits[i]["alt"],
        circuits[i]["url"],
    )
    db_circuit = crud.create_circuit(circuit_id,circuit_ref,name,location,country,lat,lng,alt,url)
    circuit_in_db.append(db_circuit)

print(circuit_in_db)


        

