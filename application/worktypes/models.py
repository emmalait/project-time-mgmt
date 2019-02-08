from application import db
from application.models import Base

class WorkType(Base):
    
    name = db.Column(db.String(144), nullable=False)
    price = db.Column(db.Numeric(scale=2), nullable=False)

    timelogs = db.relationship("TimeLog", backref='work_type', lazy=True)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name