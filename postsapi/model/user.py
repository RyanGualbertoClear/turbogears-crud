from sqlalchemy import *
from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode, DateTime
from datetime import datetime
from postsapi.model import DeclarativeBase, DBSession


class User(DeclarativeBase):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(255), nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    password = Column(Unicode(255), nullable=False)
    created = Column(DateTime, default=datetime.now)

    def login(self, email, password):
        return DBSession.query(User).filter_by(email=email, password=password).first()

    def signup(self, name, email, password):
        user = User(name=name, email=email, password=password)
        DBSession.add(user)
        DBSession.flush()
        print(user)
        return user


__all__ = ['User']
