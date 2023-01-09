from models.User import User
from models import bc


def authenticate(username, password):
    user = User.query.filter(User.username == username).first()
    if bc.check_password_hash(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)
