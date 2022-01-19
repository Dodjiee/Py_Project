"""
    Defines departments web aplication view 
"""
from wsgiref.handlers import format_date_time
from flask import render_template, url_for, redirect, Blueprint
from flask_login import current_user, login_required
from company import db, app, departments, employees
from company.models.department_models import Department
from company.departments.forms import DepartmentForm,DelForm
from company.models.employee_models import Employee

departments = Blueprint('departments', __name__)


@login_required
@departments.route('/create', methods = ['GET','POST'])
def create_dep():
    """
    Returns rendered template to create department
    :return rendered template to create department
    """
    form = DepartmentForm()

    if form.validate_on_submit():
        department = Department(name = form.name.data)

        db.session.add(department)
        db.session.commit()

        return redirect(url_for('core.index'))
    
    return render_template('create_dep.html', form = form)

@departments.route('/show') 
def show_dep():
    """
    Returns rendered template to show all departments
    :return rendered template to show all departments

    """

    departments = Department.query.all()
    return render_template('departments.html', departments = departments)



@departments.route('/<int:department_id>/update', methods = ['GET','POST'])
@login_required
def update():
    """
    Returns rendered template to update form for department
    :return rendered template to update form for department
    """
    form = DepartmentForm()

    if form.validate_on_submit():

        departments.name  = form.name.data

        db.session.commit()

        return redirect(url_for('departments.department', department_id = departments.id))


    return render_template('create_dep.html', form = form)


@departments.route('/delete', methods = ['GET','POST'])
@login_required
def delete_dep():
    """
    Returns rendered template to delete department
    :return rendered template to delete department


    """
    form = DelForm()
    
    if form.validate_on_submit():
        id = form.id.data
        department = Department.query.get(id)
        db.session.delete(department)
        db.session.commit()

        return redirect(url_for('departments.show_dep'))
    return render_template('delete_dep.html',form=form)

