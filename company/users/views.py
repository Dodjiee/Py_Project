"""
    Defines user web aplication view 
"""


from flask import render_template, url_for, redirect, Blueprint,request
from flask_login import login_user,current_user,logout_user,login_required
from company import db, app
from company.models.user_models import User
from company.users.forms import RegistrationForm, LoginForm

users = Blueprint('users', __name__)

@users.route('/logout')
def logout():
    """
    Make user to log out 
    Returns rendered template to show home page 
    """
    logout_user()
    return redirect(url_for('core.index'))


@app.route('/register', methods=['GET','POST'])
def register():
    """
    
    Returns rendered template to a registration form
    """

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email = form.email.data,
                    username= form.username.data,
                    password = form.password.data)
        
        db.session.add(user)
        db.session.commit()
       

        return redirect(url_for('users.login'))

    return render_template('register.html', form = form)


@users.route('/login',methods=['GET','POST'])
def login():
    """
    
    Returns rendered template to a login form

    """

    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            
            
            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            if next ==None or not next[0]=='/':
                next = url_for('core.index')

            return redirect(next)

    return render_template('login.html',form=form)