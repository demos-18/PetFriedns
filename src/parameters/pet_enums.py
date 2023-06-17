from src.parameters.parameter_enum import ParEnum
from src.generators.string_generalor import string_generator


class NegativeNames(ParEnum):
    NUMBER = 45
    TWO_FIVE_FIVE_STRING = string_generator(255)
    ONE_ZERO_ZERO_ONE_STRING = string_generator(1001)
    BLANK_LINE = ""
    SPECIAL_CHARACTERS = "@#$%^&*()[]{}<>\|/"
    CHINESE = "假借字假借字"


class PositiveNames(ParEnum):
    POSITIVE_NAME = "Рексик"


class NegativeAnimalType(ParEnum):
    NUMBER = 65
    TWO_FIVE_FIVE_STRING = string_generator(255)
    ONE_ZERO_ZERO_ONE_STRING = string_generator(1001)
    BLANK_LINE = ""
    SPECIAL_CHARACTERS = "@#$%^&*()[]{}<>\|/"
    CHINESE = "假借字假借字"


class PositiveAnimalType(ParEnum):
    ANIMAL_TYPE = "Кошка"


class NegativeAge(ParEnum):
    STRING = "7"
    NEGATIVE = -9
    LARGE = 98765
    SPECIAL_CHARACTERS = "@#$%^&*()_[]{}\|/<>"
    BLANK_LINE = ""


class PositiveAge(ParEnum):
    POSITIVE_AGE = 7


class NegativePetPhoto(ParEnum):
    TEXT_FILE = "images/drot.txt"
    BLANK_LINE = ""


class NegativePetId(ParEnum):
    BLANK_LINE = ""
    LONG_ID = "98876543216871354"
    STRING = "хтонь"












