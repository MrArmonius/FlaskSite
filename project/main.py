from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

from .model import Stl
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    #Get all uuid link to this user id
    
    array_jobs = Stl.query.filter_by(userId=current_user.get_id()).all()
    
    for job in array_jobs:
        job.templateChemin = job.templateChemin[8:]
    print(array_jobs)
    return render_template('profile.html', name=current_user.name, jobs=array_jobs)
