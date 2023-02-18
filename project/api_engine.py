from flask import Blueprint, render_template, redirect, url_for, \
	send_from_directory, current_app, request, session
from flask_login import login_required, current_user

import requests

from .model import Stl

api_engine = Blueprint('api_engine', __name__)

@api_engine.route('/api_engine/<uuid>', methods=['GET'])
@login_required
def send_request(uuid):
	print("This is uuid: ", uuid)
	url = 'http://127.0.0.1:3250/jobs'
	data = {'data': '{"job_id":"'+uuid+'"}'}
	stl = Stl.query.filter_by(id=uuid).first()
	print(stl.stlChemin)
	file_stl = {'file': open('/home/armonius/Documents/flask/FlaskAPI_RESTful/README.md' ,'rb')}
	headers = {'Accept-Encoding': ''}

	response = requests.post(url, files = file_stl, data = data)

	print(response.request.url)
	print(response.request.body.decode('utf-8'))
	print(response.request.headers)

	return '', 202