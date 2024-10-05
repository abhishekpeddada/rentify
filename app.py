from flask import Flask, render_template, request, redirect, url_for,flash,session
from models import User, Property
from database import db_session, init_db
import hashlib

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def setup():
    init_db()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        user_type = request.form['user_type']
        password = request.form['password']
        print("register",password)
        session["username"] = first_name
        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        # Create a new user instance with hashed password
        user = User(first_name, last_name, email,hashed_password, phone_number, user_type,)
        
        # Add user to the database
        db_session.add(user)
        db_session.commit()
        
        # Redirect to login page
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        print(email,password)
        user = db_session.query(User).filter(User.email == email).first()
        if user:
            print(user.email)
            # Validate password
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user.password == hashed_password:
                # Redirect based on user type
                session["username"] = user.first_name
                session['user_email'] = user.email
                session['user_type'] = user.user_type
                if user.user_type == 'seller':
                    return redirect(url_for('seller_dashboard'))
                elif user.user_type == 'buyer':
                    return redirect(url_for('buyer_dashboard'))  # Implement buyer dashboard
            else:
                # Incorrect password
                flash('Incorrect email or password')
                return ("<h1>Incorrect Password</h1>")
        else:
            # User not found
            flash('User not found')
            return ("<h1>User not found</h1>")
    return render_template('login.html')

@app.route('/seller_dashboard')
def seller_dashboard():
    if session:
        user_email = session['user_email']
        print("seller",user_email in session['user_email'])
        if user_email in session['user_email']:
            properties = db_session.query(Property).filter(Property.email == user_email).all()
            return render_template('seller_dashboard.html', properties=properties)
        else:
            # Handle case when user is not logged in
            return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/edit_property')
def edit_property():
    return render_template('edit_property.html')

@app.route('/property_submit/<int:property_id>',methods=['POST'])
def property_submit(property_id):
    email = session['user_email']
    property = db_session.query(Property).filter(Property.email == email).first()
    if request.method == 'POST':
        property.email = request.form['email']
        property.place = request.form['place']
        property.area = request.form['area']
        property.bedrooms = request.form['bedrooms']
        property.bathrooms = request.form['bathrooms']
        property.nearby_hospitals = request.form['nearby_hospitals']
        property.nearby_colleges = request.form['nearby_colleges']
        db_session.commit()
        flash('Property updated successfully')
        return render_template('property_detail.html', property=property)
    else:
            # Property not found or does not belong to the logged-in seller
            flash('Property not found')
            return ("Property not found")

@app.route('/delete_property/<int:property_id>', methods=['GET'])
def delete_property(property_id):
    user_email = session['user_email']
    if user_email in session['user_email']:
        property = db_session.query(Property).filter(Property.id == property_id).first()
        if property and property.email == session['user_email']:
            db_session.delete(property)
            db_session.commit()
            flash('Property deleted successfully')
        else:
            # Property not found or does not belong to the logged-in seller
            flash('Property not found')
    else:
        # Redirect to login page if user is not logged in
        return redirect(url_for('login'))
    return redirect(url_for('seller_dashboard'))

@app.route('/buyer_dashboard')
def buyer_dashboard():
    if session:
        properties = db_session.query(Property).all()
        return render_template('buyer_dashboard.html', properties=properties)
    return redirect(url_for('login'))

@app.route('/property_detail/<int:property_id>')
def property_detail(property_id):
    property = db_session.query(Property).filter(Property.id == property_id).first()
    if property:
        return render_template('property_detail.html', property=property)
    else:
        # Handle the case where the property with the given ID does not exist
        return render_template('error.html', message='Property not found')

@app.route('/add_property', methods=['GET', 'POST'])
def add_property():
    if request.method == 'POST':
        email = request.form['email']
        place = request.form['place']
        area = request.form['area']
        bedrooms = request.form['bedrooms']
        bathrooms = request.form['bathrooms']
        nearby_hospitals = request.form['nearby_hospitals']
        nearby_colleges = request.form['nearby_colleges']
        user_id = request.form['user_id']
        property = Property(email,place, area, bedrooms, bathrooms, nearby_hospitals, nearby_colleges, user_id)
        db_session.add(property)
        db_session.commit()
        return redirect(url_for('seller_dashboard'))
    return render_template('add_property.html')

@app.route('/logout')
def logout():
    session.clear()  # Clear the session data
    return redirect(url_for('login'))

@app.route('/print'):
def print():
    print("hello world")

if __name__ == '__main__':
    app.run(debug=True)
