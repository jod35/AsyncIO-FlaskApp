from simple import app,db
from flask import render_template,request,url_for,redirect

@app.route('/')
def index():

    context={
        'title':"Home Page"
    }
    return render_template('index.html',**context)

@app.route('/login')
def login():
    context={
        'title':"Login To Your Account"
    }
    return render_template('login.html',**context)

@app.route('/register')
def register():
    context={
        'title':"Create Your Account"
    }
    return render_template('signup.html',**context)

@app.route('/profile')
def user_profile():
    context={
        'title':"Your Profile"
    }
    return render_template('profile.html')

