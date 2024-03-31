class Service():

    __url1__ = ''
    __url2__ = ''

    __headers__ = {}

    __validNames__ = []

    def requestTTS(self, text: str, voice: str):
        if voice not in self.__validNames__:
            raise Exception('Not a valid name')