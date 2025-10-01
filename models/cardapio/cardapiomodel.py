from utils.database_instance import db
from .diadasemana import Dia
from .prato import Prato
from .refeicao import Refeicao

class Cardapio(db.Model):
    __tablename__ = "cardapio"
    
    id= db.Column(db.Integer, primary_key=True)
    dia_id = db.Column(db.Integer, db.ForeignKey('dia.id'), nullable=False) 
    prato_id = db.Column(db.Integer, db.ForeignKey('prato.id'), nullable=False)
    refeicao_id = db.Column(db.Integer, db.ForeignKey('refeicao.id'), nullable=False)

    dia = db.relationship('Dia', backref='cardapios')
    prato = db.relationship('Prato', backref='cardapios')  
    refeicao = db.relationship('Refeicao', backref='cardapios') 