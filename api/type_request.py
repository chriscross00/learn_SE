import requests
import json

parameters = {'lat': 37.78, 'lon': -122.41}
response = requests.get('http://api.open-notify.org/iss-pass.json',
                        params=parameters)
data = response.json()
print(type(data))
print(data)
