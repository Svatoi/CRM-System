import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv('.env')

from .auth import auth_bp
from .dashboard import dashboard_bp

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'plakiplaki')

    app.register_blueprint(dashboard_bp)
    app.register_blueprint(auth_bp)

    return app