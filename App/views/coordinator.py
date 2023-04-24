from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.controllers import *

coordinator_views = Blueprint('coordinator_views', __name__, template_folder='../templates')

@coordinator_views.route('/coordinator', methods = ['GET'])
def coordinator_view():
    user = Coordinator.query.filter_by(first_name = current_user.first_name).first()
    organization = Organization.query.get(user.organization_id)

    return render_template('ResultsManager.html', organization = organization.name)


@coordinator_views.route('/coordinator/add-competition', methods = ['GET'])
def add_competition_view():
    return render_template('addCompetition.html')


@coordinator_views.route('/coordinator/add-competition', methods = ['POST'])
def add_competition_action():
    data = request.form

    coordinator = Coordinator.query.get(current_user.id)
    newcompetition = coordinator.add_competition(data['name'], data['start_time'], data['end_time'])
    if not newcompetition:
        flash('Competition name taken!') 
        return redirect('/coordinator/add-competition')
    else:
        flash("Competition added!")
        return redirect('/coordinator')


@coordinator_views.route('/<string:competition_name>/dashboard', methods = ['GET'])
def dashboard_view(competition_name):
    user = Coordinator.query.filter_by(first_name = current_user.first_name).first()
    if isinstance(user, Coordinator):
        user_type = 'Coordinator'
    else:
        user_type = None
    
    

    return render_template('dashboard.html', competition = competition_name, user_type = user_type)


@coordinator_views.route('/<string:competition_name>/manage-results', methods = ['GET'])
def manage_results_view(competition_name):
    user = Coordinator.query.filter_by(first_name = current_user.first_name).first()
    if isinstance(user, Coordinator):
        user_type = 'Coordinator'
    else:
        user_type = None
    

    return render_template('manageCompetitionResults.html', user_type = user_type)


