# Represents User in the App

from . import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(100))
  name = db.Column(db.String(200))
