from App.models import *

class LeaderBoard(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    competition_id = db.Column(db.Integer, db.ForeignKey(Competition.id), nullable = False, unique = False)
    team_id = db.Column(db.Integer, db.ForeignKey(Team.id), nullable = False, unique = False)
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

