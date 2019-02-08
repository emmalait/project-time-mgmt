from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.timelogs.models import TimeLog
from application.timelogs.forms import TimeLogForm
from application.worktypes.models import WorkType

@app.route("/timelogs", methods=["GET"])
@login_required
def timelogs_index():
    logs = TimeLog.query.filter_by(account_id = current_user.id).all()
    
    for timelog in logs:
        timelog.work_type_name = WorkType.query.filter_by(id = timelog.work_type_id).first()
    return render_template("timelogs/list.html", timelogs = logs)

@app.route("/timelogs/new/")
@login_required
def timelogs_form():
    return render_template("timelogs/new.html", form = TimeLogForm())

@app.route("/timelogs/<timelog_id>/", methods=["GET", "POST"])
@login_required
def timelog(timelog_id):
    if request.method == "GET":
        tl = TimeLog.query.filter_by(id = timelog_id).first()

#       t = TimeLog.query.get(timelog_id)
#       t.cleared = True
#       db.session().commit()
  
        return render_template("timelogs/view.html", timelog = tl)

    t = TimeLog.query.get(timelog_id)
    t.cleared = True
    db.session().commit()
  
    return render_template("timelogs/view.html", timelog = tl)

@app.route("/timelogs/", methods=["POST"])
@login_required
def timelogs_create():
    form = TimeLogForm(request.form)

    if not form.validate():
        return render_template("timelogs/new.html", form = form)

    t = TimeLog(form.hours.data, form.description.data)
    t.account_id = current_user.id
    t.work_type_id = form.work_type.data.id
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("timelogs_index"))