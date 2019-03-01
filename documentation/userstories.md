# User stories

### In production
* As an employee/manager I want to view a summary of my projects and recent time logs so that I know what I should be working on and where I left off.


```python
def find_projects_user_is_assigned_to(account_id)
```

```sql
SELECT project.id, project.name, project.budget, project.customer_id FROM project
  LEFT JOIN project_members ON project.id = project_members.project_id
  LEFT JOIN account ON project_members.account_id = account.id
  WHERE account.id = account_id;
```

* As an employee/manager I want to record my hours by project and work type so that I can track my hours.
* As an employee/manager I want to view my time logs so that I can be sure I logged everything.
* As an employee/manager I want to edit my logged hours so that I can fix any errors.
* As an employee/manager I want to view and add customers, projects and work types so that I can log my hours even if some data has not yet been entered.
* As an employee/manager I want to view project entries by project so that I can get a bigger picture of who is doing what.
* As an employee I want to view project entries by project and by invoicing status so that I know what project entries have been approved for invoicing by the project manager.
* As a manager I want to view project entries by project and by invoicing status so that I know what data counts towards costs and revenues.

```python
def find_cleared_timelogs_by_project(project_id)
```

Version for Heroku:
```sql
SELECT time_log.id, account.name, work_type.name, time_log.description, time_log.hours, time_log.cleared, account.id FROM time_log
  LEFT JOIN project ON time_log.project_id = project.id
  LEFT JOIN work_type ON time_log.work_type_id = work_type.id
  LEFT JOIN account on time_log.account_id = account.id
  WHERE project.id = project_id AND time_log.cleared = 't';
```

Version for Sqlite:
```sql
SELECT time_log.id, account.name, work_type.name, time_log.description, time_log.hours, time_log.cleared, account.id FROM time_log
  LEFT JOIN project ON time_log.project_id = project.id
  LEFT JOIN work_type ON time_log.work_type_id = work_type.id
  LEFT JOIN account on time_log.account_id = account.id
  WHERE project.id = project_id AND time_log.cleared = 1;
```

```python
def find_uncleared_timelogs_by_project(project_id)
```

Version for Heroku:
```sql
SELECT time_log.id, account.name, work_type.name, time_log.description, time_log.hours, time_log.cleared, account.id FROM time_log
  LEFT JOIN project ON time_log.project_id = project.id
  LEFT JOIN work_type ON time_log.work_type_id = work_type.id
  LEFT JOIN account on time_log.account_id = account.id
  WHERE project.id = project_id AND time_log.cleared = 'f';
```

Version for Sqlite:
```sql
SELECT time_log.id, account.name, work_type.name, time_log.description, time_log.hours, time_log.cleared, account.id FROM time_log
  LEFT JOIN project ON time_log.project_id = project.id
  LEFT JOIN work_type ON time_log.work_type_id = work_type.id
  LEFT JOIN account on time_log.account_id = account.id
  WHERE project.id = project_id AND time_log.cleared = 0;
```

* As a manager I want to manage users' roles so that I can change users' roles when e.g. personnel changes occur.
* As a manager I want to manage users' salary data so that I can get cost data for projects.
* As a manager I want to mark project entries as invoiced so that the entries are calculated into the costs and revenues for the project.
* As a manager I want to find out the accrued costs of a project so that I can follow how it meets its budget.
```python
def get_costs(project_id)
```

Version for Heroku:
```sql
SELECT SUM(time_log.hours * account.salary) FROM project
  LEFT JOIN time_log ON project.id = time_log.project_id
  LEFT JOIN account ON time_log.account_id = account.id
  WHERE project.id = project_id AND time_log.cleared = 't';
``` 

Version for Sqlite:
```sql
SELECT SUM(time_log.hours * account.salary) FROM project
  LEFT JOIN time_log ON project.id = time_log.project_id
  LEFT JOIN account ON time_log.account_id = account.id
  WHERE project.id = project_id AND time_log.cleared = 1;
``` 
* As a manager I want to find out the revenues of a project so that I can get data for the project's profitability.
```python
def get_revenues(project_id)
```

Version for Heroku:
```sql
SELECT SUM(time_log.hours * work_type.price) FROM project
  LEFT JOIN time_log ON project.id = time_log.project_id
  LEFT JOIN work_type ON time_log.work_type_id = work_type.id
  WHERE project.id = project_id) AND time_log.cleared = 't';
```

Version for Sqlite:
```sql
SELECT SUM(time_log.hours * work_type.price) FROM project
  LEFT JOIN time_log ON project.id = time_log.project_id
  LEFT JOIN work_type ON time_log.work_type_id = work_type.id
  WHERE project.id = project_id AND time_log.cleared = 1;
```

* As a manager I want to find out the gross profit of a project so that I can follow its profitability.
* As a manager I want to assign users to projects so that the composition of the project team is visible to everyone.
```python
def find_users_not_assigned_to_project(project_id)
```

```sql
SELECT account.id, account.name FROM account
  LEFT JOIN project_members ON project_members.account_id = account.id
  LEFT JOIN project ON project.id = project_members.project_id
  WHERE NOT project.id = project_id OR project_members.account_id IS NULL;
```   

### Backlog
* As a manager I want to assign (a) project manager(s) to each project so that the composition of the project team is visible to everyone.
