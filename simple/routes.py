from simple import app,db,bcrypt
import asyncio
from flask import render_template,request,url_for,redirect
from .models import User

#function to add to db session
def add_to_session(new_object):
    return db.session.add(new_object)


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

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method =='POST':
        username=request.form['username']
        email=request.form['email']
        password=bcrypt.generate_password_hash(request.form['password'])


        new_user=User(username=username,email=email,passwd_hash=password)

        async def main():
            db.session.add(new_user)
            await asyncio.sleep(1)
            db.session.commit()
            await asyncio.sleep(2)
            return redirect(url_for('login'))

        asyncio.run(main())
        
        

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

