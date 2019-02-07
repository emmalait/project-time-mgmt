from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, validators

class TimeLogForm(FlaskForm):
    hours = IntegerField("Hours")
    description = StringField("Log description", [validators.Length(min=2)])

    class Meta:
        csrf = False