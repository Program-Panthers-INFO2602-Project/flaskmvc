from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required, LoginManager, login_user, logout_user

from .index import index_views
from App.controllers import *

login_manager = LoginManager()

def user_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, RegularUser):
            return "Unauthorized", 401
        return func(*args, **kwargs)
    return wrapper

def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated or not isinstance(current_user, Admin):
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
def homepage_view():
    return render_template('organizations.html')


@user_views.route('/account', methods = ['GET'])
@login_required
def account_view():
    render_template('account.html')
