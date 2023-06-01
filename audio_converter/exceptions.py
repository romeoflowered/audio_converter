from fastapi import HTTPException, status

UserAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="Пользователь уже существует"
)

UserNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Пользователь не существует"
)

AudioFormatBadException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Поддерживается только audio.wav - формат"
)

ThisUserHasNoAudioException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Аудиозапись не найдена")


