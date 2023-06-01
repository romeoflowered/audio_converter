import uuid

from sqlalchemy import delete, insert, select

from audio_converter.database import session_maker


class BaseDAO:
    model = None

    @classmethod
    def find_by_id(cls, model_id: uuid.UUID):
        with session_maker() as session:
            query = select(cls.model).filter_by(id=model_id)
            result = session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    def find_one_or_none(cls, **filter_by):
        with session_maker() as session:
            query = session.query(cls.model).filter_by(**filter_by)
            return query.one_or_none()

    @classmethod
    def add(cls, **data):
        with session_maker() as session:
            new_instance = cls.model(**data)
            session.add(new_instance)
            session.commit()
            return new_instance

    @classmethod
    def delete(cls, **filter_by):
        with session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            session.execute(query)
            session.commit()

