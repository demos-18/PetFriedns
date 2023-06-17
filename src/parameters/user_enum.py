from src.parameters.parameter_enum import ParEnum
from src.generators.string_generalor import string_generator
from settings import valid_email, valid_password


class NegativeEmails(ParEnum):
    VALID_EMAIL = f"{valid_email}"
    INVALID_EMAIL = "ivan.dakl@789gmail.com"
    STRING = "plaintext"
    NUMBER = 78954
    BLANK_LINE = ""
    SPECIAL_CHARACTERS = "!@#$%^&*()_><{}[]"


class PositiveEmails(ParEnum):
    VALID_EMAIL = f"{valid_email}"


class NegativePasswords(ParEnum):
    BLANK_STRING = ""
    SPECIAL_CHARACTERS = "!@#$%^&*()_><{}[]"
    TWO_FIVE_FIVE_STRING = string_generator(255)
    ONE_ZERO_ZERO_ONE = string_generator(1001)


class PositivePasswords(ParEnum):
    PASSWORD = f"{valid_password}"


class AuthKeys(ParEnum):
    NUMBER = {"key": 143894}
    CHINESE = {"key": "假借字假借字"}
    RUSSIAN = {"key": "абвгдкот"}
    BLANK_LINE = {"key": ""}
    BROKEN_KEY = {"key": "e324337601ac3d3819562cccc8e95c313b1088d98a99fdc104ff837a"}
    SMALL_KEY = {"key": "e324337601ac3d3819562cccc8e95c313b1088d98a99fdc104f"}
    LONG_KEY = {"key": "e324337601ac3d3819562cccc8e95c313b1088d98a99fdc104ff833875d"}


class PositiveFilter(ParEnum):
    MY_PETS = "my_pets"
    ALL_PETS = ""


class NegativeFilter(ParEnum):
    TWO_FIVE_FIVE_STRING = string_generator(255)
    ONE_ZERO_ZERO_ONE_STRING = string_generator(1001)
    SPECIAL_CHARACTERS = "!@#$%^&*()_><{}[]"
    RUSSIAN = "Кошка"
    CHINESE = "假借字假借字"
    NUMBER = 2279
