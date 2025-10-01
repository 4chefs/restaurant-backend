from utils.database_instance import db
class Prato(db.Model):
    __tablename__ = "prato"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    descricao = db.Column(db.String(150))
    
    cardapios = db.relationship('Cardapio', backref='prato', lazy=True)