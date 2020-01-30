from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_celeb_db(name, value):
    celeb=Celebrity(name=name, value=value)
    #there is a line of code missing here, what else does a user ne
    session.add(celeb)
    session.commit()

def get_all():
	cc=session.query(Celebrity).all()
	return cc 



# def get_user(name,value):
#     """Find the first user in the DB, by their username."""
#     return session.query().filter_by(username=username).first()
# def update(username,fav_food):
# 	user=get_user(username)
# 	user.fav_food=fav_food
# 	session.commit()