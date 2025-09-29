from utils.database_instance import db
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # 'servidor', 'aluno', 'admin', 'nutricionista'
    
    def __repr__(self):
        return f"<Usuario {self.nome}, {self.tipo}>"