import requests
import re

url = "https://www.acapela-group.com/demo.json"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.6",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": '"Chromium";v="142", "Brave";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "referer": "https://www.acapela-group.com/demos/"
}

response = requests.get(url, headers=headers, allow_redirects=True)
matches = re.findall(r'"VoiceNameForTTSTools"\s*:\s*"([^"]+)"', response.text)

keys = set()
with open("src/pyt2s/voices/acapela.py", "w", encoding="utf-8") as f:
    f.write("from enum import Enum as __enum__\n\n")
    f.write("class Voice(__enum__):\n")
    for match in matches:
        if(match not in keys):
            keys.add(match)
            f.write(f"    {match.replace('-', '_')} = \"{match}\"\n")
