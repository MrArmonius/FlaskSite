from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PATH_USER'] = 'static/upload/user/'
    app.config['UPLOAD_PATH'] = os.path.join('project', app.config['PATH_USER'])
    

    db.init_app(app)

    

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .model import User

    with app.app_context():
        db.create_all()

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for dropzone page
    from .upload import upload as upload_blueprint
    app.register_blueprint(upload_blueprint)

    # blueprint for visualize STL file
    from .display import display as display_blueprint
    app.register_blueprint(display_blueprint)

    return app
