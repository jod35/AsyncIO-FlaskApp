from simple import db
from flask_login import UserMixin
from simple import login_manager

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    passwd_hash=db.Column(db.Text,nullable=False)


    def __init__(self,username,email,passwd_hash):
        self.username=username
        self.email=email
        self.passwd_hash=passwd_hash


    def __repr__(self):
        return f"{self.username}'s account"




