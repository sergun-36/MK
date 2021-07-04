import logging.config
import yaml

with open("logging.yaml", "r") as file:
	log_yaml_conf = yaml.safe_load(file.read())

logging.config.dictConfig(log_yaml_conf)
logger = logging.getLogger("simpleExample")


db_settings = {"database": "MK.db",
				"drivername": "sqlite"}