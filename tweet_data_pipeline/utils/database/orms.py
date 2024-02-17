from typing import Type, TypeVar

from sqlalchemy import INTEGER, TEXT, Column, DateTime, MetaData, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Common base class for all declarative ORMs."""

    pass


class Tweets(Base):
    """Define metadate for airport tweets."""

    metadata = MetaData(schema="public")
    __tablename__ = "tweets"
    twitter_user = Column(String, primary_key=True)
    date_created = Column(DateTime(timezone=False), primary_key=True)
    number_of_likes = Column(INTEGER)
    source_of_tweet = Column(String)
    tweet = Column(TEXT)


BaseType = TypeVar("BaseType", bound=Type[Base])
