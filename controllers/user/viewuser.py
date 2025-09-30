from models.usermodel import Usuario
from flask import request, jsonify
from errors.view_error import ViewError

def view_user_by_id() -> Usuario:
    """
    Retorna um usuário específico com base no ID fornecido via parâmetro na URL.

    Parâmetros esperados:
        - id (int): ID do usuário. Exemplo: /user?id=1

    Returns:
        flask.Response: JSON contendo os dados do usuário correspondente.

    Raises:
        ViewError: Se o parâmetro 'id' não for fornecido ou se o usuário não for encontrado.
    """
    user_id = request.args.get("id")
    if not user_id:
        raise ViewError("Parâmetro 'id' é obrigatório. Exemplo: /user?id=1")

    usuario = Usuario.query.get(user_id)
    if not usuario:
        raise ViewError(f"Usuário com ID {user_id} não encontrado.")

    return jsonify(usuario.json())


def view_user_by_name() -> list[Usuario]:
    """
    Retorna uma lista de usuários cujo nome contenha o valor informado no parâmetro da URL.

    Parâmetros esperados:
        - nome (str): Nome parcial ou completo do usuário. Exemplo: /user?nome=joao

    Returns:
        flask.Response: Lista JSON com os usuários encontrados.

    Raises:
        ViewError: Se 'nome' não for fornecido ou se nenhum usuário for encontrado.
    """
    nome = request.args.get("nome")
    if not nome:
        raise ViewError("Parâmetro 'nome' é obrigatório. Exemplo: /user?nome=joao")

    usuarios = Usuario.query.filter(Usuario.nome.ilike(f"%{nome}%")).all()
    if not usuarios:
        raise ViewError(f"Nenhum usuário encontrado com nome contendo '{nome}'.")

    return jsonify([user.json() for user in usuarios])


def view_user_by_role() -> list[Usuario]:
    """
    Retorna uma lista de usuários de acordo com o tipo (papel) informado.

    Parâmetros esperados:
        - tipo (str): Tipo do usuário (ex: 'aluno', 'admin', etc). Exemplo: /user?tipo=aluno

    Returns:
        flask.Response: Lista JSON dos usuários encontrados.

    Raises:
        ViewError: Se o parâmetro 'tipo' não for fornecido ou se nenhum usuário for encontrado.
    """
    tipo = request.args.get("tipo")
    if not tipo:
        raise ViewError("Parâmetro 'tipo' é obrigatório. Exemplo: /user?tipo=aluno")

    usuarios = Usuario.query.filter_by(tipo=tipo).all()
    if not usuarios:
        raise ViewError(f"Nenhum usuário do tipo '{tipo}' encontrado.")

    return jsonify([user.json() for user in usuarios])
