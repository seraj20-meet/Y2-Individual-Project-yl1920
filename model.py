from sqlalchemy import Column, Integer, String, Boolean,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class Celebrity(Base):
    __tablename__ = "celebrities"
    id=Column(Integer,primary_key=True)
    name= Column(String)
    value= Column(Float)
