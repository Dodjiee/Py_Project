"""
    defines department model
"""

from company import db

class Department(db.Model):

    
    """
    The class represents the model department
    Attributes :
    id: int - identification of department
    name: str - name of department
    employees: employees inside the department
    
    Function :
    _init__() : constructor of class
    __str__() : string representation of class
    """

    __tablename__ = 'departments'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    employees = db.relationship('Employee', cascade="all,delete", backref = db.backref('department'), lazy = True)

    
    def __init__(self, name):
        self.name = name

    
    def __repr__(self):
        return f'Department name : {self.name}'
       

