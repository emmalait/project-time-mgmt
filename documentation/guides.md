## Installation guide

Before installation, you should install [Python 3](https://www.python.org/downloads/) and Pip if you do not have them installed. Pip is usually included in the Python installation package.

* Clone repository: `git@github.com:emmalait/project-time-mgmt.git`
* ...or [download it](https://github.com/emmalait/project-time-mgmt/archive/master.zip) as a .zip package and unzip.
* Navigate to repository root: `cd project-time-mgmt`
* Create virtual environment via command line: `python3 -m venv venv`
* Activate virtual environment: `source venv/bin/activate`
* Install project dependencies in the virtual environment: `pip install -r requirements.txt`
* Run app: `python3 run.py`
* Application is now running at <http://127.0.0.1:5000>

## User guide

### Registration
Using the app requires registration. To register, click on 'Register' in the navigation menu, enter your name (2-144 characters), username (2-144 characters), password (min 6 characters) and repeat password, and click 'Register'.

### Login
All features of the app (excluding registration and login) require the user to be logged in. To log in, click on 'Log in' in the navigation menu, enter your username and password, and click 'Log in'. After logging in, you are redirected to the front page, where the projects you have been assigned to and your five most recent time logs are displayed.

### Logout
To log out, click on the 'Log out' link in the navigation menu.

### Roles
Users can have one of two roles: manager and employee. The first user to register into an instance of the app will be given the role of manager automatically. Otherwise, all registered users are initially assigned the role of employee. 

### Users 
User data is managed under 'Users' in the navigation menu and is only available to users with the manager role. Under 'Users', managers can change users' roles and manage users' salaries. The salary data is used to calculated costs for projects.

### Time logs
All users can enter time logs. Time logs are entered under 'Log time' in the navigation menu. To add a time log, user must choose a project and work type and add a description and the hours spent. Users can only log time to projects they are currently assigned to (assignments are managed by managers under the project details page, see more under [Projects](https://github.com/emmalait/project-time-mgmt/blob/master/documentation/guides.md#projects).

Users can view their time logs under 'Time logs' in the navigation menu. Provided that the time log's invoicing status is 'Not invoiced', the user can edit or delete the time log. If the invoicing status is changed to 'Invoiced', users can only view the time log. 

### Work types
Work types are managed under 'Work types' in the navigation menu. Existing work types are listed and they can be edited or deleted. Deletion is only possible if the work type has not been used in a time log. New work types can be added via the 'Add work type' link. Work type data includes name (2-144 characters) and price (0-1000 euros). The price data is used to calculate revenues for projects.

### Customers
Customer data is managed under 'Customers' in the navigation menu. Existing customers are listed and customer data can be edited via the 'Edit' link. New customers can be added via the 'Add customer' link. Customer data includes the customer's name (2-144 characters) and their business ID (9 characters, e.g. 1234567-8).

### Projects
Project data is managed and viewed under 'Projects' in the navigation menu. Existing projects are listed. For employees, the customer of the project, project name and project budget are visible. For managers, additionally project costs, revenues and profit are also visible. Project costs, revenues and profit are based on project entries that have the invoicing status 'Invoiced'.

New projects can be added via the 'Add project' link. Project data includes customer name, which is selected from a list of existing customers, project name (2-144 characters) and budget (0-9 000 000 000 euros). 

Project details can be viewed via the 'View details' link. Employees can view project members, i.e. the users assigned to the project, and all project entries. They can additionally edit or delete their own time logs provided that their invoicing status is 'Not invoiced'. Managers can in addition view key figures of the project (costs, revenues and gross profit), assign and unassign users to/from the project via the 'Assign users' link, and mark time logs as invoiced. Managers can also edit everyone's time logs, not just their own.
