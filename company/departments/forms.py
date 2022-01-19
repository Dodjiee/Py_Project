"""
    Defines department forms for creating and deleting 
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,IntegerField
from wtforms.validators import DataRequired

class DepartmentForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Add')


class DelForm(FlaskForm):

    id = IntegerField('Id of Department to Remove:',  validators=[DataRequired()])
    submit = SubmitField('Remove Department')