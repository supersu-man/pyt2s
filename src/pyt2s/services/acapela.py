import json as __json__
from typing import Any

import requests as __requests__

from src.pyt2s.models.acapela_models import AcapelaVoice
from src.pyt2s.services.BaseService import BaseService

__session__ = __requests__.session()
__url1__ = 'https://www.acapela-group.com/www/static/website/demoOptionsDef_voicedemo.php'
__url2__ = 'https://h-ir-ssd-1.acapela-group.com/webservices/1-60-00/UrlMaker.json'
__headers__ = {
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Referer': 'https://www.acapela-group.com/demos/',
    'Origin': 'https://www.acapela-group.com/demos/',                             
}


class Acapela(BaseService):
    voice_service: AcapelaVoice = AcapelaVoice

    def requestTTS(self, text: str, voice: voice_service = voice_service.sharon22k):
        res = __session__.get(__url1__, headers=__headers__)
        json_res = res.text.replace('var vaasOptions = ', '').replace('};', '}')
        json_res = __json__.loads(json_res)
        params = {
            'cl_login': json_res['login'],
            'cl_app': json_res['app'],
            'session_start': json_res['session']['start'],
            'session_time': json_res['session']['time'],
            'session_key': json_res['session']['key'],
            'req_voice': voice.value,
            'req_text': text
        }
        res = __session__.post(__url2__, params=params, headers=__headers__)
        res = __session__.get(res.json()['snd_url'])
        return res.content
