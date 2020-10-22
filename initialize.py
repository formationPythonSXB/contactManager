from common import db
from models import Contact
import datetime

db.drop_all()
db.create_all()

db.session.add(Contact(name="Alice",   phone="1111", email='alice@gmail.com', birthday=None))
db.session.add(Contact(name="Bob",     phone="2222", email='bob@yahoo.fr', birthday=None))
db.session.add(Contact(name="Camille", phone="3333", email='camille@hotmail.com', birthday=datetime.datetime.now()))

db.session.commit()
