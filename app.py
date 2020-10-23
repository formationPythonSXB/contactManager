from common import app, db
from flask import render_template, request, redirect
from models import Contact

@app.route('/')
def homepage():
    contacts = Contact.query.all()
    return render_template('homepage.html', contacts=contacts)
