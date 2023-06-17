from enum import Enum


class ParEnum(Enum):

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))