from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    prosperaId = db.Column(db.BigInteger, primary_key=True)
    clues = db.Column(db.String(255), index=True)
    nom_mun = db.Column(db.String(255), index=True)

    def __init__(self,prosperaId = 0):
        self.prosperaId = prosperaId
#end
