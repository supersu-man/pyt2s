
import requests
import re

url = "https://www.cepstral.com/media/js/demos.js?v=2.1.6"
headers = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "sec-ch-ua": '"Chromium";v="142", "Brave";v="142", "Not_A Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "script",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "referer": "https://www.cepstral.com/en/demos"
}

response = requests.get(url, headers=headers, allow_redirects=True)

personal_html_match = re.search(r'var personalHtml = \'(.*?)\';', response.text, re.DOTALL)
personal_html = personal_html_match.group(1)

personal_voices = re.findall(
    r'<option(?: selected="selected")? value="(?!divider)([^"-][^"]*)">', personal_html
)

with open("src/pyt2s/voices/cepstral.py", "w", encoding="utf-8") as f:
    f.write("from enum import Enum as __enum__\n\n")
    f.write("class Voice(__enum__):\n")
    for voice in personal_voices:
        f.write(f"    {voice.replace('-', '_')} = \"{voice}\"\n")