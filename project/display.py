from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

display = Blueprint('display', __name__)

@display.route('/display', methods=['GET'])
@login_required
def display_index():
    return render_template('display.html')