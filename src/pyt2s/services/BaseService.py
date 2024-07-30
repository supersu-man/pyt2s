from src.pyt2s.models.BaseModel import BaseVoiceModel


class BaseService():
    voice_service: BaseVoiceModel

    def requestTTS(self, text: str, voice: BaseVoiceModel):
        return Exception('you can not use base service for requests')
