import requests
import json

response = requests.get('http://api.open-notify.org/iss-now.json')

if response.status_code == 200:
    response_dict = json.loads(response.text)
    location = response_dict['iss_position']
    print(f"Current location:  {location['longitude']}, {location['latitude']}")
else:
    print('Request failed')