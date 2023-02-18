from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Stl(db.Model):
    id = db.Column(db.String(36), primary_key=True) # primary keys are required by SQLAlchemy
    userId = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    filament = db.Column(db.String(12), nullable=False, server_default="PLA")
    volumeFilament = db.Column(db.Integer, nullable=True)
    couleur = db.Column(db.String(20), nullable=False, server_default="black")
    minx = db.Column(db.Integer, nullable=True)
    miny = db.Column(db.Integer, nullable=True)
    minz = db.Column(db.Integer, nullable=True)
    maxx = db.Column(db.Integer, nullable=True)
    maxy = db.Column(db.Integer, nullable=True)
    maxz = db.Column(db.Integer, nullable=True)
    stlChemin = db.Column(db.String(180), nullable=False)
    gcodeChemin = db.Column(db.String(180), nullable=True)
    state = db.Column(db.String(20), nullable=False, server_default="Init")


