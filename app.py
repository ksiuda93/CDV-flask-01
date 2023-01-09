from flask import Flask
from models import db, ma, bc
from flask_jwt import JWT
from services.jwt_handler import authenticate, identity


"""
Blueprint import
"""
from routes.user import user_bp
from routes.home import home_bp


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='cdv-secret-1234123',
    JWT_AUTH_HEADER_PREFIX="CDV",
    SQLALCHEMY_DATABASE_URI='mysql://cdv-app:tajneHaslo123@127.0.0.1/app',
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=True
)
db.init_app(app)
db.init_app(app)
ma.init_app(app)
bc.init_app(app)
jwt = JWT(app, authenticate, identity)


"""
Blueprint registration
"""

app.register_blueprint(user_bp, url_prefix="/api/v1")
app.register_blueprint(home_bp)


if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run()