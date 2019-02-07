# Flask app
from flask import Flask
app = Flask(__name__)

# Database
from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///timelogs.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

# App functionalities
from application import views

from application.timelogs import models
from application.timelogs import views

from application.auth import models
from application.auth import views

# Login
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please log in to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Create db tables if necessary
db.create_all()