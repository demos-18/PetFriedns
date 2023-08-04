import json

import requests

data ={
    "animal_type" : "",
    "age" : ""
}
headers ={
    "auth_key" : "e8315846932119d7103fe13c43acb3de44d7c71da2d9c451246021c9"
}
add_pet = requests.post(f'https://petfriends.skillfactory.ru/api/create_pet_simple', headers=headers, data=json.dumps(data))
print(add_pet.status_code)
print(add_pet.headers)
print(add_pet.text)

