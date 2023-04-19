from App.models import TeamMember
from App.database import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable = False, unique = False)
    team_name = db.Column(db.String, nullable = False, unique = True)
    points = db.Column(db.Integer, unique = False, nullable = False)
    time_taken = db.Column(db.Time, unique = False, nullable = True)
    members = db.relationship('User', secondary = 'team_member', backref = 'team', lazy = True)


    def __init__(self, competition_id, team_name, points, time_taken):
        self.competition_id = competition_id
        self.team_name = team_name
        self.points = points
        self.time_taken = time_taken

    def calculate_rank(self, competition_id, points, time_taken):
        competition = Competition.query.filter_by(id = competition_id)
        
            

    def get_json(self):
        return{
            'id': self.id,
            'competition_id' : self.competition_id,
            'team_name': self.team_name,
            'points': self.points,
            'rank': self.rank,
            'time_taken': self.time_taken
        }

    def repr():
        return f'<Team {self.id} :21 {self.team_name} - {self.points} {self.time_taken}>'