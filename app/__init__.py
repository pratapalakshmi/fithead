from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .models import db
import os


def create_app():
    app = Flask(__name__)

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'DATABASE_URL', 'postgresql://postgres:password@localhost:5432/postgres')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # JWT configuration
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'SecretKey')  # Change this in production
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600  # 1 hour

    db.init_app(app)
    migrate = Migrate(app, db)
    jwt = JWTManager(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
