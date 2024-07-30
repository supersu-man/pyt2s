from typing import Type

from src.pyt2s.models.BaseModel import BaseVoiceModel
from src.pyt2s.services.BaseService import BaseService


def service_selector(voice_name: str) -> Type[BaseService]:
    subclasses = BaseService.__subclasses__()

    for subclass in subclasses:
        values = [e.value for e in subclass.voice_service]
        if voice_name in values:
            return subclass

    raise Exception("service could not found")


def print_list_voices():
    subclasses = BaseVoiceModel.__subclasses__()

    for subclass in subclasses:
        values = [e.value for e in subclass]
        print('-'*20, end='')
        print(subclass.__name__, end='')
        print('-'*20)

        print(values)


def list_voices():
    subclasses = BaseVoiceModel.__subclasses__()
    voice_list = []

    for subclass in subclasses:
        values = [e for e in subclass]
        voice_list.extend(values)

    return voice_list


def requestTTS(text: str, voice: BaseVoiceModel):
    service = service_selector(voice.value)
    return service.requestTTS(text, voice)
