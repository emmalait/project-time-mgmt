from flask_login import current_user

from application import db
from application.models import Base

from sqlalchemy import text

class TimeLog(Base):

    hours = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(144), nullable=False)
    cleared = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    work_type_id = db.Column(db.Integer, db.ForeignKey('work_type.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    
    def __init__(self, hours, description):
        self.hours = hours
        self.description = description
        self.cleared = False
    
    @staticmethod
    def find_users_logs_by_worktype(worktype_id):
        stmt = text("SELECT work_type.name, time_log.description, time_log.hours FROM time_log"
                    " LEFT JOIN account ON time_log.account_id = account.id"
                    " LEFT JOIN work_type ON time_log.work_type_id = work_type.id"
                    " WHERE work_type.id = " + str(worktype_id) + " AND account.id = " + str(current_user.id))
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"work_type":row[0], "description":row[1], "hours":row[2]})

        return response

    @staticmethod
    def find_worktypes_in_users_logs():
        stmt = text("SELECT work_type.id FROM time_log"
                    " LEFT JOIN account on time_log.account_id = account.id"
                    " LEFT JOIN work_type ON time_log.work_type_id = work_type.id"
                    " WHERE account.id = " + str(current_user.id))
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append(row[0])

        return response
    
    @staticmethod
    def find_cleared_timelogs_by_project(project_id):
        stmt = text("SELECT time_log.id, account.name, work_type.name, time_log.description, time_log.hours, time_log.cleared, account.id FROM time_log"
                        " LEFT JOIN project ON time_log.project_id = project.id"
                        " LEFT JOIN work_type ON time_log.work_type_id"
                        " LEFT JOIN account on time_log.account_id = account.id"
                        " WHERE project.id = " + str(project_id) + " AND time_log.cleared")

        res = db.engine.execute(stmt)
    
        response = []
        for row in res:
            response.append({
                "id": row[0],
                "user":row[1],
                "work_type":row[2],
                "description":row[3],
                "hours":row[4],
                "cleared":row[5],
                "user_id":row[6]
            })

        return response

    @staticmethod
    def find_uncleared_timelogs_by_project(project_id):
        stmt = text("SELECT time_log.id, account.name, work_type.name, time_log.description, time_log.hours, time_log.cleared, account.id FROM time_log"
                        " LEFT JOIN project ON time_log.project_id = project.id"
                        " LEFT JOIN work_type ON time_log.work_type_id"
                        " LEFT JOIN account on time_log.account_id = account.id"
                        " WHERE project.id = " + str(project_id) + " AND NOT time_log.cleared")

        res = db.engine.execute(stmt)
        
        response = []
        for row in res:
            response.append({
                "id": row[0],
                "user":row[1],
                "work_type":row[2],
                "description":row[3],
                "hours":row[4],
                "cleared":row[5],
                "user_id":row[6]
            })

        return response