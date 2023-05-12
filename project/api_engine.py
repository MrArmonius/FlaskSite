from flask import Blueprint, render_template, redirect, url_for, \
	send_from_directory, current_app, request, session
from flask_login import login_required, current_user

import requests

from .model import Stl
from . import db

api_engine = Blueprint('api_engine', __name__)

@api_engine.route('/price/<uuid>', methods=['POST'])
@login_required
def calculate_price(uuid):
	#Get the JSON data
	json_data = request.json
	#Send bad format if json_data is None and don't have the correct keys
	if json_data is None:
		return '', 400
	if not ("material" in json_data and "color" in json_data) and len(json_data.keys()) != 2:
		return '', 400

	stl = Stl.query.filter_by(id=uuid).first()

	#Check if the object exists
	if stl is None:
		return '', 404

	if not check_user_owned_uuid(stl):
		return '',403

	#Apply transformation about color and material with colors

	if stl.state == "Init":
		response = send_request(stl, uuid)
		return '',206

	if stl.state != "Finish":
		json_response = get_status(stl, uuid)
		
		return json_response,206

	json_response = get_status(stl, uuid)
	json_response['price'] = algo_price(stl)
	return json_response,200

	
def send_request(stl, uuid):
	print("This is uuid: ", uuid)

	url = 'http://127.0.0.1:3250/jobs'
	data = {'data': '{"job_id":"'+uuid+'"}'}

	file_stl = {'file': open(stl.stlChemin ,'rb')}
	headers = {'Accept-Encoding': ''}

	response = requests.post(url, files = file_stl, data = data)

	stl.state = "Sending"
	db.session.commit()

	return response

def get_status(stl, uuid):
	url = 'http://127.0.0.1:3250/jobs/'+uuid
	response = requests.get(url)

	# Feed the database with the new informations.
	dico_job = response.json()['job']

	stl.state = dico_job['status']

	#Feed the databse if the status is 'Finish'
	if dico_job['status'] == 'Finish':
		stl.volumeFilament = dico_job['filament_volume']
		stl.minx = dico_job['minx']
		stl.miny = dico_job['miny']
		stl.minz = dico_job['minz']
		stl.maxx = dico_job['maxx']
		stl.maxy = dico_job['maxy']
		stl.maxz = dico_job['maxz']
		stl.time = dico_job['time']
		stl.layerHeight = dico_job['layer_height']
		stl.lengthFilament = dico_job['filament_used']
		db.session.commit()


	return dico_job

def check_user_owned_uuid(orm):
	# Check if the uuid is owned by the correct user
	user_log = int(current_user.get_id())
	user_uuid = orm.userId
	if(user_log != user_uuid):
		return False
	else:
		return True

def algo_price(stl):
	#Return an int in function of the time and the length and the material used
	time, filament_length, material = stl.time, stl.lengthFilament, stl.filament
	
	#Price for 1 seconds:
	time_delta = 0.001

	#Price for 1meter of material depends of material value
	filament_length_delta = 1.0

	#Final price
	price = round((time*time_delta + filament_length*filament_length_delta)*2,2)

	stl.price = price
	db.session.commit()
	return price