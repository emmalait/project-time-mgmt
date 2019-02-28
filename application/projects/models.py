from flask_login import current_user

from application import db
from application.models import Base

from sqlalchemy import text

import os

ProjectMembers = db.Table('project_members',
    db.Column('account_id', db.Integer, db.ForeignKey('account.id')),
    db.Column('project_id', db.Integer, db.ForeignKey('project.id'))
)

class Project(Base):

    name = db.Column(db.String(144), nullable=False)
    budget = db.Column(db.Numeric(scale=2), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    members = db.relationship('User', secondary=ProjectMembers, backref='projects', lazy=True)

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    
    @staticmethod
    def get_costs(project_id):
        # Use a different version of the query for Heroku because of PostgreSQL's boolean handling
        if os.environ.get("HEROKU"):
            stmt = text("SELECT SUM(time_log.hours * account.salary) FROM project"
                            " LEFT JOIN time_log ON project.id = time_log.project_id"
                            " LEFT JOIN account ON time_log.account_id = account.id"
                            " WHERE project.id = :project_id AND time_log.cleared = 't'").params(project_id = project_id)
        else:
            stmt = text("SELECT SUM(time_log.hours * account.salary) FROM project"
                            " LEFT JOIN time_log ON project.id = time_log.project_id"
                            " LEFT JOIN account ON time_log.account_id = account.id"
                            " WHERE project.id = :project_id AND time_log.cleared = 1").params(project_id = project_id)

        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({
                "costs": row[0]
            })

        costs = response[0].get("costs")

        if costs:
            costs = float(str(costs))
        else:
            costs = float(str(0))

        return costs
    
    @staticmethod
    def get_revenues(project_id):
        # Use a different version of the query for Heroku because of PostgreSQL's boolean handling
        if os.environ.get("HEROKU"):
            stmt = text("SELECT SUM(time_log.hours * work_type.price) FROM project"
                            " LEFT JOIN time_log ON project.id = time_log.project_id"
                            " LEFT JOIN work_type ON time_log.work_type_id = work_type.id"
                            " WHERE project.id = :project_id) AND time_log.cleared = 't'").params(project_id = project_id)
        else:
            stmt = text("SELECT SUM(time_log.hours * work_type.price) FROM project"
                        " LEFT JOIN time_log ON project.id = time_log.project_id"
                        " LEFT JOIN work_type ON time_log.work_type_id = work_type.id"
                        " WHERE project.id = :project_id AND time_log.cleared = 1").params(project_id = project_id)

        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({
                "revenues": row[0]
            })

        revenues = response[0].get("revenues")

        if revenues:
            revenues = float(str(revenues))
        else:
            revenues = float(str(0))

        return revenues