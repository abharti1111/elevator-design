
from enum import Enum, IntEnum


class ExtendedEnum(Enum):

    @classmethod
    def list(cls, name=False):
        if name:
            return list(map(lambda c: c.name, cls))
        return list(map(lambda c: c.value, cls))

    @classmethod
    def dict(cls, reverse=False):
        if reverse is False:
            d = cls._member_map_
        else:
            d = cls._value2member_map_
        return d


class ExtendedIntEnum(IntEnum):

    @classmethod
    def list(cls, name=False):
        if name:
            return list(map(lambda c: c.name, cls))
        return list(map(lambda c: c.value, cls))

    @classmethod
    def dict(cls, reverse=False):
        if reverse is False:
            d = cls._member_map_
        else:
            d = cls._value2member_map_
        return d

