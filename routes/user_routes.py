from controllers import (
    create_user, 
    delete_user,
    update_user, 
    login_user, 
    view_user_by_id, 
    view_user_by_name, 
    view_user_by_role
)
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from models.usermodel import Usuario

user_blueprint = Blueprint("user_bp", url_prefix="/user")

@user_blueprint.route("/create", methods=["POST"])
def call_create_user():
    user: Usuario = create_user()
    if user:
        return jsonify({
                "data": user.json(),
                "message":"Usuário criado com sucesso"
            }), 200

@user_blueprint.route("/login", methods=["POST"])
def call_login_user():
    data: dict = login_user()
    if data:
        return jsonify({
            "data": {
                "token": data["token"],
                "user": data["usuario"]
            },
            "message": "Login efetuado com sucesso"
        }), 200
        
@user_blueprint.route("/id/<id>", methods=["GET"])
def call_get_by_id(id):
    user : Usuario = view_user_by_id(id)
    if user:
        return jsonify({
            "data": user,
            "message": "Usário encontrado"
        })

@user_blueprint.route("/name/<name>", methods=["GET"])
def call_get_by_name(name):
    users : list[Usuario] = view_user_by_name(name)
    if users:
        user_list = [user.json() for user in users]
        return jsonify({
            "data": user_list,
            "message": f"{len(users)} Usuários com nome {name} encontrados"
        })

@user_blueprint.route("/role/<role>", methods=["GET"])
def call_get_by_role(role):
    users : list[Usuario] = view_user_by_role(role)
    if users:
        user_list = [user.json() for user in users]
        return jsonify({
            "data": user_list,
            "message": f"{len(users)} Usuários com role {role} encontrados"
        })


@jwt_required()
@user_blueprint.route("/delete/<id>", methods=["DELETE"])
def call_delete_user(id):
    user: Usuario = delete_user(id)
    if user:
        return jsonify({
            "data": user.json(),
            "message": f"Usuário {user.id} apagado com sucesso"
        })

@jwt_required()
@user_blueprint.route("/update/<id>", methods=["PUT"])
def call_update_user(id):
    user: Usuario = update_user(id)
    if user:
        return jsonify({
            "data": user.json(),
            "message": f"Usuário {user.id} atualizado com sucesso"
        })