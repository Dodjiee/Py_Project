"""
    Defines employee model
"""

from company import db
from company.models.department_models import Department
from datetime import date 

today = date.today().year

class Employee(db.Model):

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
    """

    id = db.Column(db.Integer,primary_key=True)

    department_id = db.Column(db.Integer,db.ForeignKey('departments.id'),nullable=False)

    name = db.Column(db.String(64), nullable=False)
    salary = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    post = db.Column(db.String(length=64))

    def __init__(self,name,salary,birthday,post,department_id):

        self.name = name
        self.salary = salary
        self.birthday = birthday
        self.post = post 
        self.department_id = department_id
    
    def __repr__(self):
        return f' Name : {self.name}, Current job : {self.post}, Salary: {self.salary}, Age : {today - self.birthday.year}, Department: {self.department_id}'


    