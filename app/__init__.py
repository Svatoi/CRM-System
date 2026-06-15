import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv('.env')

from .models import db
from .auth import auth_bp
from .dashboard import dashboard_bp

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'plakiplaki')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), '../crm.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)

    return app