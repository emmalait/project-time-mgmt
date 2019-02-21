from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.customers.models import Customer
from application.customers.forms import CustomerForm

# Show all customers
@app.route("/customers", methods=["GET"])
def customers_index():
    return render_template("customers/list.html", customers = Customer.query.all())

# Create a new work type
@app.route("/customers", methods=["POST"])
@login_required
def customers_create():
    form = CustomerForm(request.form)

    c = Customer(form.name.data, form.business_id.data)
    
    db.session().add(c)
    db.session().commit()
  
    return redirect(url_for("customers_index"))
    
# Show the form for creating a new work type
@app.route("/customers/new")
@login_required
def customers_form():
    return render_template("customers/new.html", form = CustomerForm())

# View a work type
@app.route("/customers/<customer_id>", methods=["GET"])
@login_required
def customer(customer_id):
    c = Customer.query.filter_by(id = customer_id).first()
  
    return render_template("customers/view.html", customer = c)