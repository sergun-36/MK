from models import Seans, Player, Hero, Game, engine, Base
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)