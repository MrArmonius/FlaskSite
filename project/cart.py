from flask import Blueprint, render_template, redirect, url_for, current_app, request
from flask_login import login_required, current_user

from .model import Stl, ShoppingCart
from .tools import check_user_owned_uuid


cart = Blueprint('cart', __name__)

@cart.route('/cart_resume', methods=['GET'])
@login_required
def cart_resume():
    return render_template('cart.html')

@cart.route('/add_item_cart/<uuid : String>', methods=['POST'])
@login_required
def add_item_cart(uuid):
    #Check if the uuid is owned by the same user and if the object exists
    stl = Stl.query.filter_by(id=uuid).first()
    #Check if the object exists
    if stl is None:
        return '', 404

    if not check_user_owned_uuid(stl):
        return '',403

    #Now add the items
    #The quantity
    quantity = request.args.get('quantity')
    if quantity is None:
        return 'Quantity is null', 400
    
    