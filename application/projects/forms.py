from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from application import db

from application.customers.models import Customer

def customer_choices():
        return Customer.query.all()

class ProjectForm(FlaskForm):
    customer = QuerySelectField(u"Customer", query_factory = customer_choices)
    name = StringField("Name", [validators.Length(min=2, max=144)])
    budget = DecimalField("Budget", [validators.InputRequired], places=2)

    class Meta:
        csrf = False