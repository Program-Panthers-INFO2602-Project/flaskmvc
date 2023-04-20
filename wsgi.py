import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from datetime import time
from App.database import db, get_migrate
from App.main import create_app
from App.controllers import *

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def initialize():
    db.drop_all()
    db.create_all()
    create_user('Bob', 'Smith', 'bob@mail.com', 'bobby123', 'bobpass')
    create_coordinator('Jane', 'Doe', 'janedoe@mail.com', 'jane123', 'janepass', 'UWI')
    print('database intialized')


'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)

@user_cli.command("list_users", help="Lists users in the database")
@click.argument("format", default="json")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())


@user_cli.command("search_user", help="Search for user in database")
@click.argument("username", default="bobby123")
def search_user_command(username):
    user = get_user(username)
    print(user.repr())


@user_cli.command("search_comp", help="Search for competition in database")
@click.argument("competition_name", default="Runtime_Competition")
def search_comeptition_command(competition_name):
    competition = get_competition(competition_name)
    print(competition.repr())


@user_cli.command("search_team", help="Search for team in database")
@click.argument("team_name", default="Program_Panthers")
def search_team_command(team_name):
    team = get_team(team_name)
    print(team.repr())

app.cli.add_command(user_cli) # add the group to the cli


'''
Coordinator Commands
'''
coordinator_cli = AppGroup('coordinator', help='Coordinator object commands') 

@coordinator_cli.command("add_comp", help="Add competition")
@click.argument("competition_name", default = "Runtime_Competition")
@click.argument("start_time", default = '12:00')
@click.argument("end_time", default = '12:00')
@click.argument("coordinator_username", default = 'jane123')
def add_competition_command(coordinator_username, competition_name, start_time, end_time):
    user = get_coordinator(coordinator_username)
    if not user:
        print('Coordinator not found!')
        return None

    competition = user.add_competition(competition_name, start_time, end_time)
    print('Competition added.')

# Create a time object with hours, minutes, and seconds
#my_time = time(12, 34, 56)  # Represents 12:34:56


@coordinator_cli.command("edit_comp", help="Edit competition")
@click.argument("competition_name", default = "Hackathon")
@click.argument("start_time", default = '10:00')
@click.argument("end_time", default = '12:00')
@click.argument("coordinator_username", default = 'jane123')
@click.argument("competition_id", default = 1)
def edit_competition_command(coordinator_username, competition_id, competition_name, start_time, end_time):
    user = get_coordinator(coordinator_username)
    if not user:
        print('Coordinator not found!')
        return None

    competition = user.edit_competition(competition_id, competition_name, start_time, end_time)
    print('Competition edited.')


@coordinator_cli.command("remove_comp", help="Remove competition")
@click.argument("coordinator_username", default = 'jane123')
@click.argument("competition_id", default = 1)
def edit_competition_command(coordinator_username, competition_id):
    user = get_coordinator(coordinator_username)
    if not user:
        print('Coordinator not found!')
        return None

    competition = user.remove_competition(competition_id)
    print('Competition removed.')


@coordinator_cli.command("list_competitions", help="Lists all competitions in the database")
@click.argument("format", default="json")
def list_competition_command(format):
    if format == 'string':
        print(get_all_competitions())
    else:
        print(get_all_competitions_json())


@coordinator_cli.command("add_team", help="Add Team to a competition")
@click.argument("team_name", default = "Program_Panthers")
@click.argument("points", default = '100')
@click.argument("coordinator_username", default = 'jane123')
@click.argument("competition_name", default = 'Runtime_Competition')
@click.argument("time_taken", default = '1:20')
def add_team_command(coordinator_username, competition_name, team_name, points, time_taken):
    user = get_coordinator(coordinator_username)
    if not user:
        print('Coordinator not found!')
        return None

    competition = get_competition(competition_name)
    if competition:
        competition_id = competition.id

    if not competition:
        print('Competition not found!')
        return None

    team = user.add_team(competition.id, team_name, points, time_taken)
    print('Team added.')


@coordinator_cli.command("edit_team", help="Edit team")
@click.argument("competition_name", default = "Runtime_Competition")
@click.argument("team_name", default = 'AI_Squad')
@click.argument("points", default = '120')
@click.argument("time_taken", default = '1:30')
@click.argument("team_id", default = 1)
@click.argument("coordinator_username", default = 'jane123')
def edit_team_command(coordinator_username, competition_name, team_id, team_name, points, time_taken):
    user = get_coordinator(coordinator_username)
    if not user:
        print('Coordinator not found!')
        return None

    competition = get_competition(competition_name)
    team = user.edit_team(competition.id, team_id, team_name, points, time_taken)
    print('Team edited.')


@coordinator_cli.command("remove_team", help="Remove team")
@click.argument("coordinator_username", default = 'jane123')
@click.argument("team_id", default = 1)
def edit_competition_command(coordinator_username, team_id):
    user = get_coordinator(coordinator_username)
    if not user:
        print('Coordinator not found!')
        return None

    team = user.remove_team(team_id)
    print(team)
    print('Competition removed.')


@coordinator_cli.command("list_teams", help="Lists all teams in the database")
@click.argument("format", default="json")
def list_team_command(format):
    if format == 'string':
        print(get_all_teams())
    else:
        print(get_all_teams_json())


@coordinator_cli.command("list_comp_teams", help="Lists all teams for a particular competition")
@click.argument("format", default="json")
@click.argument("competition_name", default="Hackathon")
def list_team_command(format, competition_name):
    if format == 'string':
        print(get_all_competition_teams(competition_name))
    else:
        print(get_all_competition_teams_json(competition_name))

app.cli.add_command(coordinator_cli) # add the group to the cli


'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)