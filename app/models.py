# Boilerplate for Models

from app import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer)
    code = db.Column(db.Integer)
    name = db.Column(db.String(50))
    alive = db.Column(db.Boolean)
    score = db.Column(db.Integer)

    def __repr__(self):
        return "<Player: %r>" % (self.name)
