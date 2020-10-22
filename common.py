from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
swagger = Swagger(app)
