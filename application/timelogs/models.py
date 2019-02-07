from application import db
from application.models import Base

class TimeLog(Base):

    hours = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    cleared = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    work_type_id = db.Column(db.Integer, db.ForeignKey('work_type.id'), nullable=False)
    

    def __init__(self, hours, description):
        self.hours = hours
        self.description = description
        self.cleared = False