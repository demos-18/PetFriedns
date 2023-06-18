from api import PetFriends
from src.pydantic_schemas.schemas import Key, PetSolo, PetInList
from src.response_handler.reponse_handler import ResponseHandler
from src.parameters.pet_enums import PositiveAge, PositiveNames, PositiveAnimalType
from src.parameters.user_enum import PositiveEmails, PositivePasswords, PositiveFilter
import pytest

pf = PetFriends()


class TestPositivePetFriends:

    @pytest.mark.parametrize("email", PositiveEmails.list())
    @pytest.mark.parametrize("password", PositivePasswords.list())
    def test_get_api_key(self, email, password):
        """В этом тесте проверяем возможность получения api-ключа c корректными данными."""
        res = pf.get_api_key(email, password)
        response = ResponseHandler(res)

        response.assert_status_code(200).validate_pydantic(Key)

    @pytest.mark.parametrize("fillter", PositiveFilter.list())
    def test_get_list_of_pets(self, get_api_key, fillter):
        """В этом тесте проверяем возможность получения списка питомцев с кореектными данными."""
        res = pf.get_list_of_pets(get_api_key, fillter)
        response = ResponseHandler(res)

        response.assert_status_code(200).validate_pydantic(PetInList)

    @pytest.mark.parametrize("name", PositiveNames.list())
    @pytest.mark.parametrize("animal_type", PositiveAnimalType.list())
    @pytest.mark.parametrize("age", PositiveAge.list())
    def test_add_new_pet(self, get_api_key, name, animal_type, age, pet_photo):
        """В этом тесте провряем возможность создания нового питомца с корректными данными."""
        res = pf.add_new_pet(get_api_key, name, animal_type, age, pet_photo)
        response = ResponseHandler(res)

        response.assert_status_code(200).validate_pydantic(PetSolo)
        assert response.parsed_obj("name") == name
        assert response.parsed_obj("animal_type") == animal_type
        assert response.parsed_obj("age") == str(age)

    def test_delete_pet(self, get_api_key, get_pet_id):
        """В этом тесте проверяем возможность удаления питомца с корректными данными."""
        res = pf.delete_pet(get_api_key, get_pet_id)
        response = ResponseHandler(res)

        response.assert_status_code(200)

    @pytest.mark.parametrize("name", PositiveNames.list())
    @pytest.mark.parametrize("animal_type", PositiveAnimalType.list())
    @pytest.mark.parametrize("age", PositiveAge.list())
    def test_update_pet(self, get_api_key, get_pet_id, name, animal_type, age):
        """В этом тесте проверяем возможность обновления данных питомца с корректными данными."""
        update = pf.update_pet(get_api_key, get_pet_id, name, animal_type, age)
        update = ResponseHandler(update)

        update.assert_status_code(200).validate_pydantic(PetSolo)
        assert update.parsed_obj("name") == name
        assert update.parsed_obj("animal_type") == animal_type
        assert update.parsed_obj("age") == str(age)

    @pytest.mark.parametrize("name", PositiveNames.list())
    @pytest.mark.parametrize("animal_type", PositiveAnimalType.list())
    @pytest.mark.parametrize("age", PositiveAge.list())
    def test_add_new_pet_without_photo(self, get_api_key, name, animal_type, age):
        """В этом тесте проверяем возможность добавления нового питомца без фотографии с корректными данными."""
        res = pf.add_new_pet_without_photo(get_api_key, name, animal_type, age)
        response = ResponseHandler(res)

        response.assert_status_code(200).validate_pydantic(PetSolo)
        assert response.parsed_obj("name") == name
        assert response.parsed_obj("animal_type") == animal_type
        assert response.parsed_obj("age") == str(age)

    def test_add_photo_of_pet(self, get_api_key, pet_photo, get_pet_id):
        """В этом тесте проверяем возможноть добавлении фотографии, к уже созданному питомцу с корректными данными."""
        res = pf.add_photo_of_pet(get_api_key, get_pet_id, pet_photo)
        response = ResponseHandler(res)

        response.assert_status_code(200).validate_pydantic(PetSolo)









