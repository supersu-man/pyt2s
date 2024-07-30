import requests as __requests__

from src.pyt2s.models.streamlabs_models import StreamlabsVoice
from src.pyt2s.services.BaseService import BaseService

__url1__ = 'https://streamlabs.com/polly/speak'

__headers__ = {
    'Referer': 'https://streamlabs.com'
}


class Streamlabs(BaseService):
    voice_service: StreamlabsVoice = StreamlabsVoice

    def requestTTS(self, text: str, voice: voice_service = voice_service.Brian):
        params = {
            'voice': voice.value,
            'text': text
        }
        res = __requests__.post(__url1__, params=params, headers=__headers__)
        mp3_url = res.json()['speak_url']
        res = __requests__.get(mp3_url)
        return res.content
