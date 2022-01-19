
"""
    Defines user forms 
"""

from company.models.user_models import User
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError

from flask_login import current_user


class LoginForm(FlaskForm):
    """
        Login form for user 
    """
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    """
        Registration form for user 
    """
    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo('pass_confirm', message='Passwords not the same')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')


    def validate_email(self, email):
        """
        raise error if email is registered already 
        """
    
        if User.query.filter_by(email =self.email.data).first():
            raise ValidationError('The selected email is already in use')

    def validate_username(self, username):
        if User.query.filter_by(username =self.username.data).first():
            raise ValidationError('The selected username is already taken')