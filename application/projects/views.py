from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db

from application.auth.models import User
from application.projects.models import Project
from application.projects.forms import ProjectForm, ProjectEditForm
from application.customers.models import Customer
from application.timelogs.models import TimeLog

# Show all projects
@app.route("/projects", methods=["GET"])
@login_required
def projects_index():
    ps = Project.query.all()

    for project in ps:
        project.customer_name = Customer.query.filter_by(id = project.customer_id).first().name
        project.budget = float(str(project.budget))
        project.costs = Project.get_costs(project.id)
        project.revenues = Project.get_revenues(project.id)

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
    p.costs = Project.get_costs(project_id)
    p.revenues = Project.get_revenues(project_id)

    cleared_tls = TimeLog.find_cleared_timelogs_by_project(project_id)
    uncleared_tls = TimeLog.find_uncleared_timelogs_by_project(project_id)

    return render_template(
        "projects/view.html",
        project = p,
        cleared_timelogs = cleared_tls,
        uncleared_timelogs = uncleared_tls)

# GET = view a project's edit form, POST = edit project
@app.route("/projects/<project_id>/edit", methods=["GET", "POST"])
@login_required
def edit_project(project_id):
    p = Project.query.filter_by(id = project_id).first()
    c = Customer.query.filter_by(id = p.customer_id).first()
    
    if request.method == "GET":
        editForm = ProjectEditForm(
            id = p.id,
            customer = c,
            name = p.name,
            budget = p.budget
        )
        return render_template("projects/edit.html", form = editForm) 

    form = ProjectEditForm(request.form)

    p = Project.query.filter_by(id = form.id.data).first()

    if not form.validate():
        return render_template("projects/view.html", form = form)

    p.customer_id = form.customer.data.id
    p.name = form.name.data
    p.budget = form.budget.data

    db.session().commit()
  
    return redirect(url_for("project", project_id = p.id))

# View page to assign users to a project
@app.route("/projects/<project_id>/members", methods=["GET"])
@login_required
def assignedUsers(project_id):
    p = Project.query.filter_by(id = project_id).first()
    availableUsers = User.find_users_not_assigned_to_project(project_id)

    return render_template("projects/assignedUsers.html", project = p, availableUsers = availableUsers)

# Assign user to a project
@app.route("/projects/<project_id>/members/<account_id>/assign", methods=["POST"])
@login_required
def assignUser(project_id, account_id):
    p = Project.query.filter_by(id = project_id).first()
    p.members.append(User.query.get(account_id))

    db.session().commit()

    return redirect(request.referrer)

# Unassign user to a project
@app.route("/projects/<project_id>/members/<account_id>/unassign", methods=["POST"])
@login_required
def unassignUser(project_id, account_id):

    p = Project.query.filter_by(id = project_id).first()
    p.members.remove(User.query.get(account_id))

    db.session().commit()

    return redirect(request.referrer)