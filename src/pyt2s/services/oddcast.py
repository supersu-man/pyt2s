import requests as __requests__
from enum import Enum as __enum__
from ..voices.oddcast import Voice

__url1__ = 'https://cache-a.oddcast.com/tts/genB.php'

def requestTTS(text: str, voice = Voice.Julie_US):
    engineId, languageId, voiceId = voice.value.split('-')
    params = {
        'EID': int(engineId),
        'LID': int(languageId),
        'VID': int(voiceId),
        'TXT': text,
        'EXT': 'mp3',
        'FNAME': '',
        'ACC': 15679,
        'SceneID': 2703396,
        'HTTP_ERR': '',
        'cache_flag': 3
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'Sec-Gpc': '1',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Brave";v="126"',
        'Referer': 'https://www.oddcast.com/',
        'Priority': 'u=1, i',
        'Origin': 'https://www.oddcast.com'
    }
    res = __requests__.get(__url1__, params=params, headers=headers)
    return res.content