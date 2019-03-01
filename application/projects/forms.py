from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, HiddenField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application import db

from application.customers.models import Customer

def customer_choices():
        return Customer.query.all()

class ProjectForm(FlaskForm):
    customer = QuerySelectField("Customer", query_factory = customer_choices, get_label = "name")
    name = StringField("Name", [validators.Length(min=2, max=144, message="Name must be between 2-144 characters.")])
    budget = DecimalField("Budget", [validators.NumberRange(min=0, max=9000000000, message="Budget must be between 0.00-9 000 000 000.00 euros.")], places=2)

    class Meta:
        csrf = False

class ProjectEditForm(FlaskForm):
    id = HiddenField()
    customer = QuerySelectField("Customer", query_factory = customer_choices, get_label = "name")
    name = StringField("Name", [validators.Length(min=2, max=144, message="Name must be between 2-144 characters.")])
    budget = DecimalField("Budget", [validators.NumberRange(min=0, max=9000000000, message="Budget must be between 0.00-9 000 000 000.00 euros.")], places=2)

    class Meta:
        csrf = False