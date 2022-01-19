"""
    Defines main page web aplication view 
"""

from flask import render_template,request,Blueprint

from company.departments.views import departments

core = Blueprint('core',__name__)

@core.route('/')
def index():
    """
    Returns rendered template to show home page 
    """
    return render_template('index.html', departments = departments)


