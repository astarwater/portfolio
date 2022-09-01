from email import message
from flask import flash
from crypt import methods
from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user_models import User
from flask_app.models.message_models import Message
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
        user = User.add_user(data)
        session['user_id'] = user
        return redirect('/dashboard')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid email or password.")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid email or password.")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    user = User.get_one({'id': session['user_id']})
    recipients = User.get_all_users()
    message = Message.get_message({'id': session['user_id']})
    sent = Message.sent_message_count({'id': session['user_id']})
    return render_template('dashboard.html', user=user, recipients=recipients, message=message, sent=sent)

@app.route('/send_message', methods=['POST'])
def send_message():
    Message.send_message(request.form)
    return redirect('/dashboard')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/delete/<int:message_id>')
def delete(message_id):
    data = {
        'id': message_id
    }
    Message.delete_message(data)
    return redirect('/dashboard')