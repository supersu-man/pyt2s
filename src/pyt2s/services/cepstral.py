import requests
import time
from ..service import Service

class Cepstral(Service):

    __validNames__ = [ 'Allison', 'Amy', 'Belle', 'Callie', 'Charlie', 'Dallas', 'Damien', 'David', 'Diane', 'Duchess', 'Emily', 'Linda', 'Robin', 'Shouty', 'Walter', 
        'William', 'Whispery', 'Lawrence', 'Millie', 'Duncan', 'Vittoria', 'Katrin', 'Matthias', 'Isabelle', 'Jean-Pierre', 'Alejandra', 'Miguel' ]

    __session__ = requests.session()

    __url1__ = 'https://www.cepstral.com/en/demos'
    __url2__ = 'https://www.cepstral.com/demos/createAudio.php?'
     
    def requestTTS(self, text: str, voice = 'Belle'):
        super().requestTTS(text, voice)
        params = {
            'voiceText': text,
            'voice': voice,
            'createTime': int(time.time() * 1000),
            'rate': 170,
            'pitch': 1,
            'sfx': 'none'
        }
        self.__session__.get(self.__url1__)
        res = self.__session__.get(self.__url2__, params=params)
        mp3_location = 'https://www.cepstral.com' + res.json()['mp3_loc']
        res = self.__session__.get(mp3_location)
        return res.content