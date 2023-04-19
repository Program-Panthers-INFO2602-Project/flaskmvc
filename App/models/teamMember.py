from App.database import db

class TeamMember(db.Model):
    __tablename__ = 'team_member'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable = False, unique = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False, unique = False)