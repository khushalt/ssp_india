from app.ssp_module import ssp_app, login
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, login_required
from app.ssp_module.models import User
# from flask_babel import _

@ssp_app.route('/')
@ssp_app.route('/index')
def index():
   return render_template('index.html')

@ssp_app.route('/login_page')
def login_page():
	return render_template('login.html')

@ssp_app.route('/about')
def about():
	return render_template('about.html')

@ssp_app.route('/desk')
@login_required
def desk():
	return render_template('desk/desk_base.html')

@ssp_app.route('/ping', methods=['GET'])
def ping():
	return {"status":"pong"}

@ssp_app.route('/login', methods=['POST'])
def login():
	try:
		email, password = request.form.get('username'), request.form.get('password')
		user_ =  User.query.filter_by(email=email).first()
		if not User.query.filter_by(email=email).first() or not user_.check_password(password):
			flash('Invalid username or password')
			return redirect(url_for('login_page'))
		login_user(user_, remember=user_)
		return redirect(url_for('desk'))
	except Exception as e:
		raise e

@ssp_app.route('/logout', methods=['POST'])
@login_required
def logout():pass



