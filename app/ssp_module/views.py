from app.ssp_module import ssp_app
from flask import render_template

@ssp_app.route('/')
@ssp_app.route('/index')
def index():
   return render_template('index.html')

@ssp_app.route('/login')
def login():
	return render_template('login.html')

@ssp_app.route('/about')
def about():
	return render_template('about.html')
