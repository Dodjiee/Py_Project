"""This is configuration file of the application.
    In this file logging is set up, setting up route to the database, initializing Flask,
    SQLAlchemy and Blueprints registration
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate 
from flask_login import LoginManager

login_manager = LoginManager()


app = Flask(__name__)


app.config['SECRET_KEY'] = 'mysecretkey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view = 'users.login'

from company.employees.views import employees
from company.users.views import users
from company.core.views import core
from company.departments.views import departments

app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(departments)
app.register_blueprint(employees)
