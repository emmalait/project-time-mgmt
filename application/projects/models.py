from flask_login import current_user

from application import db
from application.models import Base

from sqlalchemy import text

class Project(Base):

    name = db.Column(db.String(144), nullable=False)
    budget = db.Column(db.Numeric(scale=2), nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget