from flask import Flask, render_template, request, redirect, url_for
import os
from data import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/registation', methods=['POST'])
def registration():
    # Process the registration form data here
    payload = {'name': request.form['name'],
                'subject': request.form['subject'],
                'course': request.form['course'],
                'email': request.form['email'],
                'phone': request.form['phone'],
                'dob': request.form['dob']}
    # Redirect to the 'admissionreference' page
    register_student(payload)
    return redirect('/adrefscreen')

@app.route('/adrefscreen')
def display_admissions():
    admissions = get_admissions()
    return render_template('adrefscreen.html', admissions=admissions)

subjects = ["LIS51", "LIS55", "LIS161"]

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        results = search_by_name_and_subject(name, subject)
        return render_template('resultsadstaff.html', results=results)
    return render_template('searchadstaff.html', subjects=subjects)

@app.route('/masterlist', methods=['GET', 'POST'])
def master():
    if request.method == 'POST':
        name = request.form['name']
        subject = request.form['subject']
        results = mastersearch_by_name_and_subject(name, subject)
        return render_template('resultsadref.html', results=results)
    return render_template('searchadref.html', subjects=subjects)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
