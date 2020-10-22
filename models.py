from common import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(10), nullable=True)
    birthday = db.Column(db.Date, nullable=True)
    balance = db.Column(db.Integer, nullable=False, default=0)


