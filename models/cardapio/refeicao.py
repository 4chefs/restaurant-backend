from utils.database_instance import db
class Refeicao(db.Model):
    __tablename__ = "refeicao"
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    
    cardapios = db.relationship('Cardapio', backref='refeicao', lazy=True)