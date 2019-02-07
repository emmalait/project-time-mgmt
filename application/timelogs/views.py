from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.timelogs.models import TimeLog
from application.timelogs.forms import TimeLogForm

@app.route("/timelogs", methods=["GET"])
@login_required
def timelogs_index():
    return render_template("timelogs/list.html", timelogs = TimeLog.query.all())

@app.route("/timelogs/new/")
@login_required
def timelogs_form():
    return render_template("timelogs/new.html", form = TimeLogForm())

@app.route("/timelogs/<timelog_id>/", methods=["POST"])
@login_required
def timelogs_set_cleared(timelog_id):
    t = TimeLog.query.get(timelog_id)
    t.cleared = True
    db.session().commit()
  
    return redirect(url_for("timelogs_index"))

@app.route("/timelogs/", methods=["POST"])
@login_required
def timelogs_create():
    form = TimeLogForm(request.form)

    if not form.validate():
        return render_template("timelogs/new.html", form = form)

    t = TimeLog(form.hours.data, form.description.data)
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("timelogs_index"))