import requests

URL = 'https://api.pokemonbattle.ru' 
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : '27ec998cda3ecae2f0086e4d89d3ce1f'} 

Body_Create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
response_create = requests.post (url = f'{URL}/v2/pokemons', headers = HEADER, json = Body_Create)
message_create = response_create.json()
print (message_create)

Body_Update = {
    "pokemon_id": "311113",
    "name": "NewName",
    "photo_id": 1
}

response_update = requests.put (url = f'{URL}/v2/pokemons', headers = HEADER, json = Body_Update)
message_update = response_update.json()
print (message_update)

Body_Catch = {
    "pokemon_id": "311113"
}

response_catch = requests.post (url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = Body_Catch)
message_catch = response_catch.json()
print (message_catch)