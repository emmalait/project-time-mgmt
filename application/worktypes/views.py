from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.worktypes.models import WorkType
from application.worktypes.forms import WorkTypeForm

# Show all work types
@app.route("/worktypes", methods=["GET"])
def worktypes_index():
    return render_template("worktypes/list.html", worktypes = WorkType.query.all())

# Create a new work type
@app.route("/worktypes", methods=["POST"])
@login_required
def worktypes_create():
    form = WorkTypeForm(request.form)

    t = WorkType(form.name.data, form.price.data)

    if not form.validate():
        return render_template("worktypes/new.html", form = form)
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("worktypes_index"))
    
# Show the form for creating a new work type
@app.route("/worktypes/new")
@login_required
def worktypes_form():
    return render_template("worktypes/new.html", form = WorkTypeForm())

# View a work type
@app.route("/worktypes/<worktype_id>", methods=["GET"])
@login_required
def worktype(worktype_id):
    wt = WorkType.query.filter_by(id = worktype_id).first()
  
    return render_template("worktypes/view.html", worktype = wt)