from utils.database_instance import db
class Dia(db.Model):
    __tablename__ = "dia"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    
    cardapios = db.relationship('Cardapio', backref='dia', lazy=True)