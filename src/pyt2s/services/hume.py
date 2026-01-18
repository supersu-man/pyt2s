import json as __json__
import requests as __requests__
from ..voices.hume import Voice

__session__ = __requests__.session()

__url1__ = 'https://www.hume.ai/api/access-token'

__headers1__ = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1"
}

__url2__ = 'https://api.hume.ai/v0/tts/stream/json?access_token={access_token}'
__headers2__ = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "content-type": "application/json",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1"
}

__url3__ = 'https://api.hume.ai/v0/tts/tts_records/{generation_id}/audio?access_token={access_token}'
__headers3__ = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1"
}

def requestTTS(text: str, voice = Voice.TikTok_Fashion_Influencer):
    response1 = __session__.get(__url1__, headers=__headers1__)
    json1 = response1.json()
    
    response2 = __session__.post(__url2__.format(access_token=json1), headers=__headers2__, data=__json__.dumps({
        "no_binary": True,
        "utterances": [{
            "text": text,
            "voice": {
                "id": voice.value,
                "provider": "HUME_AI"
            }
        }],
        "num_generations": 1,
        "format": {
            "type": "mp3"
        },
        "instant_mode": True,
        "version": "1"
    }))
    first = response2.text.split("\n")[0]
    json2 = __json__.loads(first)
    generation_id = json2['generation_id']
    response3 = __session__.get(__url3__.format(generation_id=generation_id, access_token=json1), headers=__headers3__)
    response4 = __session__.get(response3.json()['signed_audio_uri'])
    return response4.content