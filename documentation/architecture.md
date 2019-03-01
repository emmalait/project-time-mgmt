# Architecture

## Database

### Database diagram

<img src="https://github.com/emmalait/project-time-mgmt/blob/master/documentation/images/db-diagram.png?raw=true" width="600">

### CREATE TABLE statements

#### User (account)
```sql
CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	role VARCHAR(144), 
	salary NUMERIC NOT NULL, 
	PRIMARY KEY (id)
);
```

#### WorkType
```sql
CREATE TABLE work_type (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	price NUMERIC NOT NULL, 
	PRIMARY KEY (id)
);
```

#### Customer
```sql
CREATE TABLE customer (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	business_id VARCHAR(9) NOT NULL, 
	PRIMARY KEY (id)
);
```

#### Project
```sql
CREATE TABLE project (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	budget NUMERIC NOT NULL, 
	customer_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(customer_id) REFERENCES customer (id)
);
```

#### TimeLog
```sql
CREATE TABLE time_log (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	hours INTEGER NOT NULL, 
	description VARCHAR(144) NOT NULL, 
	cleared BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	work_type_id INTEGER NOT NULL, 
	project_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (cleared IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(work_type_id) REFERENCES work_type (id), 
	FOREIGN KEY(project_id) REFERENCES project (id)
);
```

#### ProjectMembers
```sql
CREATE TABLE project_members (
	account_id INTEGER, 
	project_id INTEGER, 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(project_id) REFERENCES project (id)
);
```

## Application structure

### File structure

```
.
├── Procfile
├── README.md
├── application
│   ├── __init__.py
│   ├── auth
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── customers
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── models.py
│   ├── projects
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── templates
│   │   ├── auth
│   │   │   ├── list.html
│   │   │   ├── loginform.html
│   │   │   ├── register.html
│   │   │   └── view.html
│   │   ├── customers
│   │   │   ├── list.html
│   │   │   ├── new.html
│   │   │   └── view.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   ├── projects
│   │   │   ├── assignedUsers.html
│   │   │   ├── edit.html
│   │   │   ├── list.html
│   │   │   ├── new.html
│   │   │   └── view.html
│   │   ├── timelogs
│   │   │   ├── list.html
│   │   │   ├── new.html
│   │   │   └── view.html
│   │   └── worktypes
│   │       ├── list.html
│   │       ├── new.html
│   │       └── view.html
│   ├── timelogs
│   │   ├── forms.py
│   │   ├── models.py
│   │   └── views.py
│   ├── timelogs.db
│   ├── views.py
│   └── worktypes
│       ├── forms.py
│       ├── models.py
│       └── views.py
├── documentation
│   ├── architecture.md
│   ├── guides.md
│   └── images
│   │   └── db-diagram.png
│   ├── userstories.md
│   └── reflection.md
├── requirements.txt
├── run.py
```

Each database table (excl. ProjectMembers, which is an association table) corresponds with its own model, which has its dedicated folder containing its models, forms & views (routes). The HTML templates for each model are located under `application/templates`.

### Routes

PATH | VERB | FUNCTIONALITY
--- | --- | ---
/auth/login | GET | Show login form
/auth/login | POST | Handle login
/auth/logout | | Handle logout
/auth/register | GET | Show registration form
/auth/register | POST | Create a new user
/auth/<user_id> | GET | Show the edit form for a user
/auth/<user_id> | POST | Update a user
/customers | GET | Show all customer
/customers | POST | Create a new customer
/customers/new | | Show the form for creating a new customer
/customers/<customer_id> | GET | Show the edit form for a customer
/customers/<customer_id> | POST | Edit a customer
/projects | GET | Show all projects
/projects | POST | Create a new project
/projects/new | | Show the form for creating a project
/projects/<project_id> | GET | View a project
/projects/<project_id>/edit | GET | View the edit form for a project
/projects/<project_id>/edit | POST | Edit a project
/projects/<project_id>/members | GET | View page to assign users to a project
/projects/<project_id>/members/<account_id>/assign | POST | Assign user to a project
/projects/<project_id>/members/<account_id>/unassign | POST | Unassign user from a project
/timelogs |	GET	| Show all time logs by the logged in user
/timelogs	| POST	| Create a new time log for the logged in user
/timelogs/new |		| Show the form for creating a new time log
/timelogs/<timelog_id>	| GET	| Show an edit form for a time log
/timelogs/<timelog_id>	| POST	| Edit a time log
/timelogs/<timelog_id>/delete	| POST | Delete a time log
/timelogs/<timelog_id>/clear | POST | Toggle 'cleared' for time log
/worktypes	| GET	| Show all work types
/worktypes	| POST	| Create a new work type
/worktypes/new | 		| Show the form for creating a new work type
/worktypes/<worktype_id>	| GET	| Show the edit form for a work type
/worktypes/<worktype_id>	| POST	| Edit a work type
/worktypes/<worktype_id>/delete | POST | Delete a work type
