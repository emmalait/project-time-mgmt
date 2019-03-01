from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, HiddenField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application import db

from flask_login import current_user

from application.worktypes.models import WorkType
from application.projects.models import Project

def work_type_choices():
    return WorkType.query.all()

def project_choices():
    return Project.find_projects_user_is_assigned_to(current_user.id)

class TimeLogForm(FlaskForm):
    hours = IntegerField("Hours")
    project = QuerySelectField("Project", query_factory = project_choices, get_label = "name")
    work_type = QuerySelectField("Work type", query_factory = work_type_choices, get_label = "name")
    description = StringField("Log description", [validators.Length(min=2, max=144, message="Log description must be between 2 and 144 characters.")])

    class Meta:
        csrf = False

class TimeLogEditForm(FlaskForm):
    id = HiddenField()
    hours = IntegerField("Hours")
    project = QuerySelectField("Project", query_factory = project_choices, get_label = "name")
    work_type = QuerySelectField("Work type", query_factory = work_type_choices, get_label = "name")
    description = StringField("Log description", [validators.Length(min=2, max=144, message="Log description must be between 2 and 144 characters.")])

    class Meta:
        csrf = False