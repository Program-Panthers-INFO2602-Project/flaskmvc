from App.models import *
from App.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import uuid

def generate_short_uuid():
  return str(uuid.uuid4())[:8]


class User(db.Model, UserMixin):
    id = db.Column(db.String(10), primary_key=True, default=generate_short_uuid, server_default='gen_random_uuid()')
    first_name = db.Column(db.String(50), nullable = False,  unique = False)
    last_name = db.Column(db.String(50), nullable = False,  unique = False)
    email = db.Column(db.String(50), nullable = False,  unique = True)
    username =  db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.set_password(password)

    def search_team(self, team_name):
        team = Team.query.filter_by(team_name = team_name)
        if not team: 
            return None
        return team

    def search_competition(self, competition_name):
        competition = Competition.query.filter_by(name = competition_name)
        if not competition:
            return None
        return competition

    def search_user(self, username):
        user = User.query.filter_by(username = username).first()
        if not user:
            return None
        return user

    def get_json(self):
        return{
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def repr():
        return f'<User {self.id} : {self.first_name} {self.last_name} {self.username} - {self.email}>'