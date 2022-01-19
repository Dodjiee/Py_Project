from flask import Blueprint,request,jsonify
from company.models.employee_models import Employee
from company.employees import views
api = Blueprint('api',__name__)

@api.route('/show_emp', methods=['GET'])
def index():
    employee = Employee()
    employees = views.show_emp()

    return employees.jsonify(employee).data

api.add