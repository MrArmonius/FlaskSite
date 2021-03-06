from flask import Blueprint, render_template, redirect, url_for, \
	send_from_directory, current_app, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os
import imghdr

upload = Blueprint('upload', __name__)



def validate_image(stream):
	header = stream.read(512)
	stream.seek(0)
	format = imghdr.what(None, header)
	if not format:
		return None
	return '.' + (format if format != 'jpeg' else 'jpg')

@upload.app_errorhandler(413)
def too_large(e):
	return "File is too large", 413

@upload.route('/upload', methods=['GET'])
@login_required
def upload_index():
	files = os.listdir(os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id()))
	return render_template('upload.html', files=files)

@upload.route('/upload', methods=['POST'])
@login_required
def upload_post():
	for key, f in request.files.items():
		if key.startswith('file'):
			f.save(os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), secure_filename(f.filename)))
			return '', 202
	return "Image incorrect", 400

@upload.route('/upload',  methods=['DELETE'])
@login_required
def upload_delete():
	name = request.json["id"]
	os.remove(os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), secure_filename(name)))
	return '', 202

@upload.route('/thumbnail/<filename>')
@login_required
def upload_f(filename):
	#return redirect(os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), filename), code=301)
	return redirect(os.path.join(current_app.config['UPLOAD_PATH'], current_user.get_id(), filename), code=301)
	#return send_from_directory(current_app['UPLOAD_PATH'], filename)
