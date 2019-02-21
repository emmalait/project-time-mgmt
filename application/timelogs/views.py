from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.timelogs.models import TimeLog
from application.timelogs.forms import TimeLogForm, TimeLogEditForm
from application.worktypes.models import WorkType

# Show all time logs by the logged in user
@app.route("/timelogs", methods=["GET"])
@login_required
def timelogs_index():
    logs = TimeLog.query.filter_by(account_id = current_user.id).all()

    for timelog in logs:
        timelog.work_type_name = WorkType.query.filter_by(id = timelog.work_type_id).first()

    return render_template("timelogs/list.html", timelogs = logs)

# Create a new time log for the logged in user
@app.route("/timelogs", methods=["POST"])
@login_required
def timelogs_create():
    form = TimeLogForm(request.form)

    if not form.validate():
        return render_template("timelogs/new.html", form = form)

    t = TimeLog(form.hours.data, form.description.data)
    t.account_id = current_user.id
    t.work_type_id = form.work_type.data.id
    # t.project_id = form.project.data.id
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("timelogs_index"))

# Show the form for creating a new time log
@app.route("/timelogs/new")
@login_required
def timelogs_form():
    return render_template("timelogs/new.html", form = TimeLogForm())

# GET = show the edit form for a time log, POST = edit a time log
@app.route("/timelogs/<timelog_id>", methods=["GET", "POST"])
@login_required
def timelog(timelog_id):
    t = TimeLog.query.filter_by(id = timelog_id).first()

    if request.method == "GET":
        return render_template("timelogs/view.html", form = TimeLogEditForm(obj=t) )

    form = TimeLogEditForm(request.form)

    t = TimeLog.query.filter_by(id = form.id.data).first()

    if not form.validate():
        return render_template("timelogs/new.html", form = form)

    t.work_type_id = form.work_type.data.id
    t.description = form.description.data
    t.hours = form.hours.data

    db.session().commit()
  
    return redirect(url_for("timelogs_index"))

# Delete a time log
@app.route("/timelogs/<timelog_id>/delete", methods=["POST"])
@login_required
def timelogs_delete(timelog_id):
    t = TimeLog.query.filter_by(id = timelog_id).first()
    
    db.session().delete(t)
    db.session().commit()
  
    return redirect(url_for("timelogs_index"))