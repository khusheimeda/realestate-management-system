from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
#from models import db
from sqlalchemy.ext.automap import automap_base
import database
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/realestate1'
db = SQLAlchemy(app)
date_format = "%-I:%M %p, %-d %B %Y"

Base = automap_base()
Base.prepare(db.engine, reflect = True)
Admin = Base.classes.admin
Client_Address = Base.classes.client_address


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role')
        print(role)
        global username
        id = request.form['id']
        if role == 'Admin':
            return redirect(url_for('admin_password'))
        elif role == 'Client':
            return redirect(url_for('show_public_database'))
    return render_template("login_common.html")

@app.route('/login/admin/password', methods=['GET', 'POST'])
def admin_password():
    if request.method == 'POST':
        password = request.form['password']
        print(password)
        #check with password in database and redirect accordingly
    return render_template("admin_password.html")

@app.route("/login/show/public/database")
def show_public_database():
    """Returns all data in database"""
    data = [("Client_Address", ("Postal Code", "City", "State"), []),
            ("Client", ("Client_ID", "Name", "Contact_No", "DOB", "Aadhar_No", "Postal_Code"), []),
            ("Property", ("Property_ID", "Property_Type", "Owner_ID", "Date_Posted", "Property_Status"), []),
            ("Land", ("Plot_ID", "Plot_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Length", "Breadth", "Facing", "Total_Cost"), []),
            ("House", ("House_ID", "House_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Facing", "BHK", "Parking", "Total_Cost"), []),
            ("Rent", ("Rent_ID", "Building_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Facing", "BHK", "Parking", "Tenant_Type", "Monthly_Rent", "Advance_Amount"), []
)]
    data[0][2].extend(database.execute_query("SELECT * FROM Client_Address;"))
    data[1][2].extend(database.execute_query("SELECT * FROM Client;"))
    data[2][2].extend(database.execute_query("SELECT * FROM Property;"))
    data[3][2].extend(database.execute_query("SELECT * FROM Land;"))
    data[4][2].extend(database.execute_query("SELECT * FROM House;"))
    data[5][2].extend(database.execute_query("SELECT * FROM Rent;"))
    #print(data)

    return render_template("database.html", data=data, enumerate=enumerate, isinstance=isinstance, datetime=datetime, date_format=date_format)

@app.route('/enter/client', methods=['GET', 'POST'])
def home_client():
    '''results = db.session.query(Admin).all()
    for r in results:
        print(r.admin_id, r.admin_password)'''
    #return redirect(url_for(show_public_database))
    return render_template("client_view.html")

if __name__ == '__main__':
    app.run(debug=True)