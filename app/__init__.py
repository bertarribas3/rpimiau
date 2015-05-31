from flask import Flask, session, request, flash, url_for, redirect, render_template, abort, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_user , logout_user , current_user , login_required

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login'

from app import views, models, forms

