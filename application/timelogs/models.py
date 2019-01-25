from application import db

class TimeLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    hours = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    cleared = db.Column(db.Boolean, nullable=False)

    def __init__(self, hours, description):
        self.hours = hours
        self.description = description
        self.cleared = False
        