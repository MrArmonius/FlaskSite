from flask import Blueprint, render_template, redirect, url_for, \
	send_from_directory, current_app, request, session
from flask_login import login_required, current_user

import requests

from .model import Stl
from . import db

api_engine = Blueprint('api_engine', __name__)

@api_engine.route('/api_engine/start/<uuid>', methods=['GET'])
@login_required
def send_request(uuid):
	print("This is uuid: ", uuid)

	url = 'http://127.0.0.1:3250/jobs'
	data = {'data': '{"job_id":"'+uuid+'"}'}
	stl = Stl.query.filter_by(id=uuid).first()

	#Check if the object exists
	if stl is None:
		return '', 404

	print(stl.stlChemin)
	if not check_user_owned_uuid(stl):
		return '',403

	print(stl.stlChemin)
	file_stl = {'file': open(stl.stlChemin ,'rb')}
	headers = {'Accept-Encoding': ''}

	response = requests.post(url, files = file_stl, data = data)

	print(response.request.url)
	#	print(response.request.body.decode('utf-8'))
	print(response.request.headers)

	return '', 202

@api_engine.route('/api_engine/<uuid>', methods=['GET'])
@login_required
def get_status(uuid):
	stl = Stl.query.filter_by(id=uuid).first()

	#Check if the object exists
	if stl is None:
		return '', 404

	#check if the user own the uuid
	if not check_user_owned_uuid(stl):
		return '',403
	
	url = 'http://127.0.0.1:3250/jobs/'+uuid
	response = requests.get(url)

	print("Code return: ", response.status_code)

	print("Json: ", response.json())

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


	return '', 200

def check_user_owned_uuid(orm):
	# Check if the uuid is owned by the correct user
	user_log = int(current_user.get_id())
	user_uuid = orm.userId
	if(user_log != user_uuid):
		return False
	else:
		return True