from flask import render_template
from application import app
from flask_login import login_required

@app.route("/")
@login_required
def index():
    return render_template("index.html")