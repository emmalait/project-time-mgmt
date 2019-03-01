from flask import render_template
from application import app
from flask_login import login_required, current_user

from application.projects.models import Project
from application.timelogs.models import TimeLog
from application.customers.models import Customer
from application.worktypes.models import WorkType

@app.route("/")
@login_required
def index():
    projects = Project.find_projects_user_is_assigned_to(current_user.id)

    for project in projects:
        project.customer_name = Customer.query.filter_by(id = project.customer_id).first().name
        project.budget = float(str(project.budget))
        project.costs = Project.get_costs(project.id)
        project.revenues = Project.get_revenues(project.id)
    
    timelogs = TimeLog.query.filter_by(account_id = current_user.id).order_by(TimeLog.date_created.desc()).limit(5).all()

    for timelog in timelogs:
        timelog.customer_name = Customer.query.filter_by(id = Project.query.filter_by(id = timelog.project_id).first().customer_id).first().name
        timelog.project_name = Project.query.filter_by(id = timelog.project_id).first().name
        timelog.work_type_name = WorkType.query.filter_by(id = timelog.work_type_id).first().name

    return render_template("index.html", projects = projects, timelogs = timelogs)