from models.usermodel import Usuario
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from errors.login_error import LoginError

def login_user() -> dict:
    """
    Realiza o login de um usuário com base nos dados recebidos em uma requisição JSON da API.
    Gera e retorna um token JWT para autenticação nas próximas requisições.

    Requisição esperada (JSON):
    {
        "email": "usuario@exemplo.com",
        "senha": "minha_senha"
    }

    Returns:
        flask.Response: Um JSON contendo os dados do usuário e o token JWT.

    Raises:
        LoginError: Se os dados estiverem incorretos ou o usuário não existir.
    """
    data = request.json
    email = data.get("email")
    senha = data.get("senha")

    if not email or not senha:
        raise LoginError("<pre>Nem todos os campos foram preenchidos corretamente. Deveria se parecer com isso:\n{\n 'email':'user123'\n 'senha':'segredo'\n}</pre>")

    usuario: Usuario = Usuario.query.filter_by(email=email).first()

    if not usuario:
        raise LoginError("<pre>Ou usuário não existe</pre>")

    if not usuario.check_password(senha):
        raise LoginError("<pre>Senha incorreta</pre>")

    access_token = create_access_token(identity={"id": usuario.id, "tipo": usuario.tipo})

    return jsonify({
        "usuario": usuario.json(),
        "token": access_token
    }), 200
