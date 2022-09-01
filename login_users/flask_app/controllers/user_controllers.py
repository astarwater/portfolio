from crypt import methods
from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user_models import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': request.form['password'],
        'confirm_password': request.form['confirm_password']
    }
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    data['pw_hash'] = pw_hash
    valid = User.validate_user(data)
    if valid:
        user = User.save(data)
        session['user_id'] = user
        return redirect('/user/success')
    if not User.validate_user(request.form):
        return redirect('/')
    User.save(request.form)
    return redirect('/')


@app.route('/user/success')
def success():
    if 'user_id' not in session:
        return redirect('/')
    return render_template('success.html')


@app.route('/login', methods=['POST'])
def login_user():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid email or password.")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid email or password.")
        return redirect('/')
    session['user_id'] = user.id
    return render_template('success.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
