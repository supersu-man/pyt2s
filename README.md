# pyt2s
The Python Text-to-Speech library you didn’t know you needed (or maybe you did).

**⚠️ Toy project alert: This is experimental and fun, not production-grade.**

[![Downloads](https://static.pepy.tech/badge/pyt2s)](https://pepy.tech/project/pyt2s)

# 🎯 What is pyt2s

A lightweight Python wrapper for generating speech from text using various online TTS services—no heavy model downloads, no complex setup. Just plug, play, and talk.

Inspired by Chris Phillips's [php tts library](https://github.com/chrisjp/tts) library, pyt2s was born out of frustration:

“Why is there no Python TTS library that’s simple, supports multiple voices (including both genders), and doesn’t ask me to download 20GB of models?”

Now there is.

# 🧠 Supported TTS Service

pyt2s taps into several online services to give you voice variety:
- Acapela
- Cepstral
- Oddcast
- Stream Elements
- Stream Labs
- Voice Forge

# 🚀 Installation

### Option 1: From Source

```
git clone https://github.com/yourusername/pyt2s.git
cd pyt2s
pip install -r requirements.txt
pip install -e .
```

### Option 2: From PyPI

```
pip install pyt2s
```

# 🛠️ Usage

Here’s how to convert text to speech and save it as an MP3:

```
from pyt2s.services import stream_elements

# Default Voice
data = stream_elements.requestTTS('Lorem Ipsum is simply dummy text.')

# Custom Voice
data = stream_elements.requestTTS('Lorem Ipsum is simply dummy text.', stream_elements.Voice.Russell)

with open('output.mp3', '+wb') as file:
    file.write(data)
```
