from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.controllers import *

coordinator_views = Blueprint('coordinator_views', __name__, template_folder='../templates')

@coordinator_views.route('/coordinator', methods = ['GET'])
def coordinator_view():
    return render_template('ResultsManager.html')