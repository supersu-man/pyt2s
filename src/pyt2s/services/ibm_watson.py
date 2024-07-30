import requests as __requests__
import uuid as __uuid__

from src.pyt2s.models.ibm_watson_models import IbmWatsonVoice
from src.pyt2s.services.BaseService import BaseService

__session__ = __requests__.session()
__url1__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/session'   
__url2__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/store'   
__url3__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/newSynthesizer'

__headers__ = {
    'Origin': 'https://www.ibm.com',
    'Referer': 'https://www.ibm.com/demos/live/tts-demo/self-service/home',
    'Accept': 'application/json, text/plain, */*',
}


class IbmWatson(BaseService):
    voice_service: IbmWatsonVoice = IbmWatsonVoice

    def requestTTS(self, text: str, voice: voice_service = voice_service.en_GB_CharlotteV3Voice):
        __session__.post(__url1__, headers=__headers__)
        id = str(__uuid__.uuid4())
        jsonPayload = {"ssmlText": f"<prosody pitch=\"0%\" rate=\"-0%\">{text}</prosody>", "sessionID": id}
        __session__.post(__url2__, data=jsonPayload, headers=__headers__)
        res = __session__.get(__url3__, params={'voice' : voice.value,'id': id})
        return res.content
