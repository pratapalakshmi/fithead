from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Example model
default_repr = lambda self: f"<{self.__class__.__name__} id={self.id}>"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    __repr__ = default_repr 