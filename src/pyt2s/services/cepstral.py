import requests as __requests__
import time as __time__
from enum import Enum as __enum__
from ..voices.cepstral import Voice

__session__ = __requests__.session()

__url1__ = 'https://www.cepstral.com/en/demos'
__url2__ = 'https://www.cepstral.com/demos/createAudio.php?'
    
def requestTTS(text: str, voice = Voice.Belle):
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