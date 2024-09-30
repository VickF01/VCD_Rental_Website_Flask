from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    email = db.Column(db.String(50), primary_key = True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    role = db.Column(db.String(5))

    def __init__(self, email, name, password, role):
        self.email = email
        self.name = name
        self.password = password
        self.role = role

    def __repr__(self):
        return '[%s, %s, %s, %s]' % \
            (self.email, self.name, self.password, self.role)