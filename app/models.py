from datetime import date

from app import db
class Document(db.Model): 

    """
    Create an Event table
    """
    __tablename__ = 'document'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    category = db.Column(db.String(128))
    user = db.Column(db.String(128))
    avaliado = db.Column(db.Boolean)
    directory = db.Column(db.String(128))
    time = db.Column(db.Integer)
    
    def __repr__(self):
        return '<>Documento: {}'.format(self.name_event)

class Permission(db.Model):

    """
    Create an kajshdkjh table
    """
    __tablename__ = 'permission'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128))
    level = db.Column(db.Integer)

    def __repr__(self):
        return '<>Permissao: {}'.format(self.name_event)
