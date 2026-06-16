from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'admin':
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('Incorrect username or password', 'danger')

    return render_template('auth/login.html')

@auth_bp.route('/logout')
def logout():
    flash('You have successfully logged out', 'info')
    return redirect(url_for('auth.login'))