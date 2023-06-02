from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
import os

from .model import Stl
from .tools import check_user_owned_uuid

display = Blueprint('display', __name__)

@display.route('/display', methods=['GET'])
@login_required
def display_index(): #Get the args from URL parameters for the files names. Flask uses werkzeug MultiDict so we can have sevral value for the same key
    uuid = request.args.get('file')
    stl = Stl.query.filter_by(id=uuid).first()
    #Check if the object exists
    if stl is None:
        return '', 404

    if not check_user_owned_uuid(stl):
        return '',403

    file_path = stl.stlChemin[7:]
    name = stl.name
    return render_template('display.html', ThreeD=file_path, Filename=name, Username=current_user.name)