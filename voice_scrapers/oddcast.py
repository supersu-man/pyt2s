import requests
import json

url = "https://www.oddcast.com/ttsdemo/"
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Chromium\";v=\"142\", \"Brave\";v=\"142\", \"Not_A Brand\";v=\"99\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "sec-gpc": "1",
    "upgrade-insecure-requests": "1"
}

response = requests.get(url, headers=headers)

jsonString = response.text.split("var voicesData = ")[1].split("};")[0]+"}"
jsonObj = json.loads(jsonString)

voices = []
for key,value in jsonObj.items():
    for(_, voice) in value['voices'].items():
        voice['voice_name'] = voice['voice_name'].replace(" ", "_").replace("(", "").replace(")", "").replace("-", "_")
        voices.append(voice)

with open("src/pyt2s/voices/oddcast.py", "w", encoding="utf-8") as f:
    f.write("from enum import Enum as __enum__\n\n")
    f.write("class Voice(__enum__):\n")
    for voice in voices:
        f.write(f"    {voice['voice_name']} = \"{voice['engine_id']}-{voice['language_id']}-{voice['voice_id']}\"\n")