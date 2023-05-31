import zope.sqlalchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

maker = sessionmaker(autoflush=True, autocommit=False)
DBSession = scoped_session(maker)
zope.sqlalchemy.register(DBSession)
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata


def init_model(engine):
    DBSession.configure(bind=engine)
    return DBSession

from postsapi.model.post import Post
from postsapi.model.user import User

__all__ = ('User', 'Post')
