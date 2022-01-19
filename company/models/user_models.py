"""
    defines user model
"""

from company import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

""" By inheriting the UserMixin we get access to a lot of built-in attributes
 which we will be able to call in our views!
 is_authenticated()
 get_id()
"""


class User(db.Model, UserMixin):
    """
    The class represents the model employee
    Attributes :
    id: int - identification of employee
    name: str - name of employee
  
    birthday: date - when employee was born
    salary: int - how much employee get in cash
    department_id: int - identification for department (made for ForeignKey relation)
    
    Function :
    _init__() : constructor of class
    __str__() : string representation of class
    check_password(): return if password_hash match password
    """


    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(64),unique = True, index = True)
    username = db.Column(db.String(64),unique = True, index = True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    
    def __repr__(self):
        return f"Username: {self.username}, Email: {self.email}"