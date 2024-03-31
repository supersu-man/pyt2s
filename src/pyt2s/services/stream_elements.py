import requests
from ..service import Service

class StreamElements(Service):

    __validNames__ = [ 'Brian', 'Amy', 'Emma', 'Geraint', 'Russell', 'Nicole', 'Joey', 'Justin', 'Matthew', 'Ivy', 'Joanna', 'Kendra', 'Kimberly', 'Salli', 'Raveena', 'Zhiyu', 
        'Mads', 'Naja', 'Ruben', 'Lotte', 'Mathieu', 'Celine', 'Chantal', 'Hans', 'Marlene', 'Vicki', 'Aditi', 'Karl', 'Dora', 'Carla', 'Bianca', 'Giorgio', 
        'Takumi', 'Mizuki', 'Seoyeon', 'Liv', 'Ewa', 'Maja', 'Jacek', 'Jan', 'Ricardo', 'Vitoria', 'Cristiano', 'Ines', 'Carmen', 'Maxim', 'Tatyana', 'Enrique', 
        'Conchita', 'Mia', 'Miguel', 'Penelope', 'Astrid', 'Filiz', 'Gwyneth', 'en-US-Wavenet-A', 'en-US-Wavenet-B', 'en-US-Wavenet-C', 'en-US-Wavenet-D', 
        'en-US-Wavenet-E', 'en-US-Wavenet-F', 'en-US-Standard-B', 'en-US-Standard-C', 'en-US-Standard-D', 'en-US-Standard-E', 'en-GB-Standard-A', 'en-GB-Standard-B', 
        'en-GB-Standard-C', 'en-GB-Standard-D', 'en-GB-Wavenet-A', 'en-GB-Wavenet-B', 'en-GB-Wavenet-C', 'en-GB-Wavenet-D', 'en-AU-Standard-A', 'en-AU-Standard-B', 
        'en-AU-Wavenet-A', 'en-AU-Wavenet-B', 'en-AU-Wavenet-C', 'en-AU-Wavenet-D', 'en-AU-Standard-C', 'en-AU-Standard-D', 'en-IN-Wavenet-A', 'en-IN-Wavenet-B', 
        'en-IN-Wavenet-C', 'af-ZA-Standard-A', 'ar-XA-Wavenet-A', 'ar-XA-Wavenet-B', 'ar-XA-Wavenet-C', 'bg-bg-Standard-A', 'cmn-CN-Wavenet-A', 'cmn-CN-Wavenet-B', 
        'cmn-CN-Wavenet-C', 'cmn-CN-Wavenet-D', 'cs-CZ-Wavenet-A', 'da-DK-Wavenet-A', 'nl-NL-Standard-A', 'nl-NL-Wavenet-A', 'nl-NL-Wavenet-B', 'nl-NL-Wavenet-C', 
        'nl-NL-Wavenet-D', 'nl-NL-Wavenet-E', 'fil-PH-Wavenet-A', 'fi-FI-Wavenet-A', 'fr-FR-Standard-C', 'fr-FR-Standard-D', 'fr-FR-Wavenet-A', 'fr-FR-Wavenet-B', 
        'fr-FR-Wavenet-C', 'fr-FR-Wavenet-D', 'fr-CA-Standard-A', 'fr-CA-Standard-B', 'fr-CA-Standard-C', 'fr-CA-Standard-D', 'de-DE-Standard-A', 'de-DE-Standard-B', 
        'de-DE-Wavenet-A', 'de-DE-Wavenet-B', 'de-DE-Wavenet-C', 'de-DE-Wavenet-D', 'el-GR-Wavenet-A', 'hi-IN-Wavenet-A', 'hi-IN-Wavenet-B', 'hi-IN-Wavenet-C', 
        'hu-HU-Wavenet-A', 'is-is-Standard-A', 'id-ID-Wavenet-A', 'id-ID-Wavenet-B', 'id-ID-Wavenet-C', 'it-IT-Standard-A', 'it-IT-Wavenet-A', 'it-IT-Wavenet-B', 
        'it-IT-Wavenet-C', 'it-IT-Wavenet-D', 'ja-JP-Standard-A', 'ja-JP-Wavenet-A', 'ja-JP-Wavenet-B', 'ja-JP-Wavenet-C', 'ja-JP-Wavenet-D', 'ko-KR-Standard-A', 
        'ko-KR-Wavenet-A', 'lv-lv-Standard-A', 'nb-no-Wavenet-E', 'nb-no-Wavenet-A', 'nb-no-Wavenet-B', 'nb-no-Wavenet-C', 'nb-no-Wavenet-D', 'pl-PL-Wavenet-A', 
        'pl-PL-Wavenet-B', 'pl-PL-Wavenet-C', 'pl-PL-Wavenet-D', 'pt-PT-Wavenet-A', 'pt-PT-Wavenet-B', 'pt-PT-Wavenet-C', 'pt-PT-Wavenet-D', 'pt-BR-Standard-A', 
        'ru-RU-Wavenet-A', 'ru-RU-Wavenet-B', 'ru-RU-Wavenet-C', 'ru-RU-Wavenet-D', 'sr-rs-Standard-A', 'sk-SK-Wavenet-A', 'es-ES-Standard-A', 'sv-SE-Standard-A', 
        'tr-TR-Standard-A', 'tr-TR-Wavenet-A', 'tr-TR-Wavenet-B', 'tr-TR-Wavenet-C', 'tr-TR-Wavenet-D', 'tr-TR-Wavenet-E', 'uk-UA-Wavenet-A', 'vi-VN-Wavenet-A', 
        'vi-VN-Wavenet-B', 'vi-VN-Wavenet-C', 'vi-VN-Wavenet-D', 'Linda', 'Heather', 'Sean', 'Hoda', 'Naayf', 'Ivan', 'Herena', 'Tracy', 'Danny', 'Huihui', 'Yaoyao', 
        'Kangkang', 'HanHan', 'Zhiwei', 'Matej', 'Jakub', 'Guillaume', 'Michael', 'Karsten', 'Stefanos', 'Szabolcs', 'Andika', 'Heidi', 'Kalpana', 'Hemant', 'Rizwan', 
        'Filip', 'Lado', 'Valluvar', 'Pattara', 'An' ]

    __url1__ = 'https://api.streamelements.com/kappa/v2/speech?'

    def requestTTS(self, text: str, voice = 'Brian'):
        super().requestTTS(text, voice)
        params = {
            'voice': voice,
            'text': text
        }
        res = requests.get(self.__url1__, params)
        return res.content