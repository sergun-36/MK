from flask import Flask, jsonify, request
from models import Seans, Player, Hero, Game, engine, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import exc
from settings import logger
from flask_swagger import swagger
from datetime import datetime as dt

Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
#logger.info("Check logger")

app = Flask(__name__)

@app.route("/")
def home():
	logger.info("Home is successfull")
	return "THis is MK"

@app.route("/seans")
def seans_all():
	try:
		session = Session()
		seans_query = session.query(Seans).all()
		seans = [seans.serialize for seans in seans_query]
		res = jsonify(seans)
		logger.info("All seanses is got")
		return res, 200

	except Exception as ex:
		message = f"Seanses can not be recieved. Exception - {ex}"
		res = jsonify({"error":message})
		logger.warning(message)
		return res, 400


@app.route("/seans/<seans_id>")
def seans_one(seans_id):
	try:
		session = Session()
		seans_query = session.query(Seans).filter(Seans.id ==seans_id ).one()
		res = jsonify(seans_query.serialize)
		logger.info(f"Seans with {seans_id} is recieved successfull")
		return res, 200
	except Exception as ex:
		message = f"Seans with {seans_id} is not recieved. Error is {ex}"
		logger.warning(message)
		res = jsonify({"error": message})
		return res, 400

@app.route("/seans/create", methods = ["POST"])
def create_seans():
	content = request.get_json()
	#seans_name = content.get("name")
	date = request.get("date")
	if date:
		try:
			session = Session()
			new_seans = Seans(date) 



@app.route("/users", methods = ["GET"])
def all_users():
	session = Session()
	try:
		player_query = session.query(Player).all()
		logger.info(player_query)
	except exc.NoResultFound as ex:
		logger.warning(f"No records {ex}")
	return str(player_query)


@app.route("/spec")
def spec():
	swag =  swagger(app)
	swag["info"]["version"] = "1.0"
	swag["info"]["title"] = "My API"
	return jsonify(swag)


if __name__ == "__main__":
	app.run(debug = True)