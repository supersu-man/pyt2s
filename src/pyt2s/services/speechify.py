import json as __json__
import requests as __requests__
from ..voices.speechify import Voice, Tone

__session__ = __requests__.session()

__url__ = "https://voiceover-demo-server--us-central1-5hlswwmzra-uc.a.run.app/tts/stream"

__headers__ = {
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
    "sec-fetch-site": "cross-site",
    "sec-gpc": "1",
    "referer": "https://speechify.com/",
}

def requestTTS(text: str, voice = Voice.Maggie, tone = Tone.Story_Telling):
    payload = {
        "text": text,
        "voiceId": voice.value,
        "prompt": tone.value
    }
    response = __session__.post(__url__, headers=__headers__, json=payload)
    return response.content
