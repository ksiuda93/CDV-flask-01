from . import Blueprint, jsonify, request
from models.User import User, UserSchema
from flask_jwt import jwt_required, current_identity
from services import redis_handler, rabbit_handler

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
    if user.add_user():
        data = request.get_json()
        email = data['email']
        redis_handler.create_msg('api-email', email)
        rabbit_handler.create_msg('pl-api-email', email)
        return jsonify(request.get_json()), 201
    else:
        return jsonify({"Error": "Endpoint error!"}), 404


@user_bp.delete("/user/<int:user_id>")
@jwt_required()
def delete_user(user_id):
    user = User.query.get(user_id)
    user.delete_user()
    return jsonify(UserSchema().dump(user))
