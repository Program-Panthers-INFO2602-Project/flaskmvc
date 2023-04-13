from App.models import *

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    organization_id = db.Column(db.Integer, nullable = False, unique = False)
    start_time = db.Column(db.Time, unique = False, unique = False)
    end_time = db.COlumn(db.Time, unique = False, nullable = False)
    teams = db.relationship()
    leaderboard_entries = db.relationship()

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
        return f'<Competition {self.id}: {self.name} - Start Time: {self.start_time} End Time: {self.end_time}> 