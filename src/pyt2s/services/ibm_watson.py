import requests as __requests__
import uuid as __uuid__
from enum import Enum as __enum__

class Voice(__enum__):
    en_GB_CharlotteV3Voice = 'en-GB_CharlotteV3Voice'
    en_GB_JamesV3Voice = 'en-GB_JamesV3Voice'
    en_GB_KateV3Voice = 'en-GB_KateV3Voice'
    en_AU_JackExpressive = 'en-AU_JackExpressive'
    en_AU_HeidiExpressive = 'en-AU_HeidiExpressive'
    en_US_AllisonV3Voice = 'en-US_AllisonV3Voice'
    en_US_AllisonExpressive = 'en-US_AllisonExpressive'
    en_US_EmilyV3Voice = 'en-US_EmilyV3Voice'
    en_US_EmmaExpressive = 'en-US_EmmaExpressive'
    en_US_HenryV3Voice = 'en-US_HenryV3Voice'
    en_US_KevinV3Voice = 'en-US_KevinV3Voice'
    en_US_LisaV3Voice = 'en-US_LisaV3Voice'
    en_US_LisaExpressive = 'en-US_LisaExpressive'
    en_US_MichaelV3Voice = 'en-US_MichaelV3Voice'
    en_US_MichaelExpressive = 'en-US_MichaelExpressive'
    en_US_OliviaV3Voice = 'en-US_OliviaV3Voice'
    nl_NL_MerelV3Voice = 'nl-NL_MerelV3Voice'
    fr_FR_NicolasV3Voice = 'fr-FR_NicolasV3Voice'
    fr_FR_ReneeV3Voice = 'fr-FR_ReneeV3Voice'
    fr_CA_LouiseV3Voice = 'fr-CA_LouiseV3Voice'
    de_DE_BirgitV3Voice = 'de-DE_BirgitV3Voice'
    de_DE_DieterV3Voice = 'de-DE_DieterV3Voice'
    de_DE_ErikaV3Voice = 'de-DE_ErikaV3Voice'
    it_IT_FrancescaV3Voice = 'it-IT_FrancescaV3Voice'
    ja_JP_EmiV3Voice = 'ja-JP_EmiV3Voice'
    ko_KR_JinV3Voice = 'ko-KR_JinV3Voice'
    pt_BR_IsabelaV3Voice = 'pt-BR_IsabelaV3Voice'
    es_ES_EnriqueV3Voice = 'es-ES_EnriqueV3Voice'
    es_ES_LauraV3Voice = 'es-ES_LauraV3Voice'
    es_LA_SofiaV3Voice = 'es-LA_SofiaV3Voice'
    es_US_SofiaV3Voice = 'es-US_SofiaV3Voice'

__session__ = __requests__.session()
__url1__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/session'   
__url2__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/store'   
__url3__ = 'https://www.ibm.com/demos/live/tts-demo/api/tts/newSynthesizer'

__headers__ = {
    'Origin': 'https://www.ibm.com',
    'Referer': 'https://www.ibm.com/demos/live/tts-demo/self-service/home',
    'Accept': 'application/json, text/plain, */*',
}

def requestTTS(text: str, voice = 'en-GB_CharlotteV3Voice'):
    __session__.post(__url1__, headers=__headers__)
    id = str(__uuid__.uuid4())    
    jsonPayload = {"ssmlText": f"<prosody pitch=\"0%\" rate=\"-0%\">{text}</prosody>", "sessionID": id}   
    __session__.post(__url2__, data=jsonPayload, headers=__headers__)
    res = __session__.get(__url3__, params={'voice' : voice,'id': id})
    return res.content