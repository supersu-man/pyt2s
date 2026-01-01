import requests as __requests__
from ..voices.voice_forge import Voice

__url1__ = 'https://api.voiceforge.com/swift_engine?'

__headers__ = {
    'HTTP_X_API_KEY': '8b3f76a8539',
}

def requestTTS(text: str, voice = Voice.Conrad):
    params = {
        'voice': voice.value,
        'msg': text,
        'email': 'null',
    }
    res = __requests__.get(__url1__, params=params, headers=__headers__)
    return res.content