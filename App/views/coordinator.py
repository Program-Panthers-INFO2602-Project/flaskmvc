from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from App.controllers import *

coordinator_views = Blueprint('coordinator_views', __name__, template_folder='../templates')

@coordinator_views.route('/coordinator', methods = ['GET'])
def coordinator_view():
    return render_template('ResultsManager.html')


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



@coordinator_views.route('/coordinator/manage-competition', methods = ['GET'])
def manage_competition_view():
    user = Coordinator.query.filter_by(first_name = current_user.first_name).first()
    return render_template('editCompetition.html')


@coordinator_views.route('/coordinator/manage-competition', methods = ['POST'])
def manage_competition_action():
    return render_template('editCompetition.html')



@coordinator_views.route('/coordinator/add-team', methods = ['GET'])
def add_team_view():
    return render_template('addTeam.html')

@coordinator_views.route('/coordinator/manage-team', methods = ['GET'])
def manage_team_view():
    return render_template('editTeam.html')