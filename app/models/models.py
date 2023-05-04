from extensions import db


class UserGroups(db):
    id = db.Column(db.Integer, primary_key=True)
    grupo = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String)


class User(db):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    
    