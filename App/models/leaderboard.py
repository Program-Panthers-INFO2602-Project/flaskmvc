from App.models import *
from App.database import db

class LeaderBoard(db.Model):
    __tablename__ = 'leaderboard'
    id = db.Column(db.Integer, primary_key = True)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable = False, unique = False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable = False, unique = False)
    rank = db.Column(db.Integer, nullable = False, unique = False)
    
    def __init__(self, competition_id, team_id, rank):
        self.competition_id = competition_id
        self.team_id = team_id
        self.rank = rank


    def get_json(self):
        return{
            'id': self.id,
            'competition_id': self.competition_id,
            'team_id': self.team_id,
            'rank': self.rank
        }

