from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, validators

class CustomerForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144, message="Name must be between 2-144 characters.")])
    business_id = StringField("Business ID", [validators.Length(min=9, max=9, message="Business ID must be 9 characters (e.g. 1234567-8).")])

    class Meta:
        csrf = False

class CustomerEditForm(FlaskForm):
    id = HiddenField()
    name = StringField("Name", [validators.Length(min=2, max=144, message="Name must be between 2-144 characters.")])
    business_id = StringField("Business ID", [validators.Length(min=9, max=9, message="Business ID must be 9 characters (e.g. 1234567-8).")])

    class Meta:
        csrf = False