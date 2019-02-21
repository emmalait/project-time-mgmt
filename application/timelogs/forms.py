from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, HiddenField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application import db

from application.worktypes.models import WorkType
from application.projects.models import Project

def work_type_choices():
    return WorkType.query.all()

def project_choices():
    return Project.query.all()

class TimeLogForm(FlaskForm):
    hours = IntegerField("Hours")
    project = QuerySelectField("Project", query_factory = project_choices, get_label = "name")
    work_type = QuerySelectField("Work type", query_factory = work_type_choices, get_label = "name")
    description = StringField("Log description", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False

class TimeLogEditForm(FlaskForm):
    id = HiddenField()
    hours = IntegerField("Hours")
    project = QuerySelectField("Project", query_factory = project_choices, get_label = "name")
    work_type = QuerySelectField("Work type", query_factory = work_type_choices, get_label = "name")
    description = StringField("Log description", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False