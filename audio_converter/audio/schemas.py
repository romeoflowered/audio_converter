from fastapi import File, UploadFile
from pydantic import BaseModel


class SAddAudioRequest(BaseModel):
    user_id: int
    token: str


class SAudioResponse(BaseModel):
    audio_id: str
    download_url: str
