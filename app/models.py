from app import db


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel = db.Column(db.String(50), nullable=False)
    kategorie_id = db.Column(db.Integer, db.ForeignKey('kategorie.id'), nullable=False)
    text = db.Column(db.String(9999))

class Kategorie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    blog = db.relationship('Blog', lazy='select', backref=db.backref('Kategorie', lazy='joined'))
