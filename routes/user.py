from . import Blueprint, jsonify, request
from models.User import User, UserSchema
from flask_jwt import jwt_required, current_identity

user_bp = Blueprint('user', __name__)
users = []


@user_bp.get("/users")
@jwt_required()
def get_all_users():
    return jsonify(UserSchema(many=True).dump(User.query.all()))


@user_bp.get("/user")
@jwt_required()
def hello_user():
    return jsonify(UserSchema().dump(current_identity))


@user_bp.post("/user")
def add_user():
    user = User(**request.get_json())
    user.add_user()
    return jsonify(request.get_json()), 201


@user_bp.delete("/user/<int:user_id>")
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    user.delete_user()
    return jsonify(UserSchema().dump(user))
