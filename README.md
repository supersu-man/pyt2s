# pyt2s
The Python Text to Speech library you've been looking for (maybe not).

**Note: This is a toy project**

A simple python library to convert texts to voice using different TTS services.


## About
This python library is heavily inpired from Chris Phillips's [php tts library](https://github.com/chrisjp/tts). I wanted to use a Python TTS library for one of my projects, but I found none that is simply plug-and-play, supports multiple voices, includes both genders, and doesn’t require me to download trained models of tens of GBs. 

## Services
- Acapela
- Cepstral
- IBM Watson
- Oddcast
- Stream Elements
- Stream Labs
- Voice Forge

## Usage
- Install using `pip install pyt2s`
- Request TTS and saving as mp3
    ```
    from pyt2s.services import stream_elements

    # Default Voice
    data = stream_elements.requestTTS('Lorem Ipsum is simply dummy text.')

    # Custom Voice
    data = stream_elements.requestTTS('Lorem Ipsum is simply dummy text.', stream_elements.Voice.Russell.value)

    with open('output.mp3', '+wb') as file:
        file.write(data)
    ```