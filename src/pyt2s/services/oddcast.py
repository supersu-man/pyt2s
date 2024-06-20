import requests as __requests__
from enum import Enum as __enum__

class Voice(__enum__):
    v4_3_1 = '4-3-1'
    v6_2_1 = '6-2-1'
    v5_4_1 = '5-4-1'
    v4_2_1 = '4-2-1'
    v5_3_1 = '5-3-1'
    v2_7_1 = '2-7-1'
    v1_7_1 = '1-7-1'
    v7_4_1 = '7-4-1'
    v5_2_1 = '5-2-1'
    v12_4_1 = '12-4-1'
    v8_4_1 = '8-4-1'
    v9_2_1 = '9-2-1'
    v10_2_1 = '10-2-1'
    v4_7_1 = '4-7-1'
    v4_4_1 = '4-4-1'
    v10_4_1 = '10-4-1'
    v3_7_1 = '3-7-1'
    v13_4_1 = '13-4-1'
    v5_7_1 = '5-7-1'
    v6_7_1 = '6-7-1'
    v9_4_1 = '9-4-1'
    v11_2_1 = '11-2-1'
    v7_2_1 = '7-2-1'
    v6_3_1 = '6-3-1'
    v8_3_1 = '8-3-1'
    v7_7_1 = '7-7-1'
    v3_1_1 = '3-1-1'
    v1_1_1 = '1-1-1'
    v2_2_1 = '2-2-1'
    v7_3_1 = '7-3-1'
    v2_4_1 = '2-4-1'
    v3_3_1 = '3-3-1'
    v1_3_1 = '1-3-1'
    v2_1_1 = '2-1-1'
    v2_3_1 = '2-3-1'
    v4_1_1 = '4-1-1'
    v11_4_1 = '11-4-1'
    v8_2_1 = '8-2-1'
    v1_2_1 = '1-2-1'
    v3_4_1 = '3-4-1'
    v8_7_1 = '8-7-1'
    v1_7_27 = '1-7-27'
    v2_7_27 = '2-7-27'
    v2_2_27 = '2-2-27'
    v1_4_27 = '1-4-27'
    v1_2_27 = '1-2-27'
    v1_4_22 = '1-4-22'
    v3_2_5 = '3-2-5'
    v2_2_5 = '2-2-5'
    v1_2_5 = '1-2-5'
    v1_4_5 = '1-4-5'
    v3_3_10 = '3-3-10'
    v5_3_10 = '5-3-10'
    v4_3_10 = '4-3-10'
    v1_2_10 = '1-2-10'
    v2_2_10 = '2-2-10'
    v4_4_10 = '4-4-10'
    v4_7_10 = '4-7-10'
    v6_3_10 = '6-3-10'
    v7_3_10 = '7-3-10'
    v1_4_10 = '1-4-10'
    v3_7_10 = '3-7-10'
    v2_7_10 = '2-7-10'
    v1_7_10 = '1-7-10'
    v2_4_10 = '2-4-10'
    v8_3_10 = '8-3-10'
    v1_7_18 = '1-7-18'
    v1_4_18 = '1-4-18'
    v1_7_19 = '1-7-19'
    v2_7_19 = '2-7-19'
    v1_2_19 = '1-2-19'
    v1_4_19 = '1-4-19'
    v2_2_19 = '2-2-19'
    v2_4_11 = '2-4-11'
    v2_7_11 = '2-7-11'
    v1_7_11 = '1-7-11'
    v2_2_11 = '2-2-11'
    v1_2_11 = '1-2-11'
    v4_4_11 = '4-4-11'
    v1_4_11 = '1-4-11'
    v1_2_31 = '1-2-31'
    v2_7_32 = '2-7-32'
    v1_7_32 = '1-7-32'
    v2_2_23 = '2-2-23'
    v1_4_23 = '1-4-23'
    v1_2_23 = '1-2-23'
    v1_7_23 = '1-7-23'
    v2_1_4 = '2-1-4'
    v2_7_4 = '2-7-4'
    v1_7_4 = '1-7-4'
    v2_2_4 = '2-2-4'
    v4_2_4 = '4-2-4'
    v3_2_4 = '3-2-4'
    v1_1_4 = '1-1-4'
    v4_3_4 = '4-3-4'
    v3_3_4 = '3-3-4'
    v3_4_4 = '3-4-4'
    v5_4_4 = '5-4-4'
    v4_4_4 = '4-4-4'
    v5_2_4 = '5-2-4'
    v1_3_4 = '1-3-4'
    v1_4_4 = '1-4-4'
    v4_7_4 = '4-7-4'
    v2_4_4 = '2-4-4'
    v2_3_4 = '2-3-4'
    v3_7_4 = '3-7-4'
    v6_2_4 = '6-2-4'
    v3_1_4 = '3-1-4'
    v1_2_15 = '1-2-15'
    v3_4_3 = '3-4-3'
    v2_7_3 = '2-7-3'
    v1_7_3 = '1-7-3'
    v3_2_3 = '3-2-3'
    v1_1_3 = '1-1-3'
    v1_3_3 = '1-3-3'
    v2_1_3 = '2-1-3'
    v2_2_3 = '2-2-3'
    v1_4_3 = '1-4-3'
    v2_3_3 = '2-3-3'
    v2_4_3 = '2-4-3'
    v1_2_8 = '1-2-8'
    v1_4_8 = '1-4-8'
    v1_7_8 = '1-7-8'
    v2_7_8 = '2-7-8'
    v3_2_8 = '3-2-8'
    v2_7_24 = '2-7-24'
    v1_4_24 = '1-4-24'
    v1_7_24 = '1-7-24'
    v1_4_29 = '1-4-29'
    v1_7_29 = '1-7-29'
    v2_7_28 = '2-7-28'
    v1_4_28 = '1-4-28'
    v1_7_28 = '1-7-28'
    v2_7_7 = '2-7-7'
    v1_7_7 = '1-7-7'
    v1_3_7 = '1-3-7'
    v10_2_7 = '10-2-7'
    v9_2_7 = '9-2-7'
    v5_2_7 = '5-2-7'
    v6_2_7 = '6-2-7'
    v8_2_7 = '8-2-7'
    v1_2_7 = '1-2-7'
    v1_4_7 = '1-4-7'
    v7_2_7 = '7-2-7'
    v2_3_7 = '2-3-7'
    v2_2_7 = '2-2-7'
    v2_4_7 = '2-4-7'
    v3_2_7 = '3-2-7'
    v6_3_12 = '6-3-12'
    v5_3_12 = '5-3-12'
    v1_7_12 = '1-7-12'
    v2_7_12 = '2-7-12'
    v1_4_12 = '1-4-12'
    v3_3_12 = '3-3-12'
    v7_3_12 = '7-3-12'
    v4_3_12 = '4-3-12'
    v2_3_12 = '2-3-12'
    v8_3_12 = '8-3-12'
    v7_3_13 = '7-3-13'
    v4_3_13 = '4-3-13'
    v8_3_13 = '8-3-13'
    v10_3_13 = '10-3-13'
    v5_3_13 = '5-3-13'
    v2_3_13 = '2-3-13'
    v1_4_13 = '1-4-13'
    v6_3_13 = '6-3-13'
    v1_3_13 = '1-3-13'
    v9_3_13 = '9-3-13'
    v1_7_20 = '1-7-20'
    v2_2_20 = '2-2-20'
    v2_7_20 = '2-7-20'
    v2_4_20 = '2-4-20'
    v1_2_20 = '1-2-20'
    v1_4_14 = '1-4-14'
    v1_7_14 = '1-7-14'
    v2_2_14 = '2-2-14'
    v2_7_14 = '2-7-14'
    v1_2_14 = '1-2-14'
    v2_7_6 = '2-7-6'
    v3_4_6 = '3-4-6'
    v3_7_6 = '3-7-6'
    v4_7_6 = '4-7-6'
    v1_7_6 = '1-7-6'
    v1_3_6 = '1-3-6'
    v2_3_6 = '2-3-6'
    v2_4_6 = '2-4-6'
    v1_2_30 = '1-2-30'
    v1_4_30 = '1-4-30'
    v2_2_21 = '2-2-21'
    v2_4_21 = '2-4-21'
    v1_2_21 = '1-2-21'
    v1_7_37 = '1-7-37'
    v3_4_37 = '3-4-37'
    v1_2_2 = '1-2-2'
    v6_2_2 = '6-2-2'
    v2_2_2 = '2-2-2'
    v9_2_2 = '9-2-2'
    v4_3_2 = '4-3-2'
    v5_3_2 = '5-3-2'
    v1_4_2 = '1-4-2'
    v3_4_2 = '3-4-2'
    v7_2_2 = '7-2-2'
    v8_2_2 = '8-2-2'
    v10_2_2 = '10-2-2'
    v4_2_2 = '4-2-2'
    v3_2_2 = '3-2-2'
    v2_1_2 = '2-1-2'
    v5_2_2 = '5-2-2'
    v2_3_2 = '2-3-2'
    v3_3_2 = '3-3-2'
    v5_4_2 = '5-4-2'
    v4_4_2 = '4-4-2'
    v1_1_2 = '1-1-2'
    v1_3_2 = '1-3-2'
    v1_4_9 = '1-4-9'
    v1_2_9 = '1-2-9'
    v1_7_9 = '1-7-9'
    v2_7_9 = '2-7-9'
    v3_4_9 = '3-4-9'
    v2_2_9 = '2-2-9'
    v1_4_26 = '1-4-26'
    v1_3_26 = '1-3-26'
    v2_3_26 = '2-3-26'
    v1_4_16 = '1-4-16'
    v2_7_16 = '2-7-16'
    v1_2_16 = '1-2-16'
    v3_2_16 = '3-2-16'
    v1_7_16 = '1-7-16'
    v2_2_16 = '2-2-16'
    v1_7_40 = '1-7-40'

__url1__ = 'https://cache-a.oddcast.com/tts/genB.php'

def requestTTS(text: str, voice = '3-3-1'):
    voiceParts = voice.split('-')
    voiceId, engineId, languageId = voiceParts
    params = {
        'EID': int(engineId),
        'LID': int(languageId),
        'VID': int(voiceId),
        'TXT': text,
        'EXT': 'mp3',
        'FNAME': '',
        'ACC': 15679,
        'SceneID': 2703396,
        'HTTP_ERR': '',
        'cache_flag': 3
    }
    res = __requests__.get(__url1__, params=params)
    return res.content