from simple import app,db,bcrypt
import asyncio
from flask import render_template,request,url_for,redirect
from .models import User
from flask_login import login_user,current_user,logout_user

#function to add to db session
def add_to_session(new_object):
    return db.session.add(new_object)


@app.route('/')
def index():

    context={
        'title':"Home Page"
    }
    return render_template('index.html',**context)


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.passwd_hash,password):
            async def main():
                login_user(user)
                await asyncio.sleep(3)
                print("User is logged IN")
            asyncio.run(main())
            return redirect(url_for('user_profile'))
    context={
        'title':"Login To Your Account"
    }
    return render_template('login.html',**context)

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method== 'POST':
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        passwd_hash=bcrypt.generate_password_hash(password)


        new_user=User(username=username,email=email,passwd_hash=passwd_hash)    

        async def main():
            db.session.add(new_user)
            await asyncio.sleep(3)
            db.session.commit()
        asyncio.run(main())

        return redirect(url_for('login'))

    context={
        'title':"Create Your Account"
    }
    return render_template('signup.html',**context)


@app.route('/logout')
def logout():
    logout_user()
    return redirect("/")

@app.route('/profile')
def user_profile():
    context={
        'title':"Your Profile"
    }
    return render_template('profile.html')

