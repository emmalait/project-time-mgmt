from application import app, db
from flask import redirect, render_template, request, url_for
from application.timelogs.models import TimeLog

@app.route("/timelogs", methods=["GET"])
def timelogs_index():
    return render_template("timelogs/list.html", timelogs = TimeLog.query.all())

@app.route("/timelogs/new/")
def timelogs_form():
    return render_template("timelogs/new.html")

@app.route("/timelogs/<timelog_id>/", methods=["POST"])
def timelogs_set_cleared(timelog_id):

    t = TimeLog.query.get(timelog_id)
    t.cleared = True
    db.session().commit()
  
    return redirect(url_for("timelogs_index"))

@app.route("/timelogs/", methods=["POST"])
def timelogs_create():
    t = TimeLog(request.form.get("hours"), request.form.get("description"))
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("timelogs_index"))