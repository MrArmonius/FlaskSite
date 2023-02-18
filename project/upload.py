from flask import Blueprint, render_template, redirect, url_for, \
	send_from_directory, current_app, request, session
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
import imghdr
import uuid

from .preview import generate_preview
from . import db
from .model import Stl


upload = Blueprint('upload', __name__)



# def validate_image(stream):
# 	header = stream.read(512)
# 	stream.seek(0)
# 	format = imghdr.what(None, header)
# 	if not format:
# 		return None
# 	return '.' + (format if format != 'jpeg' else 'jpg')

@upload.app_errorhandler(413)
def too_large(e):
	return "File is too large", 413

@upload.route('/upload', methods=['GET'])
@login_required
def upload_index():
	files = os.listdir(os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), "template"))
	files_name = []
	for name in files:
		if name[-4:] == "jpeg":
			files_name.append(os.path.join(current_app.config['PATH_USER'], current_user.get_id(), "template", name))
	
	return render_template('upload.html', files=files_name)

@upload.route('/upload', methods=['POST'])
@login_required
def upload_post():
	for key, f in request.files.items():
		if key.startswith('file'):
			path = os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), secure_filename(f.filename))
			f.save(path)
			generate_preview(path, secure_filename(f.filename))

			new_uuid = str(uuid.uuid4())

			# create a new stl entrance to store it
			new_stl = Stl(id=new_uuid,userId=current_user.get_id(), filament="PLA", couleur="black", stlChemin=path)

    		# add the new stl entrance
			db.session.add(new_stl)
			db.session.commit()

			return new_uuid, 202
	return "Incorrect file", 400

@upload.route('/upload',  methods=['DELETE'])
@login_required
def upload_delete():
	name = request.json["id"]
	os.remove(os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), secure_filename(name)))
	return '', 202

@upload.route('/thumbnail/<filename>')
@login_required
def upload_f(filename):
	filename_secure = secure_filename(filename) + '.jpeg'
	return os.path.join(current_app.config['PATH_USER'], current_user.get_id(), "template", filename_secure)
