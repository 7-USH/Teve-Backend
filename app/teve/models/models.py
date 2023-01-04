from teve.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    password = Column(String)
    name = Column(String)
    favs = relationship("Fav", back_populates="creator")


class Fav(Base):
    __tablename__ = "fav"
    stream_link = Column(String, primary_key=True)
    category = Column(String)
    channel_name = Column(String)
    user_id = Column(String, ForeignKey('user.email'))
    creator = relationship("User", back_populates="favs")
