from app.ssp_module import ssp_app, login, mail
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from app.ssp_module.models import User
from flask_mail import Message
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

@ssp_app.route('/forgot')
def forgot_password():
	return render_template('forgot_password.html')

@ssp_app.route('/desk')
@login_required
def desk():
	return render_template('desk/dashboard.html')

@ssp_app.route('/login', methods=['POST'])
def login():
	try:
		email, password = request.form.get('username'), request.form.get('password')
		user_ =  User.query.filter_by(email=email).first()
		if not User.query.filter_by(email=email).first() or not user_.check_password(password):
			flash('Invalid username or password')
			return redirect(url_for('login_page'))
		flash('Logged in successfully')
		login_user(user_, remember=user_)
		return redirect(url_for('desk'))
	except Exception as e:
		raise e

@ssp_app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login_page'))

@ssp_app.route('/forgot_password', methods=['POST'])
def sendnew_password():
	user_ =  User.query.filter_by(email=request.form.get('username')).first()
	if not user_:
		flash("Oops, it seems we dont have your account" , "danger")
		return redirect(url_for('forgot_password'))
	try:
		msg = Message("Hello",
			              sender=ssp_app.config.get('MAIL_USERNAME'),
			              recipients=["khushalt5@gmail.com"])
		mail.send(msg)
		flash("Password Instruction sent successfully", "success")
	except Exception as e:
		raise e
	return redirect(url_for('forgot_password'))


