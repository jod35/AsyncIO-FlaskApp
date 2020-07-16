from simple import app,db
from flask import render_template,request,url_for,redirect

@app.route('/')
def hello():
    return "Hello"