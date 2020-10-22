from common import app, db
from flask import render_template, request, redirect
from models import Contact

@app.route('/')
def homepage():
    contacts = Contact.query.all()
    return render_template('homepage.html', contacts=contacts)


@app.route('/add', methods=['POST'])
def add_contact():
    """
    Endpoint to add a contact
    ---
    parameters:
      - name: name
        in: body
        type: string
        required: true
      - name: phone
        in: body
        type: string
        required: true
      - name: email
        in: body
        type: string
        required: true
    responses:
      200:
        description: Successfully created the contact
    """
    db.session.add(Contact(name=request.form["name"],
                           phone=request.form["phone"],
                           email=request.form["email"],
                           birthday=None))
    db.session.commit()
    return redirect("/")
