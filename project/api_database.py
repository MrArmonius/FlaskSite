from flask import Blueprint, render_template, redirect, url_for, \
	send_from_directory, current_app, request, session
from flask_login import login_required, current_user

from .model import Stl

api_database = Blueprint('api_database', __name__)

@api_database.route('/profile/jobs', methods=['GET'])
@login_required
def send_jobs():
    user_id = int(current_user.get_id())
    stl = Stl.query.filter_by(userId=user_id).all()
    print(stl)
    for stl_sample in stl:
        print("Id: ", stl_sample.id)
        print("Date: ", stl_sample.creation_date.strftime("%m/%d/%Y, %H:%M:%S"), " type: ", type(stl_sample.creation_date))
        print("Couleur: ", stl_sample.couleur)
        print("Material: ", stl_sample.filament)
        print("Price: ", stl_sample.price)
        print(" -- -- -- -- -- -- ")

    return '', 200
