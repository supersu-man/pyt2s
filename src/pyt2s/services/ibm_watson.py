import requests
import uuid
from ..service import Service

class IBM_Watson(Service):
    
    __validNames__ = [ 'en-GB_CharlotteV3Voice', 'en-GB_JamesV3Voice', 'en-GB_KateV3Voice', 'en-AU_JackExpressive', 'en-AU_HeidiExpressive', 'en-US_AllisonV3Voice', 
        'en-US_AllisonExpressive', 'en-US_EmilyV3Voice', 'en-US_EmmaExpressive', 'en-US_HenryV3Voice', 'en-US_KevinV3Voice', 'en-US_LisaV3Voice', 
        'en-US_LisaExpressive', 'en-US_MichaelV3Voice', 'en-US_MichaelExpressive', 'en-US_OliviaV3Voice', 'nl-NL_MerelV3Voice', 'fr-FR_NicolasV3Voice', 
        'fr-FR_ReneeV3Voice', 'fr-CA_LouiseV3Voice', 'de-DE_BirgitV3Voice', 'de-DE_DieterV3Voice', 'de-DE_ErikaV3Voice', 'it-IT_FrancescaV3Voice', 
        'ja-JP_EmiV3Voice', 'ko-KR_JinV3Voice', 'pt-BR_IsabelaV3Voice', 'es-ES_EnriqueV3Voice', 'es-ES_LauraV3Voice', 'es-LA_SofiaV3Voice', 'es-US_SofiaV3Voice' ]

    __session__ = requests.session()   
    __url1__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/session'   
    __url2__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/store'   
    __url3__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/newSynthesizer'

    def requestTTS(self, text: str, voice = 'en-GB_CharlotteV3Voice'):
        super().requestTTS(text, voice)
        id = str(uuid.uuid4())       
        self.__session__.post(self.__url1__)       
        res = self.__session__.get(self.__url2__, params=params)       
        params = {'ssmlText': f'<prosody pitch=\'0%\' rate=\'-0%\'>{text}</prosody>', 'sessionID': id}       
        res = self.__session__.get(f'{self.__url3__}?voice={voice}&id={id}')
        return res.content