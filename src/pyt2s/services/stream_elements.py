import requests as __requests__

from src.pyt2s.models.stream_elements_models import StreamElementsVoice
from src.pyt2s.services.BaseService import BaseService

__url1__ = 'https://api.streamelements.com/kappa/v2/speech?'


class StreamElements(BaseService):
    voice_service: StreamElementsVoice = StreamElementsVoice

    def requestTTS(self, text: str, voice: voice_service = voice_service.Brian):
        params = {
            'voice': voice.value,
            'text': text
        }
        res = __requests__.get(__url1__, params)
        return res.content
