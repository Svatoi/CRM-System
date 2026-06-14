from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return "<h1>LOGIN</h1>"

@auth_bp.route('/logout')
def logout():
    return "<h1>LOGOUT</h1>"