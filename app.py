from flask import Flask, request, redirect, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant_booking1.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "AFagsDfa$!lmgq34@mvajbhf74nm&lakhdffahdhjfgrftAg"
db = SQLAlchemy(app)


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(20))
    phone = db.Column(db.String(50))

    def __init__(self, firstname, lastname, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone


class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(20))

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email


# ===================================================General URL's===============================================


@app.route('/')
@app.route('/home/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/menu/')
def menu():
    return render_template('menu.html')


@app.route('/booking/', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        if not request.form['firstname'] or not request.form['lastname'] or not request.form['email'] or not request.form['phone']:
            print('Please, fill all the fields', 'error')
        else:
            bookings = Booking(request.form['firstname'], request.form['lastname'], request.form['email'],
                               request.form['phone'])
            db.session.add(bookings)
            db.session.commit()
            print('Record added')
            return redirect(url_for('index'))
    return render_template('booking.html')


@app.route('/events/')
def event():
    return render_template('contact.html')


@app.route('/events/enquiry/')
def enquiry():
    return render_template('contact.html')


@app.route('/find-us/')
def contact():
    return render_template('contact.html')


@app.route('/newsletter-signup/', methods=['GET', 'POST'])
def newsletter_signup():
    if request.method == 'POST':
        if not request.form['firstname'] or not request.form['lastname'] or not request.form['email']:
            print('Please, fill all the fields', 'error')
        else:
            newsletters = Newsletter(request.form['firstname'], request.form['lastname'], request.form['email'])
            db.session.add(newsletters)
            db.session.commit()
            print('Record added')
            return redirect(url_for('index'))
    return render_template('newsletter-signup.html')


# @app.route('/contact-us/')
# def contact_us_page():
#     return render_template()


# ===================================================Admin URL's===============================================
@app.route('/login/')
@app.route('/admin/')
def admin_login_page():
    return render_template('admin_login_page.html')


@app.route('/admin_panel/')
def admin_panel():
    return render_template('admin_panel.html')


@app.route('/admin_panel/admin_panel_bookings/')
def admin_panel_bookings():
    return render_template('admin_panel_bookings.html', Booking=Booking.query.all())


@app.route('/admin_panel/newsletter_subscribers/')
def admin_panel_newsletter_subscribers():
    return render_template('admin_panel_subscribers.html', Newsletter=Newsletter.query.all())


@app.route('/admin_panel/enquiries/')
def admin_panel_enquiries():
    return render_template('admin_panel_enquiries.html')


@app.route('/admin_panel/messages/')
def admin_panel_messages():
    return render_template('admin_panel_messages.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
