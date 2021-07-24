import requests
data = {"name_player": "sergei"}
root_url = "http://127.0.0.1:5000/"

def create_player(data):
	response = requests.post(f"{root_url}create/player", json = data)
	return response.json()

def create_seans(data):
	response = requests.post(f"{root_url}create/seans/", json = data)
	return response

data_date = {"date": "2021-07-24"}
print(create_seans(data_date))