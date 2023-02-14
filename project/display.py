from flask import Blueprint, render_template, redirect, url_for, current_app, request, session
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

display = Blueprint('display', __name__)

@display.route('/display', methods=['GET'])
@login_required
def display_index(): #Get the args from URL parameters for the files names. Flask uses werkzeug MultiDict so we can have sevral value for the same key
    file = request.args.get('file')
    name = os.path.join("/static/upload/user/", current_user.get_id()) + "/" + secure_filename(file)
    filename = secure_filename(file).split(".")[0]
    return render_template('display.html', ThreeD=name, Filename=filename, Username=current_user.name, Session=session.sid)