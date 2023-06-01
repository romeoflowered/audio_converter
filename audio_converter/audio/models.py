
import uuid

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from audio_converter.database import Base


class Audio(Base):
    __tablename__ = "audio"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    file_name = Column(String, unique=True, index=True)

    user = relationship("User", back_populates="audio")
