import json
import os.path
import pytest
import requests
from settings import valid_email, valid_password
from api import PetFriends

pf = PetFriends()


@pytest.fixture(scope="class", autouse=True)
def get_api_key(email=valid_email, password=valid_password):
    headers = {
        'accept': 'application/json',
        'email': email,
        'password': password,
    }
    res = requests.get(f'https://petfriends.skillfactory.ru/api/key', headers=headers)
    result = ''
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return result


@pytest.fixture(scope="function")
def get_pet_id(get_api_key, fillter="my_pets"):
    pf.add_new_pet_without_photo(get_api_key, name="Пушок", animal_type="Кошка", age=12)

    res = pf.get_list_of_pets(get_api_key, fillter)
    response = res.json()
    pet_id = response["pets"][0]["id"]

    yield pet_id

    pf.delete_pet(get_api_key, pet_id)


@pytest.fixture(scope="class", autouse=True)
def pet_photo(pet_photo='images\\kot2.jpg'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    return pet_photo


@pytest.fixture(scope="class", autouse=True)
def pet_wrong_photo(pet_photo='images/drot.txt'):
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    return pet_photo
