from flask import Flask, Blueprint, render_template,url_for, redirect, request, flash, make_response, jsonify, send_from_directory
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import login_required, login_user, current_user, logout_user

from .index import index_views
from .coordinator import coordinator_views

from App.controllers import *

auth_views = Blueprint('auth_views', __name__, template_folder='../templates')


@auth_views.route('/', methods = ['GET'])
def login_page():
    return render_template('login.html')


@auth_views.route('/signup', methods = ['GET'])
def signup_view():
    return render_template('signup1.html')


@auth_views.route('/signup/competitor', methods = ['GET'])
def signup_competitior_view():
    return render_template('signupcompetitor.html')


@auth_views.route('/signup/coordinator', methods = ['GET'])
def signup_coordinator_view():
    return render_template('signupcoordinator.html')


@auth_views.route('/signup/competitor', methods = ['POST'])
def signup_competitor_action():
    data = request.form

    newuser = signup_user(data['first_name'], data['last_name'], data['email'],
                            data['username'], data['password']) 
    if newuser:
        login_user(newuser)  # login the user
        flash('Account Created!')  # send message
        return redirect('/home')  # redirect to homepage
    else:
        flash("username or email already exists")  # error message
        return redirect('/signup/competitor')


@auth_views.route('/signup/coordinator', methods = ['POST'])
def signup_coordinator_action():
    data = request.form

    newcoordinator = signup_coordinator(data['first_name'], data['last_name'], data['email'], data['username'],
                        data['password'], data['organization_name'])
                         
    if newcoordinator:
        login_user(newcoordinator)  # login the user
        flash('Account Created!')  # send message
        return redirect('/coordinator')  # redirect to homepage
    else:
        flash("username or email already exists")  # error message
        return redirect('/signup/coordinator')


@auth_views.route('/login', methods=['POST'])
def login_action():
    data = request.form
    user = login_competitor(data['username'], data['password'])
    if user:
        flash('Logged in successfully.')  
        login_user(user)  
        return redirect('/home') # redirect to hompage

    coordinator = login_coordinator(data['username'], data['password'])
    if coordinator:
        flash('Logged in successfully.')
        login_user(coordinator)
        return redirect('/coordinator')

    flash('Invalid username or password') # send message to next page
    return redirect('/')


@auth_views.route('/logout', methods=['GET'])
def logout_action():
  logout_user()
  flash('Logged Out')
  return redirect('/')

