from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    role = db.Column(db.String(144), nullable=True)
    salary = db.Column(db.Numeric(scale=2), nullable=False)

    timelogs = db.relationship("TimeLog", backref='account', lazy=True)

    def __init__(self, name, username, password, role):
        self.name = name
        self.username = username
        self.password = password
        self.role = role
        self.salary = 0

    def get_id(self):
        return self.id

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True
    
    @staticmethod
    def find_users_with_no_logs():
        stmt = text("SELECT account.id, account.name FROM account"
                    " LEFT JOIN time_log ON time_log.account_id = account.id"
                    " GROUP BY account.id"
                    " HAVING COUNT(time_log.id) = 0;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        
        return response
    
    @staticmethod
    def find_users_not_assigned_to_project(project_id):
        stmt = text("SELECT account.id, account.name FROM account"
                    " LEFT JOIN project_members ON project_members.account_id = account.id"
                    " LEFT JOIN project ON project.id = project_members.project_id"
                    " WHERE NOT project.id = :project_id OR project_members.account_id IS NULL").params(project_id = project_id)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})
        
        return response