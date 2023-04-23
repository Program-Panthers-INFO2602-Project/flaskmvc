from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required, LoginManager, login_user, logout_user
from functools import wraps
from .index import index_views
from App.controllers import *
from App.models import Organization

login_manager = LoginManager()

def competitor_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, User):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

def coordinator_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Coordinator):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

@login_manager.user_loader
def load_user(user_id):
  user =  RegularUser.query.get(user_id)
  if user:
    return user
  return Admin.query.get(user_id)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

#shows home page with all organizations
@user_views.route('/home', methods = ['GET'])
@competitor_required
def homepage_view():
    organizations = Organization.query.all()
    return render_template("organizations.html", organizations = organizations)


@user_views.route('/<string:organization_name>/competitions', methods = ['GET'])
@competitor_required
def organization_competitions_view(organization_name):
    organization = Organization.query.filter_by(name = organization_name).first()
    return render_template("competitions.html", organization = organization_name, competitions = organization.competitions)


@user_views.route('/<string:competition_name>', methods = ['GET'])
@competitor_required
def competition_view(competition_name):
    return render_template("competitionResults.html")

@user_views.route('/account', methods = ['GET'])
@login_required
def account_view():
    
    return render_template('account.html')
