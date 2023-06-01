from pydantic import BaseModel


class SCreateUserRequest(BaseModel):
    name: str


class SCreateUserResponse(BaseModel):
    user_id: str
    token: str
