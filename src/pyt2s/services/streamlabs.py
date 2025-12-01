import requests as __requests__
from enum import Enum as __enum__
from ..voices.stream_labs import Voice

__url1__ = 'https://streamlabs.com/polly/speak'

__headers__ = {
    'Referer': 'https://streamlabs.com'
}
    
def requestTTS(text: str, voice = Voice.Brian):
    params = {
        'voice': voice.value,
        'text': text
    }
    res = __requests__.post(__url1__, params=params, headers=__headers__)
    mp3_url = res.json()['speak_url']
    res = __requests__.get(mp3_url)
    return res.content