from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail	import Mail
from .api.route import api_bp
from .ssp_module.routes import ssp_bp
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import JWTManager
from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin()
jwt = JWTManager()
mail = Mail()
toolbar = DebugToolbarExtension()


mail_settings = {
	"MAIL_SERVER": 'smtp.gmail.com',
 	"MAIL_PORT": 465,
	"MAIL_USE_TLS": False,
	"MAIL_USE_SSL": True,
	"MAIL_USERNAME": 'khushal.t@domain.com',
	"MAIL_PASSWORD": '******'
}


def create_app():
	ssp_app = Flask(__name__, template_folder='./templates', static_folder='./static')
	ssp_app.config.from_object(Config)
	ssp_app.config.update(mail_settings)
	ssp_app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

	register_extensions(ssp_app)
	register_blueprints(ssp_app)
	configure_database(ssp_app)	
	return ssp_app

def register_extensions(app):
	db.init_app(app)
	migrate.init_app(app, db)
	login_manager.init_app(app)
	jwt.init_app(app)
	mail.init_app(app)
	# toolbar.init_app(app)
	from app.ssp_module import models

def register_blueprints(app):
	app.register_blueprint(ssp_bp)
	app.register_blueprint(api_bp)

def configure_database(app):
	
	@app.before_first_request
	def initialize_db():
		try:
			db.create_all()
		except Exception as e:
			print(e)

	@app.teardown_request
	def shutdown_session(exception=None):
		db.session.remove()




