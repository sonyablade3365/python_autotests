import requests
import json

token = '44810b093c469484282e40c4cb252c03'
response = requests.post('https://pokemonbattle.me:5000/pokemons',headers={'trainer_token' : token}, json = {
    "name": "Алёша",
    "photo": "https://static.wikia.nocookie.net/pokemon/images/2/21/001Bulbasaur.png"
})

print(response.text)

response = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token' : token}, json = {
    "pokemon_id": 1480,
    "name": "Игнат",
    "photo": ""
})

print(response.text)

response = requests.post('https://pokemonbattle.me:5000/trainers/addPokebol', headers={'trainer_token' : token}, json = {
    "pokemon_id": "1480"
})

print(response.text)
