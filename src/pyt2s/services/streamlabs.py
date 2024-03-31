import requests
from ..service import Service

class StreamLabs(Service):
    
    __validNames__ = [ 'Brian', 'Amy', 'Emma', 'Geraint', 'Russell', 'Nicole', 'Joey', 'Justin', 'Matthew', 'Ivy', 'Joanna', 'Kendra', 'Kimberly', 'Salli', 'Raveena', 'Zeina', 
        'Zhiyu', 'Mads', 'Naja', 'Ruben', 'Lotte', 'Mathieu', 'Celine', 'Lea', 'Chantal', 'Hans', 'Marlene', 'Vicki', 'Aditi', 'Karl', 'Dora', 'Carla', 'Bianca', 
        'Giorgio', 'Takumi', 'Mizuki', 'Seoyeon', 'Liv', 'Ewa', 'Maja', 'Jacek', 'Jan', 'Ricardo', 'Camila', 'Vitoria', 'Cristiano', 'Ines', 'Carmen', 'Maxim', 
        'Tatyana', 'Enrique', 'Conchita', 'Lucia', 'Mia', 'Miguel', 'Lupe', 'Penelope', 'Astrid', 'Filiz', 'Gwyneth' ]
    
    __url1__ = 'https://streamlabs.com/polly/speak'
    
    __headers__ = {
        'Referer': 'https://streamlabs.com'
    }
    
    def requestTTS(self, text: str, voice = 'Brian'):
        super().requestTTS(text, voice)
        params = {
            'voice': voice,
            'text': text
        }
        res = requests.post(self.__url1__, params=params, headers=self.__headers__)
        mp3_url = res.json()['speak_url']
        res = requests.get(mp3_url)
        return res.content