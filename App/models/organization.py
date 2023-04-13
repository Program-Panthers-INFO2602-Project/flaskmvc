from App.models import *

class Organization(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    coordinators = db.relationship()
    competitions = db.relationship()
    

    def __init__(self, name):
        self.name = name

    def get_json(self):
        return{
            'id': self.id,
            'name': self.name,
        }

    def repr():
        return f'<Organization {self.id}: {self.name}> 