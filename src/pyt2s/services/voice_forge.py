import requests
from ..service import Service

class VoiceForge(Service):
    
    __validNames__ = [ 'Conrad', 'Designer', 'Diesel', 'Dog', 'Evilgenius', 'Frank', 'French-fry', 'Gregory', 'Jerkface', 'JerseyGirl', 'Kayla', 'Kevin', 
        'Kidaroo', 'Princess', 'RansomNote', 'Robot', 'Shygirl', 'Susan', 'Tamika', 'TopHat', 'Vixen', 'Vlad', 'Warren', 'Wiseguy', 'Zach', 'Obama' ]
    
    __url1__ = 'https://api.voiceforge.com/swift_engine?'
    
    __headers__ = {
        'HTTP_X_API_KEY': '8b3f76a8539',
    }
    
    def requestTTS(self, text: str, voice = 'Conrad'):
        super().requestTTS(text, voice)
        params = {
            'voice': voice,
            'msg': text,
            'email': 'null',
        }
        res = requests.get(self.__url1__, params=params, headers=self.__headers__)
        return res.content