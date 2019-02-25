from flask_login import current_user

from application import db
from application.models import Base

from sqlalchemy import text

import os

class Project(Base):

    name = db.Column(db.String(144), nullable=False)
    budget = db.Column(db.Numeric(scale=2), nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    def __init__(self, name, budget):
        self.name = name
        self.budget = budget
    
    @staticmethod
    def get_costs(project_id):
        if os.environ.get("HEROKU"):
            stmt = text("SELECT SUM(time_log.hours * account.salary) FROM project"
                        " LEFT JOIN time_log ON project.id = time_log.project_id"
                        " LEFT JOIN account on time_log.account_id = account.id"
                        " WHERE project.id = " + str(project_id) + " AND time_log.cleared = " + True)
        else:
            stmt = text("SELECT SUM(time_log.hours * account.salary) FROM project"
                            " LEFT JOIN time_log ON project.id = time_log.project_id"
                            " LEFT JOIN account on time_log.account_id = account.id"
                            " WHERE project.id = " + str(project_id) + " AND time_log.cleared = 1")

        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({
                "costs": row[0]
            })

        costs = response[0].get("costs")

        return costs
    
    @staticmethod
    def get_revenues(project_id):
        if os.environ.get("HEROKU"):
            stmt = text("SELECT SUM(time_log.hours * work_type.price) FROM project"
                            " LEFT JOIN time_log ON project.id =time_log.project_id"
                            " LEFT JOIN work_type ON time_log.work_type_id"
                            " WHERE project.id = " + str(project_id) + " AND time_log.cleared = " + True)
        else:
            stmt = text("SELECT SUM(time_log.hours * work_type.price) FROM project"
                        " LEFT JOIN time_log ON project.id =time_log.project_id"
                        " LEFT JOIN work_type ON time_log.work_type_id"
                        " WHERE project.id = " + str(project_id) + " AND time_log.cleared = 1")

        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({
                "revenues": row[0]
            })

        revenues = response[0].get("revenues")

        return revenues