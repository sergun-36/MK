from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from settings import db_settings


engine = create_engine(URL.create(**db_settings))
Base = declarative_base()

class Seans(Base):
	__tablename__ = "seans"
	id = Column(Integer, primary_key=True)
	date = Column("date", String)


class Player(Base):
	__tablename__ = "player"
	id_player = Column(Integer, primary_key=True)
	name_player = Column("name_player", String)
	id_seans = Column(Integer, ForeignKey("seans.id"))	


class Hero(Base):
	__tablename__ = "hero"
	id_hero = Column(Integer, primary_key = True)
	name_hero = Column("name_hero", String)
	id_player = Column(Integer, ForeignKey("player.id_player"))


class Game(Base):
	__tablename__ = "game"
	id_game = Column(Integer, primary_key=True)
	id_hero_one = Column(Integer, ForeignKey("hero.id_hero"))
	id_hero_two = Column(Integer, ForeignKey("hero.id_hero"))
	result_hero_1 = Column(Integer)
	result_hero_2 = Column(Integer)
	is_playoff = Column(Integer)



