from simple import app,db
from flask import render_template,request,url_for,redirect

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/profile')
def user_profile():
    return render_template('profile.html')

