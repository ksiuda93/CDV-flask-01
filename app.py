from flask import Flask, render_template
from models import db, ma, bc
from flask_jwt import JWT
from services.jwt_handler import authenticate, identity
from flask_caching import Cache


"""
Blueprint import
"""
from routes.user import user_bp
# from routes.home import home_bp


app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='cdv-secret-1234123',
    JWT_AUTH_HEADER_PREFIX="CDV",
    SQLALCHEMY_DATABASE_URI='mysql://cdv-app:tajneHaslo123@127.0.0.1/app',
    SQLALCHEMY_TRACK_MODIFICATIONS=True,
    SQLALCHEMY_ECHO=True,
    CACHE_TYPE="redis",
    CACHE_REDIS_URL="redis://127.0.0.1:6379/1"
)
db.init_app(app)
db.init_app(app)
ma.init_app(app)
bc.init_app(app)
cache = Cache(app)
jwt = JWT(app, authenticate, identity)


"""
Blueprint registration
"""

app.register_blueprint(user_bp, url_prefix="/api/v1")
# app.register_blueprint(home_bp)


@app.route("/")
# @cache.cached()
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
    app.run()