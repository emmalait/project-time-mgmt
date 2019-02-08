from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, HiddenField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application import db

from application.worktypes.models import WorkType

def work_type_choices():
        return WorkType.query.all()

class TimeLogForm(FlaskForm):
    hours = IntegerField("Hours")
    work_type = QuerySelectField(u"Work type", query_factory = work_type_choices)
    description = StringField("Log description", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False

class TimeLogEditForm(FlaskForm):
    id = HiddenField()
    hours = IntegerField("Hours")
    work_type = QuerySelectField(u"Work type", query_factory = work_type_choices)
    description = StringField("Log description", [validators.Length(min=2, max=144)])

    class Meta:
        csrf = False