from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

from .model import Stl

display = Blueprint('display', __name__)

@display.route('/display', methods=['GET'])
@login_required
def display_index(): #Get the args from URL parameters for the files names. Flask uses werkzeug MultiDict so we can have sevral value for the same key
    uuid = request.args.get('file')
    file = Stl.query.filter_by(id=uuid).first()
    file_path = file.stlChemin[7:]
    name = file.stlChemin.split('/')[-1]
    #name = os.path.join("/static/upload/user/", current_user.get_id()) + "/" + secure_filename(file)
    #filename = secure_filename(file).split(".")[0]
    return render_template('display.html', ThreeD=file_path, Filename=name, Username=current_user.name)