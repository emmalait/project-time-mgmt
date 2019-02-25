## Installation guide

* [Download](https://github.com/emmalait/project-time-mgmt/archive/master.zip) Git repository
* Navigate to repository root and create virtual environment via command line: `python3 -m venv venv`
* Activate virtual environment: `source venv/bin/activate`
* Install project dependencies in the virtual environment: `pip install -r requirements.txt`
* Run app: `python3 run.py`
* Application is now running at <http://127.0.0.1:5000>

## User guide

### Registration
Using the app requires registration. To register, enter name, username and password.

### Employees
After logging in, a user with the role 'employee' can log time and view and edit their time logs. They can also view work types, customers and projects. They can view project-specific reports of their logged hours.

### Managers
After logging in, a user with the role 'manager' can perform all of the previously mentioned functions and in addition can edit work types, customers and projects and manage users' roles and salary data. 

### Roles
Users are given the role 'employee' by default when registering. Users with the role 'manager' can edit user roles.
