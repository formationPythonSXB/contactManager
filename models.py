from common import db, app, api
from flask_restful import Resource

class Contact(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=True)
    phone = db.Column(db.String(10), nullable=True)
    birthday = db.Column(db.Date, nullable=True)
    balance = db.Column(db.Integer, nullable=False, default=0)

    def rest_repr(self):
        return {
            "name": self.name,
            "email": self.email
        }


class ResourceContact(Resource):

    def get(self, name=None):
        return Contact.query.filter(Contact.name == name).first_or_404().rest_repr()

class ResourceContactList(Resource):

    def get(self):
        return [c.rest_repr() for c in Contact.query.all()]

    def post(self):
        # Ici, on pourrait récupérer les données de la payload
        # pour créer un nouveau contact...
        raise NotImplementedError()

api.add_resource(ResourceContactList, '/contacts')
api.add_resource(ResourceContact, '/contacts/<string:name>')
