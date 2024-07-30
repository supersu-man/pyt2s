import requests as __requests__

from src.pyt2s.models.voice_forge_models import VoiceForgeVoice
from src.pyt2s.services.BaseService import BaseService

__url1__ = 'https://api.voiceforge.com/swift_engine?'

__headers__ = {
    'HTTP_X_API_KEY': '8b3f76a8539',
}


class VoiceForge(BaseService):
    voice_service: VoiceForgeVoice = VoiceForgeVoice

    def requestTTS(self, text: str, voice: voice_service = voice_service.Conrad):
        params = {
            'voice': voice.value,
            'msg': text,
            'email': 'null',
        }
        res = __requests__.get(__url1__, params=params, headers=__headers__)
        return res.content
