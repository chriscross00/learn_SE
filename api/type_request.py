import requests

parameters = {'lat': 40.71, 'lon': -74}
response = requests.get('http://api.open-notify.org/iss-pass.json',
                        params=parameters)
print(response.content)
