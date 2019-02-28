from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.worktypes.models import WorkType
from application.worktypes.forms import WorkTypeForm, WorkTypeEditForm

# Show all work types
@app.route("/worktypes", methods=["GET"])
@login_required
def worktypes_index():
    return render_template("worktypes/list.html", worktypes = WorkType.query.all())

# Create a new work type
@app.route("/worktypes", methods=["POST"])
@login_required
def worktypes_create():
    form = WorkTypeForm(request.form)

    wt = WorkType(form.name.data, form.price.data)

    if not form.validate():
        return render_template("worktypes/new.html", form = form)
    
    db.session().add(wt)
    db.session().commit()
  
    return redirect(url_for("worktypes_index"))

# Delete a work type
@app.route("/worktypes/<worktype_id>/delete", methods=["POST"])
@login_required
def worktypes_delete(worktype_id):
    wt = WorkType.query.filter_by(id = worktype_id).first()
    
    db.session().delete(wt)
    db.session().commit()
  
    return redirect(request.referrer)
    
# Show the form for creating a new work type
@app.route("/worktypes/new")
@login_required
def worktypes_form():
    return render_template("worktypes/new.html", form = WorkTypeForm())

# GET = show the edit form for a work type, POST = edit a work type
@app.route("/worktypes/<worktype_id>", methods=["GET", "POST"])
@login_required
def worktype(worktype_id):
    wt = WorkType.query.filter_by(id = worktype_id).first()

    if request.method == "GET":
        return render_template("worktypes/view.html", form = WorkTypeEditForm(obj=wt))

    form = WorkTypeEditForm(request.form)

    wt = WorkType.query.filter_by(id = form.id.data).first()

    if not form.validate():
        return render_template("worktypes/view.html", form = form)

    wt.name = form.name.data
    wt.price = form.price.data

    db.session().commit()
  
    return redirect(url_for("worktypes_index"))