from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, HiddenField, validators

class WorkTypeForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2, max=144, message="Name must be between 2-144 characters.")])
    price = DecimalField("Price", [validators.NumberRange(min=0, max=10000, message="Price must be between 0.00-1000.00 euros.")], places=2)

    class Meta:
        csrf = False

class WorkTypeEditForm(FlaskForm):
    id = HiddenField()
    name = StringField("Name", [validators.Length(min=2, max=144, message="Name must be between 2-144 characters.")])
    price = DecimalField("Price", [validators.NumberRange(min=0, max=10000, message="Price must be between 0.00-1000.00 euros.")], places=2)

    class Meta:
        csrf = False