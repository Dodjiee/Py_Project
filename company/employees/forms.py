"""
    Defines department forms for creating, deleting  and updating 
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,IntegerField, DateField
from wtforms.validators import DataRequired


class EmployeeForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    birthday = DateField('Birthdate', validators=[DataRequired()])
    post  = StringField('Job', validators = [DataRequired()]) 
    department_id = IntegerField('Number of department', validators= [DataRequired()])
    submit = SubmitField('Register')

class EmployeeDel(FlaskForm):

    name =  StringField('Name to fire:',  validators=[DataRequired()])
    submit = SubmitField('Fire Employee')


class UpdateEmployee(FlaskForm):
    name = StringField('Name')
    salary = IntegerField('Salary')
    post  = StringField('Job') 
    birthday = DateField('Birthdate')
    department_id = IntegerField('Number of department')
    submit = SubmitField('Update')