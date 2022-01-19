"""
    Defines departments web aplication view 
"""
from flask import render_template, url_for, redirect, Blueprint,request
from flask_login import current_user, login_required
from company import db, app, departments
from company.models.department_models import Department
from company.models.employee_models import Employee
from company.employees.forms import EmployeeDel, EmployeeForm, UpdateEmployee

employees = Blueprint('employees', __name__)


@employees.route('/add', methods = ['GET','POST'])
def add_employee():
    """
        Returns render template for creating employee
        :return: rendered template to create employee

    """

    form = EmployeeForm()

    if form.validate_on_submit():
        employee = Employee(name = form.name.data,
                            salary = form.salary.data,
                            birthday = form.birthday.data,
                            post = form.post.data,
                            department_id = form.department_id.data)

        db.session.add(employee)
        db.session.commit()
        return redirect(url_for('employees.show_emp'))
    
    return render_template('employees.html', form = form)


@employees.route('/delete_emp', methods = ['GET','POST'])
@login_required
def delete_emp():
    """
        Returns render template for deleting employee
        :return: rendered template to deleting employee

    """
    form = EmployeeDel()
    
    if form.validate_on_submit():
        name = form.name.data
        employee = Employee.query.filter_by(name = form.name.data).first()
        db.session.delete(employee)
        db.session.commit()

        return redirect(url_for('employees.show_emp'))
    return render_template('delete_emp.html',form=form)

@employees.route('/show_emp') 
def show_emp():
    """
        Returns render template to list of employees
        :return: rendered template to  list of employees

    """
    employees = Employee.query.all()
    return render_template('employee_list.html', employees = employees)


@employees.route('/<int:employee_id>/update_emp', methods= ['GET', 'POST'])
def update_emp(employee_id):

    """
        Returns render template to update employee data
        :param employee_id : employee id
        :return: rendered template to  update employee data
    """
   
    employee = Employee.query.get_or_404(employee_id)
    db.session.delete(employee)
    form = UpdateEmployee()
    if form.validate_on_submit():
        employee = Employee(name = form.name.data,
                            salary = form.salary.data,
                            birthday = form.birthday.data,
                            post = form.post.data,
                            department_id = form.department_id.data)
        db.session.add(employee)
        db.session.commit()

        return redirect(url_for('employees.show_emp', employee_id = employee.id, form = form))

    elif request.method == 'GET':
         form.name.data = employee.name
         form.salary.data = employee.salary
         form.post.data = employee.post
         form.department_id.data = employee.department_id

            
    return render_template('update_emp.html',form=form)

@employees.route('/<int:employee_id>/')
def one_emp(employee_id):
    
    """
        Returns render template to information about chosen employee
        :param employee_id : employee id
        :return: rendered template to information about chosen employee
    """
   
    one_emp = Employee.query.get_or_404(employee_id)
    return render_template('one_emp.html', employee = one_emp)


