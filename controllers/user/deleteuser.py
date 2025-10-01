from models.usermodel import Usuario
from flask import request
from errors.delete_error import DeleteError
from utils.database_instance import db

def delete_user(user_id) -> Usuario:
    """
    Apaga um usuário com base no id recebido.

    Returns:
        Objeto da classe Usuario

    Raises:
        DeleteError: Se o usuário não existir ou os dados forem inválidos.
    """
    usuario: Usuario = Usuario.query.get(user_id)

    if not usuario:
        raise DeleteError("<pre>Usuário não encontrado.</pre>")
    
    db.session.remove(usuario)
    db.session.commit()

    return usuario
