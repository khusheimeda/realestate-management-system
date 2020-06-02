from flask import Flask, render_template, request, url_for, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import database
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/realestate1'
app.secret_key = "khushei"
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
Book = Base.classes.book
Payment = Base.classes.payment


@app.route('/')
def home():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form.get('role')
        print(role)
        global id1
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
        results = db.session.query(Admin).all()
        for r in results:
            if r.admin_id == id1 and r.admin_password == password:
                return redirect(url_for('show_private_database'))
        flash("Incorrect password")
        return redirect(url_for('admin_password', id1=id1))

    return render_template("admin_password.html")


@app.route('/show/public/database')
def show_public_database():
    """Returns all data in database"""
    data = [("Property", ("Property_ID", "Property_Type", "Owner_ID", "Date_Posted", "Property_Status"), []),
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
    data[0][2].extend(database.execute_query("SELECT * FROM Property;"))
    data[1][2].extend(database.execute_query("SELECT * FROM Land;"))
    data[2][2].extend(database.execute_query("SELECT * FROM House;"))
    data[3][2].extend(database.execute_query("SELECT * FROM Rent;"))

    return render_template("database_public.html", data=data, enumerate=enumerate, isinstance=isinstance,
                           datetime=datetime, date_format=date_format)


@app.route("/show/private/database")
def show_private_database():
    """Returns all data in database"""
    data1 = [("Client_Address", ("Postal Code", "City", "State"), []),
             ("Client", ("Client_ID", "Name", "Contact_No", "DOB", "Aadhar_No", "Postal_Code"), []),
             ("Book", ("Book_ID", "Date_Booked", "Property_ID", "Owner_ID", "Buyer_ID"), []),
             ("Payment", ("Payment_ID", "Transaction_Ref_No", "Payment_Status", "Book_ID", "Client_ID"), []
              )]
    data1[0][2].extend(database.execute_query("SELECT * FROM Client_Address;"))
    data1[1][2].extend(database.execute_query("SELECT * FROM Client;"))
    data1[2][2].extend(database.execute_query("SELECT * FROM Book;"))
    data1[3][2].extend(database.execute_query("SELECT * FROM Payment;"))
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

        if owner_id != id1:
            flash("Incorrect client id")
            return redirect(url_for('sell'))

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

        flash("Property added for sale")
        return redirect(url_for('show_public_database'))
    return render_template("sell.html")


@app.route('/update/sell', methods=['GET', 'POST'])
def update_sell():
    if request.method == 'POST':
        property_type = request.form['property_type']
        property_id = request.form['property_id']

        if property_type == 'Land':
            total_cost = request.form['total_cost']
            property_status = request.form['property_status']

            if total_cost != '':
                results = db.session.query(Land).all()
                for r in results:
                    if r.plot_id == property_id:
                        database.other_query(
                            "UPDATE land SET total_cost=" + total_cost + " where plot_id='" + property_id + "'")
            if property_status != '':
                results1 = db.session.query(Property).all()
                for r in results1:
                    if r.property_id == property_id:
                        database.other_query(
                            "UPDATE property SET property_status='" + property_status + "' where property_id='" + property_id + "'")

        elif property_type == 'House':
            total_cost = request.form['total_cost_h']
            property_status = request.form['property_status_h']

            if total_cost != '':
                results = db.session.query(House).all()
                for r in results:
                    if r.house_id == property_id:
                        if total_cost != '':
                            database.other_query(
                                "UPDATE house SET total_cost=" + total_cost + " where house_id='" + property_id + "'")

            if property_status != '':
                results1 = db.session.query(Property).all()
                for r in results1:
                    if r.property_id == property_id:
                        database.other_query(
                            "UPDATE property SET property_status='" + property_status + "' where property_id='" + property_id + "'")

        elif property_type == 'Rent':
            tenant_type = request.form['tenant_type']
            monthly_rent = request.form['monthly_rent']
            advance_amount = request.form['advance_amount']
            property_status = request.form['property_status_r']

            results = db.session.query(Rent).all()
            for r in results:
                if r.rent_id == property_id:
                    if tenant_type != '':
                        database.other_query(
                            "UPDATE rent SET tenant_type='" + tenant_type + "' where rent_id='" + property_id + "'")
                    if monthly_rent != '':
                        database.other_query(
                            "UPDATE rent SET monthly_rent=" + monthly_rent + " where rent_id='" + property_id + "'")
                    if advance_amount != '':
                        database.other_query(
                            "UPDATE rent SET advance_amount=" + advance_amount + " where rent_id='" + property_id + "'")
            if property_status != '':
                results1 = db.session.query(Property).all()
                for r in results1:
                    if r.property_id == property_id:
                        database.other_query(
                            "UPDATE property SET property_status='" + property_status + "' where property_id='" + property_id + "'")

        flash("Property details updated")
        return redirect(url_for('show_public_database'))
    return render_template("update_sell.html")


@app.route('/buy/land', methods=['GET', 'POST'])
def buy_land():
    data = [("Land view", (
        "Date_Posted", "Plot_ID", "Plot_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Length",
        "Breadth",
        "Facing", "Total_Cost"), [])]
    database.other_query(
        "create view buy_land as select date_posted, Plot_ID, Plot_No, Street_No, Locality_Name, City, State, Pin_Code, Length, Breadth, Facing, Total_Cost from property, land where property_id=plot_id and property_status='Unsold';")
    data[0][2].extend(database.execute_query("SELECT * FROM buy_land;"))
    database.other_query("drop view buy_land;")
    if request.method == 'POST':
        buyer_id = request.form['buyer_id']
        plot_id = request.form['plot_id']
        results = db.session.query(Land).all()
        if buyer_id == id1:
            for r in results:
                if r.plot_id == plot_id:
                    return redirect(url_for('pay', plot_id=plot_id, amt=r.total_cost))
        else:
            flash("Please enter correct client id")
            return redirect(url_for('buy_land'))
    return render_template("buy_land.html", data=data, enumerate=enumerate, isinstance=isinstance,
                           datetime=datetime, date_format=date_format)


@app.route('/buy/house', methods=['GET', 'POST'])
def buy_house():
    data = [("House view", (
        "Date_Posted", "House_ID", "House_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Facing",
        "BHK", "Parking", "Total_Cost"), [])]
    database.other_query("create view buy_house as select date_posted, House_ID, House_No, Street_No, Locality_Name, City, State, Pin_Code, Facing, BHK, Parking, Total_Cost from property, house where property_id=house_id and property_status='Unsold';")
    data[0][2].extend(database.execute_query("SELECT * FROM buy_house;"))
    database.other_query("drop view buy_house;")
    if request.method == 'POST':
        buyer_id = request.form['buyer_id']
        house_id = request.form['house_id']
        results = db.session.query(House).all()
        if buyer_id == id1:
            for r in results:
                if r.house_id == house_id:
                    return redirect(url_for('pay', plot_id=house_id, amt=r.total_cost))
        else:
            flash("Please enter correct client id")
            return redirect(url_for('buy_house'))
    return render_template("buy_house.html", data=data, enumerate=enumerate, isinstance=isinstance,
                           datetime=datetime, date_format=date_format)

@app.route('/rent', methods=['GET', 'POST'])
def rent():
    data = [("Rent view", ("Date_Posted", "Rent_ID", "Building_No", "Street_No", "Locality_Name", "City", "State", "Pin_Code", "Facing", "BHK", "Parking", "Tenant_Type", "Monthly_Rent", "Advance_Amount"), [])]
    database.other_query("create view buy_rent as select date_posted, Rent_ID, Building_No, Street_No, Locality_Name, City, State, Pin_Code, Facing, BHK, Parking, Tenant_Type, Monthly_Rent, Advance_amount from property, rent where property_id=rent_id and property_status='Unsold';")
    data[0][2].extend(database.execute_query("SELECT * FROM buy_rent;"))
    database.other_query("drop view buy_rent;")
    if request.method == 'POST':
        buyer_id = request.form['buyer_id']
        rent_id = request.form['rent_id']
        results = db.session.query(Rent).all()
        if buyer_id == id1:
            for r in results:
                if r.rent_id == rent_id:
                    return redirect(url_for('pay', plot_id=rent_id, amt=r.advance_amount))
        else:
            flash("Please enter correct client id")
            return redirect(url_for('rent'))
    return render_template("rent.html", data=data, enumerate=enumerate, isinstance=isinstance,
                           datetime=datetime, date_format=date_format)


@app.route('/pay/<amt>/for/<plot_id>', methods=['GET', 'POST'])
def pay(plot_id, amt):
    results = db.session.query(Book).all()
    book_id = results[-1].book_id[1:]
    book_id = int(book_id) + 1
    date_booked = datetime.today()
    date_booked = date_booked.strftime("%Y") + '/' + date_booked.strftime("%m") + '/' + date_booked.strftime("%d")
    results1 = db.session.query(Property).all()
    for r in results1:
        if r.property_id == plot_id:
            owner_id = r.owner_id
            if request.method == 'POST':
                choice = request.form.get('choice')
                amount = request.form['amount']
                if amount == amt and choice == 'Buy':
                    database.other_query(
                        "INSERT INTO book values('B" + str(
                            book_id) + "', '" + date_booked + "', '" + plot_id + "', '" + owner_id + "', '" + id1 + "')")
                    results2 = db.session.query(Payment).all()
                    payment_id = results2[-1].payment_id[3:]
                    payment_id = int(payment_id) + 1
                    transaction_ref_no = int(results2[-1].transaction_ref_no) + 1
                    database.other_query(
                        "INSERT INTO payment values('PAY" + str(payment_id) + "', " + str(
                            transaction_ref_no) + ", 'Fully paid', 'B" + str(book_id) + "', '" + id1 + "')")
                    database.other_query(
                        "UPDATE property SET property_status='Sold' where property_id='" + plot_id + "'")
                    flash("Congrats! You have purchased the land")
                    return redirect(url_for('show_public_database'))

                elif amount == '100' and choice == 'Book':
                    database.other_query(
                        "INSERT INTO book values('B" + str(
                            book_id) + "', '" + date_booked + "', '" + plot_id + "', '" + owner_id + "', '" + id1 + "')")
                    results2 = db.session.query(Payment).all()
                    payment_id = results2[-1].payment_id[3:]
                    payment_id = int(payment_id) + 1
                    transaction_ref_no = int(results2[-1].transaction_ref_no) + 1
                    database.other_query(
                        "INSERT INTO payment values('PAY" + str(payment_id) + "', " + str(
                            transaction_ref_no) + ", 'Partially paid', 'B" + str(book_id) + "', '" + id1 + "')")
                    database.other_query(
                        "UPDATE property SET property_status='Booked' where property_id='" + plot_id + "'")
                    flash("Booked")
                    return redirect(url_for('show_public_database'))

                else:
                    flash("Either you have entered incorrect amount, or chosen invalid choice")
                    return redirect(url_for('pay', plot_id=plot_id, amt=amt))

    return render_template("pay.html")


@app.route('/enter/admin', methods=['GET', 'POST'])
def home_admin():
    return render_template("admin_view.html")


if __name__ == '__main__':
    app.run(debug=True)
