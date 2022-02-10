from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

display = Blueprint('display', __name__)

@display.route('/display', methods=['GET'])
@login_required
def display_index(): #Get the args from URL parameters for the files names. Flask uses werkzeug MultiDict so we can have sevral value for the same key
    files = request.args.getlist('file')
    name = []
    filenames = []
    for file in files:
        name.append(os.path.join("/static/upload/user/", current_user.get_id()) + "/" + secure_filename(file))
        filenames.append(secure_filename(file).split(".")[0])
    return render_template('display.html', ThreeDs=name, Filename=filenames, Username=current_user.name)