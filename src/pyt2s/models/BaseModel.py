from enum import Enum
from extendableenum import inheritable_enum


@inheritable_enum
class BaseVoiceModel(Enum):
    NONE = ''
