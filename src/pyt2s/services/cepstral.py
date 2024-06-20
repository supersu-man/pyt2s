import requests as __requests__
import time as __time__
from enum import Enum as __enum__

class Voice(__enum__):
    Allison = 'Allison'
    Amy = 'Amy'
    Belle = 'Belle'
    Callie = 'Callie'
    Charlie = 'Charlie'
    Dallas = 'Dallas'
    Damien = 'Damien'
    David = 'David'
    Diane = 'Diane'
    Duchess = 'Duchess'
    Emily = 'Emily'
    Linda = 'Linda'
    Robin = 'Robin'
    Shouty = 'Shouty'
    Walter = 'Walter'
    William = 'William'
    Whispery = 'Whispery'
    Lawrence = 'Lawrence'
    Millie = 'Millie'
    Duncan = 'Duncan'
    Vittoria = 'Vittoria'
    Katrin = 'Katrin'
    Matthias = 'Matthias'
    Isabelle = 'Isabelle'
    Jean_Pierre = 'Jean-Pierre'
    Alejandra = 'Alejandra'
    Miguel = 'Miguel'

__session__ = __requests__.session()

__url1__ = 'https://www.cepstral.com/en/demos'
__url2__ = 'https://www.cepstral.com/demos/createAudio.php?'
    
def requestTTS(text: str, voice = 'Belle'):
    params = {
        'voiceText': text,
        'voice': voice,
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