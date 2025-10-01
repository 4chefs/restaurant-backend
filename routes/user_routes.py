from controllers import (
    create_user, 
    delete_user,
    update_user, 
    login_user, 
    view_user_by_id, 
    view_user_by_name, 
    view_user_by_role
)
from flask import Blueprint
from flask_jwt_extended import jwt_required

user_blueprint = Blueprint("user_bp", url_prefix="/user")

@user_blueprint.route("/create", methods=["POST"])
def call_create_user():
    return create_user()

@user_blueprint.route("/login", methods=["POST"])
def call_login_user():
    return login_user()

@user_blueprint.route("/id/<id>", methods=["GET"])
def call_get_by_id(id):
    return view_user_by_id(id)

@user_blueprint.route("/name/<name>", methods=["GET"])
def call_get_by_name(name):
    return view_user_by_name(name)

@user_blueprint.route("/role/<role>", methods=["GET"])
def call_get_by_role(role):
    return view_user_by_role(role)


@jwt_required()
@user_blueprint.route("/delete", methods=["DELETE"])
def call_delete_user():
    return delete_user()

@jwt_required()
@user_blueprint.route("/update", methods=["PUT"])
def call_update_user():
    return update_user()