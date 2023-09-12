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

@app.route("/seans/", methods = ["GET"])
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


@app.route("/seans/<seans_id>/", methods = ["GET"])
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

@app.route("/create/seans/", methods = ["POST"])
def create_seans():
	print(request)
	try:
		content = request.get_json()
		#seans_name = content.get("name")
		print(content)
		date = content.get("date")
		number_player = content.get("number_player")
		number_hero = content.get("number_hero")
		if date and number_hero and number_player:
			try:
				session = Session()
				new_seans = Seans(date=date, number_hero=number_hero, number_player=number_player, is_active=1)
				session.add(new_seans)
				session.commit()
				logger.info(f"New seans with date {date} is added")
				res = jsonify(new_seans.serialize)
				return res, 201
			except Exception as ex:
				message = f"New seans is not added. Error is {ex}"
				logger.warning(message)
				res  = jsonify({"error":message})
				return res, 400
		else:
			message = "seans is not added. Key date is not found"
			logger.warning(message)
			res = jsonify({"error": message})
			return res, 400
	except Exception as ex:
		message = f"Seans is not created. Error is {ex}"
		logger.warning(message)
		res = jsonify({"error": message})
		return res, 400



@app.route("/players/", methods = ["GET"])
def all_players():
	try:
		session = Session()
		player_query = session.query(Player).all()
		players = [player.serialize for player in player_query]
		res = jsonify(players)
		logger.info("All players are recieved")
		return res, 200
	except Exception as ex:
		message = f"Plaers are not recieved. Error is {ex}"
		logger.warning(message)
		res = jsonify({"error": message})
		return res, 400

@app.route("/players/<id_player>", methods = ["GET"])
def one_player(id_player):
	try:
		session =Session()
		player_query = session.query(Player).filter(Player.id_player == id_player).one()
		res = jsonify(player_query.serialize)
		return res, 200
	except Exception as ex:
		message = f"Player with id {id_player} is not recieved. Error is {ex}"
		logger.warning(message)
		res = jsonify({"error": message})
		return res, 400

@app.route("/create/player", methods = ["POST"])
def create_player():
	print(request)
	try:
		content = request.get_json()
		if content:
			try:
				session = Session()
				# id_seans = session.query(Seans).filter(Seans.is_active==1).one()
				all_players = [Player(name_player = player['name'], id_seans=player['id_seans']) for player in content]
				print(all_players)
				session.add_all(all_players)
				session.commit()
				res = jsonify([new_player.serialize for new_player in all_players])
				logger.info("New player is created successfull")
				return res, 201
			except Exception as ex:
				message = f"Players are not added. Error is {ex}"
				logger.warning(message)
				res  = jsonify({"error":message})
				return res, 400
		else:
			message = "Players aren't added. names are not found"
			logger.warning(message)
			res = jsonify({"error": message})
			return res, 400
	except Exception as ex:
		message = f"Players are not added. Error is {ex}"
		logger.warning(message)
		res = jsonify({"error": message})
		return res, 400

@app.route("/spec/")
def spec():
	swag =  swagger(app)
	swag["info"]["version"] = "1.0"
	swag["info"]["title"] = "My API"
	return jsonify(swag)


if __name__ == "__main__":
	app.run(debug = True)