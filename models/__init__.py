from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from sqlalchemy import exc

db = SQLAlchemy()
ma = Marshmallow()
bc = Bcrypt()