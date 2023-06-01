from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from audio_converter.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    token = Column(String, unique=True, index=True)

    audio = relationship("Audio", back_populates="user")


