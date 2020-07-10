from app.ssp_module import ssp_app
from flask import render_template
from flask import request

@ssp_app.route('/')
@ssp_app.route('/index')
def index():
   return render_template('index.html')

@ssp_app.route('/login_page')
def login_():
	return render_template('login.html')

@ssp_app.route('/about')
def about():
	return render_template('about.html')

@ssp_app.route('/login', methods=['POST'])
def desk():
	if request.form:
		return redirect(url_for('about'))
	else: render_template('about.html')

@ssp_app.route('/ping', methods=['GET'])
def ping():
	"""check server connection"""
	return "pong"



