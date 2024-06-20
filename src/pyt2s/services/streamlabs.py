import requests as __requests__
from enum import Enum as __enum__

class Voice(__enum__):
    Brian = 'Brian'
    Amy = 'Amy'
    Emma = 'Emma'
    Geraint = 'Geraint'
    Russell = 'Russell'
    Nicole = 'Nicole'
    Joey = 'Joey'
    Justin = 'Justin'
    Matthew = 'Matthew'
    Ivy = 'Ivy'
    Joanna = 'Joanna'
    Kendra = 'Kendra'
    Kimberly = 'Kimberly'
    Salli = 'Salli'
    Raveena = 'Raveena'
    Zeina = 'Zeina'
    Zhiyu = 'Zhiyu'
    Mads = 'Mads'
    Naja = 'Naja'
    Ruben = 'Ruben'
    Lotte = 'Lotte'
    Mathieu = 'Mathieu'
    Celine = 'Celine'
    Lea = 'Lea'
    Chantal = 'Chantal'
    Hans = 'Hans'
    Marlene = 'Marlene'
    Vicki = 'Vicki'
    Aditi = 'Aditi'
    Karl = 'Karl'
    Dora = 'Dora'
    Carla = 'Carla'
    Bianca = 'Bianca'
    Giorgio = 'Giorgio'
    Takumi = 'Takumi'
    Mizuki = 'Mizuki'
    Seoyeon = 'Seoyeon'
    Liv = 'Liv'
    Ewa = 'Ewa'
    Maja = 'Maja'
    Jacek = 'Jacek'
    Jan = 'Jan'
    Ricardo = 'Ricardo'
    Camila = 'Camila'
    Vitoria = 'Vitoria'
    Cristiano = 'Cristiano'
    Ines = 'Ines'
    Carmen = 'Carmen'
    Maxim = 'Maxim'
    Tatyana = 'Tatyana'
    Enrique = 'Enrique'
    Conchita = 'Conchita'
    Lucia = 'Lucia'
    Mia = 'Mia'
    Miguel = 'Miguel'
    Lupe = 'Lupe'
    Penelope = 'Penelope'
    Astrid = 'Astrid'
    Filiz = 'Filiz'
    Gwyneth = 'Gwyneth'

__url1__ = 'https://streamlabs.com/polly/speak'

__headers__ = {
    'Referer': 'https://streamlabs.com'
}
    
def requestTTS(text: str, voice = 'Brian'):
    params = {
        'voice': voice,
        'text': text
    }
    res = __requests__.post(__url1__, params=params, headers=__headers__)
    mp3_url = res.json()['speak_url']
    res = __requests__.get(mp3_url)
    return res.content