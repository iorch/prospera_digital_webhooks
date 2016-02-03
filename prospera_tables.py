from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    prosperaId = db.Column(db.BigInteger, primary_key=True)
    clues = db.Column(db.String(255), index=True)
    nom_mun = db.Column(db.String(255), index=True)

    def __init__(self,prosperaId = 0):
        self.prosperaId = prosperaId

class Message(db.Model):
    __tablename__ = 'message'
    phoneId = db.Column(db.BigInteger, primary_key=True)
    message_text = db.Column(db.String(255), index=True)
    datetime = db.Column(db.String(255), index=True)
    def __init__(self,phoneId = 0,messageId = '',message_text = '', datetime = ''):
        self.phoneId = phoneId
        self.message_text = message_text
        self.datetime = datetime

    def get_message_text(self):
        return(self.message_text)
#end#end
