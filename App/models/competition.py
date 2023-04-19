#from App.models import Leaderboard
from App.models import Team
from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False, unique = True)
    organization_id = db.Column(db.Integer,  db.ForeignKey('organization.id'), nullable = False, unique = False)
    start_time = db.Column(db.Time, unique = False, nullable = False)
    end_time = db.Column(db.Time, unique = False, nullable = False)
    teams = db.relationship('Team', backref = 'competition', lazy = True)
    leaderboard_entries = db.relationship('Team', secondary = 'leaderboard', backref = 'leaderboard_entry', lazy = True)

    def __init__(self, name, organization_id, start_time, end_time):
        self.name = name
        self.organization_id = organization_id
        self.start_time = start_time
        self.end_time = end_time


    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'organization_id': self.organization_id,
            'start_time': self.start_time,
            'end_time': self.end_time
        }


    def repr():
        return f'<Competition {self.id}: {self.name} - Start Time: {self.start_time} End Time: {self.end_time}> '