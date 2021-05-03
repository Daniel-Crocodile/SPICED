"""
Berlin public transport API

documentation: https://v5.vbb.transport.rest/
"""

import requests
from pprint import pprint

BASE_URL = 'https://v5.vbb.transport.rest'

# find a station
name = 'kaisereiche'
url = f"{BASE_URL}/locations?poi=false&addresses=false&query={name}"
j = requests.get(url).json()
print(j)
closest_match = j[0]

pprint(closest_match['name'] + ' has id: ' + str(closest_match['id']))

# look up departures
print('\nNext connections from Kaisereiche:\n')

station_id = '900061104'
mins = 10

url = f'{BASE_URL}/stops/{station_id}/departures?duration={mins}'

j = requests.get(url).json()
for e in j:
    print(e['plannedWhen'][11:-9], '  ', e['line']['name'], e['direction'])
