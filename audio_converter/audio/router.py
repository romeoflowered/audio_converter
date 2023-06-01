import os
import uuid

from fastapi import APIRouter, File, UploadFile
from pydub import AudioSegment

from audio_converter.audio.dao import AudioDAO
from audio_converter.audio.schemas import SAudioResponse
from audio_converter.exceptions import (
    AudioFormatBadException,
    ThisUserHasNoAudioException,
    UserNotFoundException,
)
from audio_converter.users.dao import UserDAO

router = APIRouter(
    prefix="/audio",
    tags=["Аудиозапись"]
)


@router.get("", response_model=SAudioResponse)
def download_audio(user_id: int, token: str, audio_uuid: uuid.UUID):
    existing_user = UserDAO.find_one_or_none(id=user_id, token=token)
    if not existing_user:
        raise UserNotFoundException

    audio = AudioDAO.find_by_id(model_id=audio_uuid)

    if not audio or audio.user_id != user_id:
        raise ThisUserHasNoAudioException

    download_url = f"http://host:port/record?id={audio.id}&user={user_id}"

    return SAudioResponse(audio_id=str(audio_uuid), download_url=download_url)


@router.post("", response_model=SAudioResponse)
def add_audio(user_id: int, token: str, audio_file: UploadFile = File(...)):
    filename = audio_file.filename
    extension = filename.split(".")[-1].lower()
    if extension != "wav":
        raise AudioFormatBadException

    existing_user = UserDAO.find_one_or_none(id=user_id, token=token)
    if not existing_user:
        raise UserNotFoundException

    audio_uuid = uuid.uuid4()

    audio_file_path = os.path.join("audio_converter/audio_files", f"{audio_uuid}.wav")

    with open(audio_file_path, "wb") as f:
        f.write(audio_file.file.read())

    audio = AudioSegment.from_wav(audio_file_path)
    audio_mp_3_path = os.path.join("audio_converter/audio_files", f"{audio_uuid}.mp3")
    audio.export(audio_mp_3_path, format="mp3")

    audio_record = AudioDAO.add(id=audio_uuid, user_id=user_id, file_name=f"{audio_uuid}.mp3")

    download_url = f"http://host:port/record?id={audio_uuid}&user={user_id}"

    return SAudioResponse(audio_id=str(audio_uuid), download_url=download_url)
