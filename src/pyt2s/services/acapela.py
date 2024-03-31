import json
from ..service import Service
import requests

class Acapela(Service):

    __validNames__ = [ 'graham22k', 'harry22k', 'lucy22k', 'lucy_nt22k', 'peter22k', 'peter_nt22k', 'queenelizabeth22k', 'queenelizabeth_nt22k', 'rachel22k', 'rachel_nt22k', 
        'rosie22k', 'sophiabtob22k', 'sophiabtob_nt22k', 'rhona22k', 'rhona_nt22k', 'liam22k', 'lisa22k', 'lisa_nt22k', 'olivia22k', 'tyler22k', 'tyler_nt22k', 
        'deepa22k', 'deepa_nt22k', 'nizareng22k', 'nizareng_nt22k', 'darius22k', 'darius_nt22k', 'ella22k', 'emilioenglish22k', 'josh22k', 'karen22k', 'karen_nt22k', 
        'laura22k', 'laura_nt22k', 'lily22k', 'lily_nt22k', 'micah22k', 'rod22k', 'rod_nt22k', 'ryan22k', 'ryan_nt22k', 'saul22k', 'saul_nt22k', 'scott22k', 
        'sharon22k', 'sharon_nt22k', 'tamira22k', 'tamira_nt22k', 'taylor22k', 'taylor_nt22k', 'tracy22k', 'tracy_nt22k', 'valeriaenglish22k', 'will22k', 
        'will_nt22k', 'leila22k', 'leila_nt22k', 'jalal22k', 'jalal_nt22k', 'mehdi22k', 'mehdi_nt22k', 'nizar22k', 'nizar_nt22k', 'salma22k', 'salma_nt22k', 
        'laia22k', 'laia_nt22k', 'lulu22k', 'lulu_nt22k', 'eliska22k', 'eliska_nt22k', 'mette22k', 'mette_nt22k', 'rasmus22k', 'rasmus_nt22k', 'rikke22k', 
        'rikke_nt22k', 'daan22k', 'daan_nt22k', 'femke22k', 'femke_nt22k', 'jasmijn22k', 'jasmijn_nt22k', 'max22k', 'max_nt22k', 'tessabtob22k', 'tessabtob_nt22k', 
        'christinabtob22k', 'christinabtob_nt22k', 'jeroen22k', 'jeroen_nt22k', 'sofie22k', 'sofie_nt22k', 'zoe22k', 'zoe_nt22k', 'hanna22k', 'hanna_nt22k', 
        'hanus22k', 'hanus_nt22k', 'sanna22k', 'sanna_nt22k', 'alice22k', 'alice_nt22k', 'anais22k', 'anais_nt22k', 'anaisbtob22k', 'anaisbtob_nt22k', 'antoine22k', 
        'antoine_nt22k', 'bruno22k', 'bruno_nt22k', 'claire22k', 'claire_nt22k', 'constance22k', 'constance_nt22k', 'elise22k', 'julie22k', 'julie_nt22k', 'manon22k', 
        'manon_nt22k', 'margaux22k', 'margaux_nt22k', 'valentin22k', 'anthony22k', 'anthony_nt22k', 'louise22k', 'louise_nt22k', 'alice-be22k', 'alice-be_nt22k', 
        'anais-be22k', 'anais-be_nt22k', 'antoine-be22k', 'antoine-be_nt22k', 'bruno-be22k', 'bruno-be_nt22k', 'claire-be22k', 'claire-be_nt22k', 'elise-be22k', 
        'julie-be22k', 'julie-be_nt22k', 'manon-be22k', 'manon-be_nt22k', 'margaux-be22k', 'margaux-be_nt22k', 'valentin-be22k', 'andreas22k', 'andreas_nt22k', 
        'ankebtob22k', 'ankebtob_nt22k', 'claudia22k', 'claudia_nt22k', 'jonas22k', 'julia22k', 'julia_nt22k', 'klaus22k', 'klaus_nt22k', 'lea22k', 'sarah22k', 
        'sarah_nt22k', 'dimitris22k', 'dimitris_nt22k', 'alessio22k', 'aurora22k', 'barbarabtob22k', 'barbarabtob_nt22k', 'chiara22k', 'chiara_nt22k', 'fabiana22k', 
        'fabiana_nt22k', 'vittorio22k', 'vittorio_nt22k', 'sakura22k', 'sakura_nt22k', 'minji22k', 'minji_nt22k', 'bente22k', 'bente_nt22k', 'elias22k', 'emilie22k', 
        'ida22k', 'ida_nt22k', 'kari22k', 'kari_nt22k', 'olav22k', 'olav_nt22k', 'ania22k', 'ania_nt22k', 'gosia22k', 'gosia_nt22k', 'isabel22k', 'isabel_nt22k', 
        'gabriela22k', 'gabriela_nt22k', 'marcia22k', 'marcia_nt22k', 'sergio22k', 'sergio_nt22k', 'alyona22k', 'alyona_nt22k', 'lena22k', 'lena_nt22k', 
        'biera_hmm_22k', 'elle_hmm_22k', 'anabtob22k', 'anabtob_nt22k', 'antonio22k', 'antonio_nt22k', 'elenabtob22k', 'elenabtob_nt22k', 'ines22k', 'ines_nt22k', 
        'maria22k', 'maria_nt22k', 'emilio22k', 'rodrigo22k', 'rodrigo_nt22k', 'rosa22k', 'rosa_nt22k', 'valeria22k', 'elin22k', 'elin_nt22k', 'emil22k', 
        'emil_nt22k', 'emma22k', 'emma_nt22k', 'erik22k', 'erik_nt22k', 'filip22k', 'freja22k', 'kal22k', 'kal_nt22k', 'mia22k', 'mia_nt22k', 'samuel22k', 
        'samuel_nt22k', 'ipek22k', 'ipek_nt22k', 'zeynep22k', 'zeynep_nt22k' ]

    __session__ = requests.session()
    __url1__ = 'https://www.acapela-group.com/www/static/website/demoOptionsDef_voicedemo.php'
    __url2__ = 'https://h-ir-ssd-1.acapela-group.com/webservices/1-60-00/UrlMaker.json'

    __headers__ = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Referer': 'https://www.acapela-group.com/demos/',
        'Origin': 'https://www.acapela-group.com/demos/',                             
    }

    def requestTTS(self, text: str, voice = 'sharon22k'):
        super().requestTTS(text, voice)
        res = self.__session__.get(self.__url1__, headers=self.__headers__)
        json_res = res.text.replace('var vaasOptions = ', '').replace('};', '}')
        json_res = json.loads(json_res)
        params = {
            'cl_login': json_res['login'],
            'cl_app': json_res['app'],
            'session_start': json_res['session']['start'],
            'session_time': json_res['session']['time'],
            'session_key': json_res['session']['key'],
            'req_voice': voice,
            'req_text': text
        }

        res = self.__session__.post(self.__url2__, params=params, headers=self.__headers__)
        res = self.__session__.get(res.json()['snd_url'])
        return res.content