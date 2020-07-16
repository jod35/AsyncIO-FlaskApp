from simple import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(25),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    passwd_hash=db.Column(db.Text,nullable=False)


    def __init__(self,username,email,passwd_hash):
        self.username=username
        self.email=email
        self.passwd_hash=password


    def __repr__(self):
        return f"{self.usernames}'s account"