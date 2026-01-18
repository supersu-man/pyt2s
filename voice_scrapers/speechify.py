import requests
import json
import re

url = "https://cdn.speechify.com/voiceover-demo/assets/bundle.js"

headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "referer": "https://speechify.com/",
}

session = requests.Session()

def getResponse():
    response = session.get(url, headers=headers)
    response.encoding = "utf-8"
    return response

def getVoices(response):
    data = response.text.split("wc=")[1].split(";")[0]
    data = re.sub(r'([{,]\s*)(\w+):', r'\1"\2":', data)
    data = data.replace("\"languages\":jt(),","")
    return json.loads(data)

def getTones(response):
    data = response.text.split("Xn=")[1].split("];")[0] + "]"
    data = re.sub(r'([{,]\s*)(\w+):', r'\1"\2":', data)
    data = data.replace("\"default\":!1,","")
    data = data.replace("\"default\":!0,","")
    data = data.replace("\"defaultText\":Sn,","")
    data = data.replace(",\"defaultVoice\":Br","")
    return json.loads(data)

response = getResponse()
voices = getVoices(response)
tones = getTones(response)

with open("src/pyt2s/voices/speechify.py", "w", encoding="utf-8") as f:
    f.write("from enum import Enum as __enum__\n\n")
    f.write("class Voice(__enum__):\n")
    for voice in voices:
        f.write(f"    {voice['name'].replace('-', '_').replace(' ', '_').replace("'", "")} = \"{voice['id']}\"\n")
    f.write("\n")
    f.write("class Tone(__enum__):\n")
    for tone in tones:
        f.write(f"    {tone['style'].replace('-', '_').replace(' ', '_').replace("'", "")} = \"{tone['prompt']}\"\n")
