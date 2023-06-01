from audio_converter.dao.dao import BaseDAO
from audio_converter.users.models import User


class UserDAO(BaseDAO):
    model = User
