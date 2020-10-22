from common import app, db
from flask import render_template, request, redirect
from models import Contact

@app.route('/')
def homepage():
    contacts = Contact.query.all()
    return render_template('homepage.html', contacts=contacts)



@app.route('/add', methods=['POST'])
def add_contact():
    db.session.add(Contact(name=request.form["name"],
                           phone=request.form["phone"],
                           email=request.form["email"],
                           birthday=None))
    db.session.commit()
    return redirect("/")
