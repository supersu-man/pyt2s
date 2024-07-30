import requests as __requests__
import time as __time__

from src.pyt2s.models.cepstral_models import CepstralVoice
from src.pyt2s.services.BaseService import BaseService

__session__ = __requests__.session()

__url1__ = 'https://www.cepstral.com/en/demos'
__url2__ = 'https://www.cepstral.com/demos/createAudio.php?'


class Cepstral(BaseService):
    voice_service: CepstralVoice = CepstralVoice

    def requestTTS(self, text: str, voice: voice_service = voice_service.Belle):
        params = {
            'voiceText': text,
            'voice': voice.value,
            'createTime': int(__time__.time() * 1000),
            'rate': 170,
            'pitch': 1,
            'sfx': 'none'
        }
        __session__.get(__url1__)
        res = __session__.get(__url2__, params=params)
        mp3_location = 'https://www.cepstral.com' + res.json()['mp3_loc']
        res = __session__.get(mp3_location)
        return res.content
