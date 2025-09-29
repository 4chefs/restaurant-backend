from models.usermodel import Usuario
from errors.create_error import CreateError
from flask import request, jsonify
from werkzeug.security import generate_password_hash

def create_user() -> Usuario:
    """
    Cria um novo usuário com base nos dados recebidos em uma requisição JSON da API.

    A requisição deve conter os seguintes campos no corpo (JSON):
        - nome (str): Nome do usuário.
        - email (str): E-mail do usuário.
        - senha (str): Senha de acesso do usuário.
        - tipo (str): Tipo do usuário (ex: 'aluno', 'admin', etc).

    Returns:
        flask.Response: Um objeto JSON contendo os dados do novo usuário.

    Raises:
        CreateError: Se algum campo obrigatório estiver ausente ou se ocorrer
                     um erro ao criar o usuário.
    """
    data = request.json
    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")
    tipo = data.get("tipo")
    
    if not nome or not email or not senha or not tipo:
        raise CreateError("<pre>Nem todos os campos foram preenchidos corretamente. Deveria se parecer com isso:\n{\n 'nome':'user123'\n 'email':'email@email.com'\n 'senha':'segredo'\n 'tipo':'aluno'\n}</pre>")
    
    senha_hash = generate_password_hash(senha)
    novo_usuario = Usuario(nome=nome, email=email, senha=senha_hash, tipo=tipo)
    if not novo_usuario:
        raise CreateError("<pre>Erro ao criar o usuário (erro interno do backend)<pre>")
    
    return jsonify(novo_usuario.json())