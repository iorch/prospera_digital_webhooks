from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'dependencia'
    dependenciaId = db.Column(db.BigInteger, primary_key=True)
    nomDependencia = db.Column(db.String(255), index=True)
    descdependencia = db.Column(db.String(255))
    ambito_id = db.Column(db.BigInteger)
    articulo_id = db.Column(db.BigInteger)
    #poder_id = db.Column(db.BigInteger)

    def __init__(self,dependenciaId = 0):
        self.dependenciaId = dependenciaId
#end
