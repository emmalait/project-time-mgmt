from flask_login import current_user

from application import db
from application.models import Base

from sqlalchemy import text

class Customer(Base):

    name = db.Column(db.String(144), nullable=False)
    business_id = db.Column(db.String(9), nullable=False)

    def __init__(self, name, business_id):
        self.name = name
        self.business_id = business_id