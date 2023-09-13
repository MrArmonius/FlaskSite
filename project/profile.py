from flask import Blueprint, render_template
from . import db
from flask_login import login_required, current_user

from .model import Stl
from .model import User
from . import db

profile = Blueprint('profile', __name__)

@profile.route('/jobs')
@login_required
def jobs():
    #Get all uuid link to this user id
    
    array_jobs = Stl.query.filter_by(userId=current_user.get_id()).all()
    
    for job in array_jobs:
        job.templateChemin = job.templateChemin[8:]
    print(array_jobs)
    return render_template('jobs.html', name=current_user.name, jobs=array_jobs)

@profile.route('/informations')
@login_required
def informations():
    return render_template('informations_profile.html', name=current_user.name, userObject=current_user)

@profile.route('/factures')
@login_required
def factures():
    
    return render_template('factures.html', name=current_user.name)