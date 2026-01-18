import requests
import re
import json

url = "https://www.hume.ai/_next/static/chunks/28502-3d0beaf4ab1e1f39.js"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Not(A:Brand\";v=\"8\", \"Chromium\";v=\"144\", \"Brave\";v=\"144\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "referer": "https://demo.hume.ai/?showLogo=false&showHeading=true"
}


response = requests.get(url, headers=headers)
data = response.text.split("let P=")[1].split("}];")[0] + "}]"
data = re.sub(r'\\x([0-9a-fA-F]{2})', r'\\u00\1', data)
data = re.sub(r'([{,]\s*)(\w+):', r'\1"\2":', data)
data = re.sub(r':\s*[EMS]\.default', r': "icon"', data)
json_data = json.loads(data)[0]["voices"]

with open("src/pyt2s/voices/hume.py", "w", encoding="utf-8") as f:
    f.write("from enum import Enum as __enum__\n\n")
    f.write("class Voice(__enum__):\n")
    for voice in json_data:
        f.write(f"    {voice['name'].replace('-', '_').replace(' ', '_').replace("'", "")} = \"{voice['id']}\"\n")

    