# when our app starts its first goes through this file 

from flask import Flask
from .routes.cat_routes import cats_bp
from .db import db, migrate
from app.models.cat import Cat
import os

def create_app(config=None):
    # __name__ stores the name of the module we're in
    app = Flask(__name__)                                           # instance of flask

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False            # any modifications, could be noisy, we dont keep tracks of it, set it to false
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')    #points to our db "flasky_dev".
    if config:
        app.config.update(config)

    db.init_app(app)            # follow doc, db has function init_app, put (flask app) in it
    migrate.init_app(app, db)   # migrate has init_app function and pass (app, db ) in it

    app.register_blueprint(cats_bp)

    return app