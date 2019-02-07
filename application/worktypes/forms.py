from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, validators

class WorkTypeForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=2)])
    price = DecimalField("Price", places=2)

    class Meta:
        csrf = False