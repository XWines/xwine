from sqlalchemy import Enum

DATA_KEY = 'data'
STATUS_KEY = 'status'
MESSAGE_KEY = 'message'
ERROR_KEY = 'error'
SOMETHING_WENT_WRONG = 'Something went wrong'
ERROR = 0
SUCCESS = 1


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


# items
class Items(ExtendedEnum):
    BLACK_DOG = 'BLACK_DOG'
    ROYAL_STAGE = 'ROYAL_STAG'
