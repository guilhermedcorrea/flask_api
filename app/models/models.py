from extensions import db
from datetime import datetime


class UserGroups(db):
    __tablename__ = 'usergroups'
    id = db.Column(db.Integer, primary_key=True)
    grupo = db.Column(db.String, unique=True, nullable=False)
    status = db.Column(db.String)
    
    def __repr__(self):
        return "{self.id}"


class User(db):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String)
    data = db.Column(db.DateTime)
    
    
    def __repr__(self):
        return "{self.id}"
    
    
    