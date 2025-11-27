import json as __json__
import requests as __requests__
from enum import Enum as __enum__
from ..voices.acapela import Voice

__session__ = __requests__.session()
__url1__ = 'https://www.acapela-group.com/wp-json/acapela/v1/get_accldcfg'
__headers1__ = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": '"Chromium";v="142", "Brave";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "referer": "https://www.acapela-group.com/demos/"
}
__url2__ = 'https://www.acapela-cloud.com/api/command/'
__headers2__ = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": '"Chromium";v="142", "Brave";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-gpc": "1",
    "referer": "https://www.acapela-group.com/"
}

def requestTTS(text: str, voice = Voice.Lily22k_HQ):
    res = __session__.get(__url1__, headers=__headers1__)
    token = res.json()['token']
    params = { 'voice': voice.value, 'text': text, 'output': 'stream', 'type': 'mp3', 'samplerate': '22050', 'token': token }
    res = __session__.get(__url2__, headers=__headers2__, params=params)
    return res.content