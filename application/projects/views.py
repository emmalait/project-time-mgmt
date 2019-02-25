from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.projects.models import Project
from application.projects.forms import ProjectForm
from application.customers.models import Customer
from application.timelogs.models import TimeLog

# Show all projects
@app.route("/projects", methods=["GET"])
@login_required
def projects_index():
    ps = Project.query.all()

    for project in ps:
        project.customer_name = Customer.query.filter_by(id = project.customer_id).first().name

    return render_template("projects/list.html", projects = ps)

# Create a new project
@app.route("/projects", methods=["POST"])
@login_required
def projects_create():
    form = ProjectForm(request.form)

    if not form.validate():
        return render_template("projects/new.html", form = form)

    p = Project(form.name.data, form.budget.data)
    p.customer_id = form.customer.data.id
    
    db.session().add(p)
    db.session().commit()
  
    return redirect(url_for("projects_index"))

# Show the form for creating a project
@app.route("/projects/new")
@login_required
def projects_form():
    return render_template("projects/new.html", form = ProjectForm())

# View a project
@app.route("/projects/<project_id>", methods=["GET"])
@login_required
def project(project_id):
    p = Project.query.filter_by(id = project_id).first()

    p.customer_name = Customer.query.filter_by(id = p.customer_id).first().name
    p.budget = float(str(p.budget))
    p.costs = float(str(Project.get_costs(project_id)))
    p.revenues = float(str(Project.get_revenues(project_id)))

    cleared_tls = TimeLog.find_cleared_timelogs_by_project(project_id)
    uncleared_tls = TimeLog.find_uncleared_timelogs_by_project(project_id)

    return render_template(
        "projects/view.html",
        project = p,
        cleared_timelogs = cleared_tls,
        uncleared_timelogs = uncleared_tls)