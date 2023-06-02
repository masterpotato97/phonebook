from app import app
from flask import Flask, render_template, request, flash


@app.route('/')

def index():
    
    return render_template('index.html')


@app.route('/test',  methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        address = request.form['address']

        print(f"First Name: {first_name}")
        print(f"Last Name: {last_name}")
        print(f"Phone Number: {phone_number}")
        print(f"Address: {address}")

        flash(f"{first_name} {last_name} has been added to the address book")
       
    return render_template('contact.html')    
        