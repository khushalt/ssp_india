# from app import ssp_app, mail
from app.ssp_module.models import User
from app.app import create_app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, login_required, logout_user
from flask_mail import Message
from flask import Blueprint
from app.utils import get_reset_token, decode_user_token, send_mail

ssp_bp = Blueprint('ssp', __name__, url_prefix='/')

@ssp_bp.route('/')
@ssp_bp.route('/index')
def index():
	return render_template('index.html')

@ssp_bp.route('/login_page')
def login_page():
	return render_template('login.html')

@ssp_bp.route('/about')
def about():
	return render_template('about.html')

@ssp_bp.route('/forgot')
def forgot_password():
	return render_template('forgot_password.html')

@ssp_bp.route('/contact')
def contact_us():
	return render_template('contact.html')

@ssp_bp.route('/desk')
@login_required
def desk():
	return render_template('desk/dashboard.html')

@ssp_bp.route('/login', methods=['POST'])
def login():
	try:
		email, password = request.form.get('username'), request.form.get('password')
		user_ =  User.query.filter_by(email=email).first()
		if not User.query.filter_by(email=email).first() or not user_.check_password(password):
			flash('Invalid username or password')
			return redirect(url_for('login_page'))
		flash('Logged in successfully')
		login_user(user_, remember=user_)
		return redirect(url_for('ssp.desk'))
	except Exception as e:
		return redirect(url_for('ssp.login_page'))

@ssp_bp.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('ssp.login_page'))

@ssp_bp.route('/forgot_password', methods=['POST'])
def sendnew_password():
	from app.app import mail, create_app
	user =  User.query.filter_by(email=request.form.get('username')).first()
	if not user:
		flash("Oops, it seems we dont have your account" , "danger")
		return redirect(url_for('ssp.forgot_password'))
	try:
		token = request.url_root + "/verify/"+ token_details(create_app, request.form.get('username')) 
		send_mail(subject="Password Reset Instruction", 
				recipients=[request.form.get('username')], template = 'reset_password_mail.html',
				data={'user': user.full_name, 'token': token}, flash_msg="Password intruction sent successfully")	
	except Exception as e:
		raise e
	return redirect(url_for('ssp.forgot_password'))

def token_details(app, user):
	token = {'data': user, 'key': app().secret_key}
	return get_reset_token(token)

@ssp_bp.route('/verify/<token>', methods=['GET', 'POST'])
def verify_token(token):
	try:
		decode, app = decode_user_token(token), create_app()
		if decode.get('identity').get('key') == app.secret_key and request.method == 'GET':
			return render_template('reset_password.html')
		elif decode.get('identity').get('key') == app.secret_key and request.method == 'POST':
			user = decode.get('identity').get('data')	
			user =  User.query.filter_by(email=user).first()
			user.set_password(request.form.get('password'))
			db.session.add(user)
			db.session.commit()
			flash("Password has been set successfully", "success")
			return render_template('reset_password.html')
	except Exception as e:
		raise e


	

	
