import requests
from pprint import pprint


# response = requests.get('https://swapi.py4e.com/api/starships/9/')
# response = response.json()
# # Напечатаем в терминале содержимое ответа сервера...
# pprint(response)

# print(response.get('name'))
# # А если запросить несуществующий ключ словаря?
# print(response.get('new_name'))


response = requests.get('https://swapi.py4e.com/api/people')
response = response.json()
# pprint(response)

for person in response['results'][:10]:
    print(f"Name: {person['name']}")
    print(f"Height: {person['height']}")
    print(f"Mass: {person['mass']}")
    print(f"Hair Color: {person['hair_color']}")
    print(f"Skin Color: {person['skin_color']}")
    print(f"Eye Color: {person['eye_color']}")
    print(f"Birth Year: {person['birth_year']}")
    print(f"Gender: {person['gender']}")
    print("-" * 40)

response = requests.get('https://swapi.py4e.com/api/people/1')
response = response.json()
pprint(response)

response = requests.get('https://swapi.py4e.com/api/planets/1/')
response = response.json()
pprint(response['diameter'])