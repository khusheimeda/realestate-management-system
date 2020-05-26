from time import strftime
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
# from models import db
from sqlalchemy.ext.automap import automap_base
import database
from datetime import datetime, date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/realestate1'
db = SQLAlchemy(app)
date_format = "%-I:%M %p, %-d %B %Y"

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Admin = Base.classes.admin
Client_Address = Base.classes.client_address
Client = Base.classes.client
Property = Base.classes.property
Land = Base.classes.land
House = Base.classes.house
Rent = Base.classes.rent


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role')
        print(role)
        id1 = request.form['id']
        if role == 'Admin':
            results = db.session.query(Admin).all()
            for r in results:
                if r.admin_id == id1:
                    return redirect(url_for('admin_password', id1=id1))
            return redirect(url_for('login'))
        elif role == 'Client':
            results1 = db.session.query(Client).all()
            for r in results1:
                if r.client_id == id1:
                    return redirect(url_for('show_public_database'))
            return redirect(url_for('login'))
    return render_template("login_common.html")


@app.route('/login/admin/password/<id1>', methods=['GET', 'POST'])
def admin_password(id1):
    if request.method == 'POST':
        password = request.form['password']
        print(password)
        # check with password in database and redirect accordingly
        results = db.session.query(Admin).all()
        for r in results:
            if r.admin_id == id1 and r.admin_password == password:
                return redirect(url_for('show_private_database'))
        return redirect(url_for('admin_password', id1=id1))

    return render_template("admin_password.html")


@app.route('/show/public/database')
def show_public_database():
    """Returns all data in database"""
    data = [("Client_Address", ("Postal Code", "City", "State"), []),
            ("Client", ("Client_ID", "Name", "Contact_No", "DOB", "Aadhar_No", "Postal_Code"), []),
            ("Property", ("Property_ID", "Property_Type", "Owner_ID", "Date_Posted", "Property_Status"), []),
            ("Land", (
                "Plot_ID", "Plot_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Length", "Breadth",
                "Facing", "Total_Cost"), []),
            ("House", (
                "House_ID", "House_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Facing", "BHK",
                "Parking", "Total_Cost"), []),
            ("Rent", (
                "Rent_ID", "Building_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Facing", "BHK",
                "Parking", "Tenant_Type", "Monthly_Rent", "Advance_Amount"), []
             )]
    data[0][2].extend(database.execute_query("SELECT * FROM Client_Address;"))
    data[1][2].extend(database.execute_query("SELECT * FROM Client;"))
    data[2][2].extend(database.execute_query("SELECT * FROM Property;"))
    data[3][2].extend(database.execute_query("SELECT * FROM Land;"))
    data[4][2].extend(database.execute_query("SELECT * FROM House;"))
    data[5][2].extend(database.execute_query("SELECT * FROM Rent;"))

    return render_template("database_public.html", data=data, enumerate=enumerate, isinstance=isinstance,
                           datetime=datetime, date_format=date_format)


@app.route("/show/private/database")
def show_private_database():
    """Returns all data in database"""
    data1 = [("Book", ("Book_ID", "Date_Booked", "Property_ID", "Owner_ID", "Buyer_ID"), []),
             ("Payment", ("Payment_ID", "Transaction_Ref_No", "Payment_Status", "Book_ID", "Client_ID"), []
              )]
    data1[0][2].extend(database.execute_query("SELECT * FROM Book;"))
    data1[1][2].extend(database.execute_query("SELECT * FROM Payment;"))
    print(data1)

    return render_template("database_private.html", data=data1, enumerate=enumerate, isinstance=isinstance,
                           datetime=datetime, date_format=date_format)


@app.route('/sell', methods=['GET', 'POST'])
def sell():
    if request.method == 'POST':
        property_type = request.form['property_type']
        owner_id = request.form['owner_id']
        plot_no = request.form['plot_no']
        street_no = request.form['street_no']
        locality_name = request.form['locality_name']
        city = request.form['city']
        state = request.form['state']
        pin_code = request.form['pin_code']
        facing = request.form['facing']

        date_posted = datetime.today()
        date_posted = date_posted.strftime("%Y") + '/' + date_posted.strftime("%m") + '/' + date_posted.strftime("%d")
        # property_id = int(db.session.query(Property).order_by(Property.property_id.desc()).first()[1:])+1
        # property = [("Property", ("Property_ID", "Property_Type", "Owner_ID", "Date_Posted", "Property_Status"))]

        if property_type == 'Land':
            length = request.form['length']
            breadth = request.form['breadth']
            total_cost = request.form['total_cost']
            results = db.session.query(Land).all()
            plot_id = results[-1].plot_id[1:]
            plot_id = int(plot_id) + 1
            database.other_query("INSERT INTO property VALUES('L" + str(
                plot_id) + "', '" + property_type + "', '" + owner_id + "', '" + date_posted + "', 'Unsold')")
            database.other_query("INSERT INTO land values('L" + str(
                plot_id) + "', '" + plot_no + "', '" + street_no + "', '" + locality_name + "', '" + city + "', '" + state + "', '" + pin_code + "', " + length + ", " + breadth + ", '" + facing + "', " + total_cost + ")")

        elif property_type == 'House':
            bhk = request.form['bhk']
            parking = request.form['parking']
            total_cost = request.form['total_cost_h']
            print(total_cost)
            results = db.session.query(House).all()
            house_id = results[-1].house_id[1:]
            house_id = int(house_id) + 1
            database.other_query("INSERT INTO property VALUES('H" + str(
                house_id) + "', '" + property_type + "', '" + owner_id + "', '" + date_posted + "', 'Unsold')")
            database.other_query("INSERT INTO house values('H" + str(
                house_id) + "', '" + plot_no + "', '" + street_no + "', '" + locality_name + "', '" + city + "', '" + state + "', '" + pin_code + "', '" + facing + "', " + bhk + ", '" + parking + "', " + total_cost + ")")

        elif property_type == 'Rent':
            bhk = request.form['bhk_r']
            parking = request.form['parking_r']
            tenant_type = request.form['tenant_type']
            monthly_rent = request.form['monthly_rent']
            advance_amount = request.form['advance_amount']
            results = db.session.query(Rent).all()
            rent_id = results[-1].rent_id[1:]
            rent_id = int(rent_id) + 1
            database.other_query("INSERT INTO property VALUES('R" + str(
                rent_id) + "', '" + property_type + "', '" + owner_id + "', '" + date_posted + "', 'Unsold')")
            database.other_query("INSERT INTO rent values('R" + str(
                rent_id) + "', '" + plot_no + "', '" + street_no + "', '" + locality_name + "', '" + city + "', '" + state + "', '" + pin_code + "', '" + facing + "', " + bhk + ", '" + parking + "', '" + tenant_type + "', " + monthly_rent + ", " + advance_amount + ")")

        return redirect(url_for('show_public_database'))
    return render_template("sell.html")


@app.route('/enter/admin', methods=['GET', 'POST'])
def home_admin():
    return render_template("admin_view.html")


if __name__ == '__main__':
    app.run(debug=True)
