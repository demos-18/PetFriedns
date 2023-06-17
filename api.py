import json

import requests


def loger(func):
    def wrapper(*args, **kwargs):
        status, result, headers, path_str, body, url, path = func(*args, **kwargs)
        print('Headers: 'f'{headers!r}')
        print('Path: 'f'{path!r}')
        print('Url: 'f'{url!r}')
        print('Body: 'f'{body!r}')
        return func(*args, **kwargs)
    return wrapper


class PetFriends:
    """API библиотека к веб-приложению PetFriends"""

    def __init__(self):
        self.base_url = f'https://petfriends.skillfactory.ru/'

    def get_api_key(self, email: str, password: str) -> json:
        """"Метод делает запрос к API сервера и возвращает статус запроса и результат
        в формате JSON, с уникальным ключём пользователя, найденным по указанным email и
        password."""

        headers = {
            'email': email,
            'password': password,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)

        return res

    def get_list_of_pets(self, auth_key: json, fillter: str = '') -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и рузультат в JSON формате
        со списком найденных питомцов, совпадающих с фильтром. На данный момент фильтр может иметь
        либо пустое значение - получить список всех питомцев, либо "my_pets" - получить список собственных питомцев."""

        headers = {
            'auth_key': auth_key['key'],
        }
        fillter = {
            'fillter': fillter,
        }

        res = requests.get(self.base_url+'api/pets', headers=headers, params=fillter)

        return res

    def add_new_pet(self, auth_key: json, name: str, animal_type: str, age: int, pet_photo: str) -> json:
        """Метод отправляет данные на сервер, о добовляемом питомце и возвращает статус
        запроса на сервер и результат в JSON формате с данными добавленного питомца."""

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        headers = {
            'auth_key': auth_key['key'],
        }

        file = {
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg'),
        }

        res = requests.post(self.base_url+'api/pets', headers=headers, data=data, files=file)

        return res

    def delete_pet(self, authkey: json, pet_id: str) -> json:
        """Метод отправляет запрос на сервер на удаление питомца по указанному ID и возвращает
        статус запроса и результат в JSON формате с текстом уведомления о успешном удалении.
        Сейчас есть баг в result приходит пустая строка, но статус всегда = 200"""

        headers = {
            'auth_key': authkey['key'],
        }
        res = requests.delete(self.base_url+'api/pets/'+pet_id, headers=headers)

        return res

    def update_pet(self, auth_key: json, pet_id: str, name: str, animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер об обновлении данных питомца по указанному ID
        и возвращает статус запроса и result  в JSON формате с обновлёнными данными питомца."""

        headers = {
            'auth_key': auth_key['key'],
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }
        res = requests.put(self.base_url+'api/pets/'+pet_id, headers=headers, data=data)

        return res

    def add_new_pet_without_photo(self, auth_key: json, name: str, animal_type: str, age: int) -> json:
        """Метод отправляет запрос на сервер об созддании нового питомца по указанному api_key питомца
        и возвращает статус запроса в result в JSON формате с данными добавленного питомца."""
        headers = {
            'auth_key': auth_key['key'],
        }
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
        }

        res = requests.post(self.base_url+'api/create_pet_simple', headers=headers, data=data)

        return res

    def add_photo_of_pet(self, auth_key: json, pet_id: str, pet_photo: str) -> json:
        """Метод отправляет запрос на сервер по указанному api_key, к указанному pet_id питомцу,
        на добавление фотографии питомца. И возвращает статус запроса в result в JSON формате с данными
         питомца."""
        headers = {
            'accept': 'application/json',
            'auth_key': auth_key['key'],
        }
        file = {
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg'),
        }
        res = requests.post(self.base_url+'api/pets/set_photo/'+pet_id, headers=headers, files=file)

        return res
