from utils.database_instance import db
from werkzeug.security import generate_password_hash, check_password_hash
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # 'servidor', 'aluno', 'admin', 'nutricionista'
    
    def __repr__(self):
        return f"<Usuario {self.nome}, {self.tipo}>"
    
    def json(self) -> dict:
        return {
            "id":self.id,
            "nome":self.nome,
            "email":self.email,
            "tipo":self.tipo
        }
        
    def check_password(self, senha_clara: str) -> bool:
        """Verifica se a senha informada corresponde ao hash armazenado."""
        return check_password_hash(self.senha, senha_clara)

    def change_password(self, nova_senha: str):
        """Troca a senha do usuário e salva no banco já com hash."""
        self.senha = generate_password_hash(nova_senha)
        db.session.commit()