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
    user = db.Column(db.Integer)
    avaliado = db.Column(db.Boolean)
    directory = db.Column(db.String(128))
    
    def __repr__(self):
        return '<>Evento: {}'.format(self.name_event)
