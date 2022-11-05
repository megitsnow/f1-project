import requests
import json

response = requests.get('http://ergast.com/api/f1/2010/2/constructors')
data = response.json()
print(data)