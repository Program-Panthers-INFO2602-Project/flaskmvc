from App.models import * 

class AdminUser(User):
    coordinator_id = db.Column(db.Integer, primary_key=True)
    organization_id = db.Column(db.Integer, db.ForeignKey(organization.id), nullable = False, unique = False)
    competitions = db.relationship('admins')

    def __init__(self, coordinator_id, organization_id, first_name, last_name, email, username, password):
        super().__init__(first_name, last_name, email, username, password)
        self.coordinator_id = coordinator_id

    def add_competition(self, competition_name, organization_name, start_time, end_time):

    def edit_competition(self, competition_id, competition_name, organization_name, start_time, end_time):

    def remove_competition(self, competition_id):

    def add_team(self, competition_id, team_name, points, time_taken):

    def edit_team(self, competition_id, team_id, team_name, points, time_taken):
     
    def remove_team(self, team_id):

    def add_team_member(self, competition_id, team_id, user_id):
    
    def remove_team_member(self, competition_id, team_id, user_id):
     
    def get_json(self):
        return{
            'coordinator_id': self.coordinator_id,
            'organization_id': self.organization_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username
        }

    def repr():
        return f'<Coordinator {self.coordinator_id} : {self.first_name} {self.last_name} {self.username} - {self.email}>  