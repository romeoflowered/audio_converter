import uuid

from fastapi import APIRouter

from audio_converter.exceptions import UserAlreadyExistsException
from audio_converter.users.dao import UserDAO
from audio_converter.users.schemas import SCreateUserRequest, SCreateUserResponse

router = APIRouter(
    prefix="/user",
    tags=["Пользователь"]
)


@router.post("", response_model=SCreateUserResponse)
def create_user(request: SCreateUserRequest):
    existing_user = UserDAO.find_one_or_none(name=request.name)
    if existing_user:
        raise UserAlreadyExistsException
    uuid_token = str(uuid.uuid4())
    new_user = UserDAO.add(name=request.name, token=uuid_token)

    return SCreateUserResponse(user_id=new_user.id, token=uuid_token)
