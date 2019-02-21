from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm, UserEditForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())
    
    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "No such username or password")

    login_user(user)
    return redirect(url_for("timelogs_index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("auth_login"))

@app.route("/auth/register", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/register.html", form = RegisterForm())

    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form = form)

    t = User(form.name.data, form.username.data, form.password.data)
    
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("auth_login"))

# Show all users
@app.route("/auth", methods=["GET"])
@login_required(role="manager")
def users_index():
    return render_template("auth/list.html", users = User.query.all())

# GET = show the edit form for a user, POST = update a user
@app.route("/auth/<user_id>", methods=["GET", "POST"])
@login_required(role="manager")
def user(user_id):
    u = User.query.filter_by(id = user_id).first()

    if request.method == "GET":
        return render_template("auth/view.html", form = UserEditForm(obj=u) )

    form = UserEditForm(request.form)

    u = User.query.filter_by(id = form.id.data).first()

    if not form.validate():
        return render_template("auth/view.html", form = form)

    u.salary = form.salary.data
    u.role = form.role.data

    db.session().commit()
  
    return redirect(url_for("users_index"))