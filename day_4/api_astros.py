from pprint import pprint
from typing import List

from pydantic import BaseModel

import requests

# pip install requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
print(response)  # <Response [200]>
# 2xx ok
# 3xx warningi, przekierowanie
# 4xx 404 - brak strony, 400 Bad request - błąd w zapytaniu
# 5xx błędy serwera 500 Internal Server Error
# https://pl.wikipedia.org/wiki/Kod_odpowiedzi_HTTP
print(response.text)
# {"people": [{"craft": "ISS", "name": "Oleg Kononenko"}, {"craft": "ISS", "name": "Nikolai Chub"},
#             {"craft": "ISS", "name": "Tracy Caldwell Dyson"}, {"craft": "ISS", "name": "Matthew Dominick"},
#             {"craft": "ISS", "name": "Michael Barratt"}, {"craft": "ISS", "name": "Jeanette Epps"},
#             {"craft": "ISS", "name": "Alexander Grebenkin"}, {"craft": "ISS", "name": "Butch Wilmore"},
#             {"craft": "ISS", "name": "Sunita Williams"}, {"craft": "Tiangong", "name": "Li Guangsu"},
#             {"craft": "Tiangong", "name": "Li Cong"}, {"craft": "Tiangong", "name": "Ye Guangfu"}], "number": 12,
#  "message": "success"}

response_data = response.json()
print(response_data)
# {'people': [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'},
#             {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'},
#             {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'},
#             {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'},
#             {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#             {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}],
#  'number': 12,
#  'message': 'success'}
print(type(response_data))  # <class 'dict'>
print(response_data.keys())
# dict_keys(['people', 'number', 'message'])
for i in response_data:
    print(i, response_data[i])

# people[{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'}, {'craft': 'ISS',
#                                                                                               'name': 'Tracy Caldwell Dyson'}, {
#     'craft': 'ISS', 'name': 'Matthew Dominick'}, {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS',
#                                                                                                'name': 'Jeanette Epps'}, {
#     'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'}, {'craft': 'ISS',
#                                                                                                 'name': 'Sunita Williams'}, {
#     'craft': 'Tiangong', 'name': 'Li Guangsu'}, {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong',
#                                                                                            'name': 'Ye Guangfu'}]
# number 12
# message
# success

print(response_data['people'][0]['name'])  # Oleg Kononenko


class Astronaut(BaseModel):
    name: str
    craft: str


class AstroData(BaseModel):
    message: str
    people: List[Astronaut]
    number: int

data = AstroData(**response.json())
print(data)

for astronaut in data.people:
    print(f"Name: {astronaut.name}")

# Name: Oleg Kononenko
# Name: Nikolai Chub
# Name: Tracy Caldwell Dyson
# Name: Matthew Dominick
# Name: Michael Barratt
# Name: Jeanette Epps
# Name: Alexander Grebenkin
# Name: Butch Wilmore
# Name: Sunita Williams
# Name: Li Guangsu
# Name: Li Cong
# Name: Ye Guangfu