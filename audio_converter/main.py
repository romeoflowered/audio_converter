from fastapi import FastAPI

from audio_converter.audio.router import router as router_audio
from audio_converter.users.router import router as router_user

app = FastAPI(title="Audio_Converter")

app.include_router(router_user)
app.include_router(router_audio)
