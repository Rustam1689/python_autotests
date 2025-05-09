import requests
import pytest

URL = 'https://api.pokemonbattle.ru' 
HEADER = {'Content-Type' : 'application/json',
          'trainer_token' : '27ec998cda3ecae2f0086e4d89d3ce1f'} 

def test_status_code():
    response = requests.get (url = f'{URL}/v2/pokemons', params = {'trainer_id': '34060'})
    assert response.status_code == 200

def test_pokemon_name():
    response = requests.get (url = f'{URL}/v2/pokemons', params = {'trainer_id': '34060'})
    assert response.json()['data'][0]['name'] == 'Бульбазавр'
    