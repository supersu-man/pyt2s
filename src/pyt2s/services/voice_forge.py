import requests as __requests__
from enum import Enum as __enum__

class Voice(__enum__):
    Conrad = 'Conrad'
    Designer = 'Designer'
    Diesel = 'Diesel'
    Dog = 'Dog'
    Evilgenius = 'Evilgenius'
    Frank = 'Frank'
    French_fry = 'French-fry'
    Gregory = 'Gregory'
    Jerkface = 'Jerkface'
    JerseyGirl = 'JerseyGirl'
    Kayla = 'Kayla'
    Kevin = 'Kevin'
    Kidaroo = 'Kidaroo'
    Princess = 'Princess'
    RansomNote = 'RansomNote'
    Robot = 'Robot'
    Shygirl = 'Shygirl'
    Susan = 'Susan'
    Tamika = 'Tamika'
    TopHat = 'TopHat'
    Vixen = 'Vixen'
    Vlad = 'Vlad'
    Warren = 'Warren'
    Wiseguy = 'Wiseguy'
    Zach = 'Zach'
    Obama = 'Obama'


__url1__ = 'https://api.voiceforge.com/swift_engine?'

__headers__ = {
    'HTTP_X_API_KEY': '8b3f76a8539',
}

def requestTTS(text: str, voice = 'Conrad'):
    params = {
        'voice': voice,
        'msg': text,
        'email': 'null',
    }
    res = __requests__.get(__url1__, params=params, headers=__headers__)
    return res.content