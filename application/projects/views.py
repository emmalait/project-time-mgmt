from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.projects.models import Project
from application.projects.forms import ProjectForm
from application.customers.models import Customer

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

    #if not form.validate():
    #    return render_template("projects/new.html", form = form)

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