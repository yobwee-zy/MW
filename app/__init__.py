from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Base directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Configuration
    app.config['SECRET_KEY'] = 'unlocking-potential'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB
    db.init_app(app)

    # Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app