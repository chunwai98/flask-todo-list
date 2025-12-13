from main.extensions import db,login_manager
from flask_login import UserMixin

class Users(db.Model,UserMixin):
    __tablename__="users"

    uid=db.Column(db.Integer, primary_key=True)
    userName=db.Column(db.String, nullable=False) 
    password=db.Column(db.String, nullable=False)
    
    def __repr__(self):
        return f"Uid:{self.uid} User:{self.userName}"
    
    def get_id(self):
        return self.uid
    
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)