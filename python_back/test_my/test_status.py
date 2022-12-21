import requests

def test_statusCode():
    response = requests.get('https://pokemonbattle.me:5000/trainers')
    assert response.status_code == 200    

def test_trainerName():
    response1 = requests.get('https://pokemonbattle.me:5000/trainers', params= {'trainer_id' : '1240'})
    assert response1.json()['trainer_name'] == 'Tolik'       