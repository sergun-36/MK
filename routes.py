from flask import Flask
from models import Seans, Player, Hero, Game, engine, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from settings import logger

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
#logger.info("Check logger")

app = Flask(__name__)

@app.route("/")
def home():
	logger.info("Home is successfull")
	return "THis is MK"

@app.route("/users", methods = ["GET"])
def all_users():
	session = Session()
	try:
		player_query = session.query(Player).all()
		logger.info(player_query)
	except exc.NoResultFound as ex:
		logger.warning(f"No records {ex}")
	return str(player_query)



if __name__ == "__main__":
	app.run(debug = True)