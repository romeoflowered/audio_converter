from audio_converter.audio.models import Audio
from audio_converter.dao.dao import BaseDAO


class AudioDAO(BaseDAO):
    model = Audio
