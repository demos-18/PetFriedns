from api import PetFriends
from src.response_handler.reponse_handler import ResponseHandler
from src.parameters.user_enum import NegativeEmails, NegativePasswords, AuthKeys, PositiveFilter, NegativeFilter
from src.parameters.pet_enums import NegativeNames, NegativeAnimalType, NegativeAge, NegativePetPhoto, NegativePetId
from src.parameters.pet_enums import PositiveNames, PositiveAnimalType, PositiveAge
import pytest

pf = PetFriends()


class TestNegativePetFriend:

    @pytest.mark.parametrize("email", NegativeEmails.list())
    @pytest.mark.parametrize("password", NegativePasswords.list())
    def test_get_api_key(self, email, password):
        """В этом тесте проверяем возможность получения api-ключа с некоррктными данными."""
        res = pf.get_api_key(email, password)
        response = ResponseHandler(res)

        response.assert_status_code(403)

    @pytest.mark.parametrize("auth_key", AuthKeys.list())
    @pytest.mark.parametrize("fillter", PositiveFilter.list())
    def test_get_list_of_pets_wrong_auth_key(self, auth_key, fillter):
        """В этом тесте проверяем возможность получения списка питомцев, используя некорректный api-ключ."""
        res = pf.get_list_of_pets(auth_key, fillter)
        response = ResponseHandler(res)

        response.assert_status_code(403)

    @pytest.mark.parametrize("auth_key", AuthKeys.list())
    @pytest.mark.parametrize("name", PositiveNames.list())
    @pytest.mark.parametrize("animal_type", PositiveAnimalType.list())
    @pytest.mark.parametrize("age", PositiveAge.list())
    def test_add_new_pet_wrong_auth_key(self, auth_key, name, animal_type, age, pet_photo):
        """В этом тесте проверяем возможность создания нового питомца, используя некорректный api-ключ."""
        res = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        response = ResponseHandler(res)

        response.assert_status_code(403)

    @pytest.mark.parametrize("auth_key", AuthKeys.list())
    def test_delete_pet_wrong_auth_key(self, get_api_key, get_pet_id, auth_key):
        """В этом тесте проверяем возможность удаления питомца, используя некорректный api-ключ."""
        res = pf.delete_pet(auth_key, get_pet_id)
        response = ResponseHandler(res)

        response.assert_status_code(403)

    @pytest.mark.parametrize("auth_key", AuthKeys.list())
    @pytest.mark.parametrize("name", PositiveNames.list())
    @pytest.mark.parametrize("animal_type", PositiveAnimalType.list())
    @pytest.mark.parametrize("age", PositiveAge.list())
    def test_update_pet_wrong_auth_key(self, get_api_key, get_pet_id, auth_key, name, animal_type, age):
        """В этом тесте проверяем возможность обновления данных питомца, используя некорректный api-ключ."""
        res = pf.update_pet(auth_key, get_pet_id, name, animal_type, age)
        response = ResponseHandler(res)

        response.assert_status_code(403)

    @pytest.mark.parametrize("auth_key", AuthKeys.list())
    @pytest.mark.parametrize("name", PositiveNames.list())
    @pytest.mark.parametrize("animal_type", PositiveAnimalType.list())
    @pytest.mark.parametrize("age", PositiveAge.list())
    def test_add_new_pet_without_photo_wrong_auth_key(self, auth_key, name, animal_type, age):
        """В этом тесте проверяем возможность добавления нового питомца, используя некорректный api-ключ."""
        res = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)
        response = ResponseHandler(res)

        response.assert_status_code(403)

    @pytest.mark.parametrize("auth_key", AuthKeys.list())
    def test_add_photo_of_pet_wrong_auth_key(self, get_api_key, auth_key, get_pet_id, pet_photo):
        """В этом тесте проверям возможность добавления к созданному питомцу, используя некорректный api-ключ."""
        res = pf.add_photo_of_pet(auth_key, get_pet_id, pet_photo)
        response = ResponseHandler(res)

        response.assert_status_code(403)

    @pytest.mark.parametrize("fillter", NegativeFilter.list())
    def test_get_list_of_pets(self, get_api_key, fillter):
        """В этом тесте проверяем возможность получения списка питомцев, используя некорректные значения фильтра."""
        res = pf.get_list_of_pets(get_api_key, fillter)
        response = ResponseHandler(res)

        response.assert_status_code(400)

    @pytest.mark.parametrize("name", NegativeNames.list())
    @pytest.mark.parametrize("animal_type", NegativeAnimalType.list())
    @pytest.mark.parametrize("age", NegativeAge.list())
    @pytest.mark.parametrize("pet_photo", NegativePetPhoto.list())
    def test_add_new_pet(self, get_api_key, name, animal_type, age, pet_photo):
        """В этом тесте проверяем возможность создания нового питомца, используя некорректные данные."""
        res = pf.add_new_pet(get_api_key, name, animal_type, age, pet_photo)
        response = ResponseHandler(res)

        response.assert_status_code(400)

    @pytest.mark.parametrize("pet_id", NegativePetId.list())
    def test_delete_pet(self, get_api_key, pet_id):
        """В этом тесте проверяем возможность удаления питомца, используя некорректное значение pet_id."""
        res = pf.delete_pet(get_api_key, pet_id)
        response = ResponseHandler(res)

        response.assert_status_code(400)

    @pytest.mark.parametrize("name", NegativeNames.list())
    @pytest.mark.parametrize("animal_type", NegativeAnimalType.list())
    @pytest.mark.parametrize("age", NegativeAge.list())
    def test_update_pet(self, get_api_key, pet_id, name, animal_type, age):
        """В этом тесте проверяем возможность обновления данных питомца, используя некорректные данные."""
        res = pf.update_pet(get_api_key, pet_id, name, animal_type, age)
        response = ResponseHandler(res)

        response.assert_status_code(400)

    @pytest.mark.parametrize("name", NegativeNames.list())
    @pytest.mark.parametrize("animal_type", NegativeAnimalType.list())
    @pytest.mark.parametrize("age", NegativeAge.list())
    def test_add_new_pet_without_photo(self, get_api_key, name, animal_type, age):
        """В этом тесте проверяем возможность создания нового питомца без фотографии, используя некорректные данные."""
        res = pf.add_new_pet_without_photo(get_api_key, name, animal_type, age)
        response = ResponseHandler(res)

        response.assert_status_code(400)

    @pytest.mark.parametrize("pet_id", NegativePetId.list())
    @pytest.mark.parametrize("pet_photo", NegativePetPhoto.list())
    def test_add_photo_of_pet(self, get_api_key, pet_id, pet_photo):
        """В этом тесте проверяем возможность добавления фотографии к созданному питомцу,
        используя неккорректные данные."""
        res = pf.add_photo_of_pet(get_api_key, pet_id, pet_photo)
        response = ResponseHandler(res)

        response.assert_status_code(400)

    @pytest.mark.parametrize("pet_photo", NegativePetPhoto.list())
    def test_add_photo_of_pet(self, get_api_key, get_pet_id, pet_photo):
        """В этом тесте проверяем возможность добавления фотографии к созданному питомцу,
        используя корректный pet_id и некорретные данные для фотографии."""
        res = pf.add_photo_of_pet(get_api_key, get_pet_id, pet_photo)
        response = ResponseHandler(res)

        response.assert_status_code(400)
