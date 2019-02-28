from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, validators

class CustomerForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144)])
    business_id = StringField("Business ID", [validators.Length(min=9, max=9)])

    class Meta:
        csrf = False

class CustomerEditForm(FlaskForm):
    id = HiddenField()
    name = StringField("Name", [validators.Length(min=2, max=144)])
    business_id = StringField("Business ID", [validators.Length(min=9, max=9)])

    class Meta:
        csrf = False