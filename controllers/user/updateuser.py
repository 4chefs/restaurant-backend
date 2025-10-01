from models.usermodel import Usuario
from flask import request
from errors.login_error import LoginError
from utils.database_instance import db

def update_user(user_id) -> Usuario:
    """
    Atualiza os dados de um usuário com base nos dados recebidos em uma requisição JSON.

    Requisição esperada (JSON):
    {
        "nome": "Novo Nome",
        "email": "novoemail@exemplo.com",
        "tipo": "aluno/servidor/admin/nutricionista",
        "senha": "nova_senha" (opcional)
    }

    Returns:
        Objeto da classe Usuario

    Raises:
        LoginError: Se o usuário não existir ou os dados forem inválidos.
    """

    data = request.json
    if not data:
        raise LoginError("<pre>Envie ao menos um campo para atualizar.</pre>")

    usuario: Usuario = Usuario.query.get(user_id)

    if not usuario:
        raise LoginError("<pre>Usuário não encontrado.</pre>")

    nome = data.get("nome")
    email = data.get("email")
    tipo = data.get("tipo")
    senha = data.get("senha")

    if nome:
        usuario.nome = nome

    if email:
        existente = Usuario.query.filter_by(email=email).first()
        if existente and existente.id != usuario.id:
            raise LoginError("<pre>Já existe um usuário com esse email.</pre>")
        usuario.email = email

    if tipo:
        usuario.tipo = tipo

    if senha:
        usuario.change_password(senha)
    else:
        db.session.commit()

    return usuario
