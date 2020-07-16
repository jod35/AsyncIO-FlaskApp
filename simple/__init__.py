from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from .config import DevConfig


#init app
app=Flask(__name__)

#config app
app.config.from_object(DevConfig)

#init db
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager=LoginManager(app)



from . import routes
from .models import User

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


