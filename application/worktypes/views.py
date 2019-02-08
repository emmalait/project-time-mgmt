from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.worktypes.models import WorkType
from application.worktypes.forms import WorkTypeForm

@app.route("/worktypes", methods=["GET"])
def worktypes_index():
    return render_template("worktypes/list.html", worktypes = WorkType.query.all())

@app.route("/worktypes/new/")
@login_required
def worktypes_form():
    return render_template("worktypes/new.html", form = WorkTypeForm())

@app.route("/worktypes/<worktype_id>/", methods=["GET"])
@login_required
def worktype(worktype_id):
    wt = WorkType.query.filter_by(id = worktype_id).first()

#    t = TimeLog.query.get(timelog_id)
#    t.cleared = True
#    db.session().commit()
  
    return render_template("worktypes/view.html", worktype = wt)


@app.route("/worktypes/", methods=["POST"])
@login_required
def worktypes_create():
    form = WorkTypeForm(request.form)

    #if not form.validate():
    #    return render_template("worktypes/new.html", form = form)

    t = WorkType(form.name.data, form.price.data)
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("worktypes_index"))