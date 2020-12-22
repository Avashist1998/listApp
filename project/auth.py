from .models import User
from flask import flash
from flask import request
from flask import url_for
from flask import redirect
from flask import Blueprint
from .extentions import sqlDB
from flask import render_template
from flask_login import login_user
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get('remember') else False
    user = User.query.filter_by(email=email).first()
    if user:
        if check_password_hash(user.password, password):
            login_user(user,remember=remember)
            return redirect(url_for('main.profile'))
        flash('Incorrect Password')
        return redirect(url_for('auth.login'))
    flash('Incorrect Email')
    return redirect(url_for('auth.login'))

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route("/signup", methods=["POST"])
def singup_post():
    email = request.form.get("email")
    name = request.form.get("name")
    password = request.form.get("password")
    user = User.query.filter_by(email=email).first()
    if user:
        flash('Email address already exists')
        return redired(user_for('auth.signup'))
    
    new_user = User(email=email, name=name, password=generate_password_hash(password,method='sha256'))
    sqlDB.session.add(new_user)
    sqlDB.session.commit()
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return "logout page"
    # return render_template("logout.html")