from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail	import Mail
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import JWTManager
import traceback

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin()
jwt = JWTManager()
mail = Mail()


mail_settings = {
	"MAIL_SERVER": 'smtp.gmail.com',
 	"MAIL_PORT": 465,
	"MAIL_USE_TLS": False,
	"MAIL_USE_SSL": True,
	"MAIL_USERNAME": 'khushal.t@indictranstech.com',
	"MAIL_PASSWORD": "testpassword"
}


def create_app():
	ssp_app = Flask(__name__, template_folder='./templates', static_folder='./static')
	ssp_app.config.from_object(Config)
	ssp_app.secret_key = '_5#y2L"F4Q8z\n\xec]/'
	# ssp_app.config.update(mail_settings)

	register_extensions(ssp_app)
	register_blueprints(ssp_app)
	configure_database(ssp_app)	
	return ssp_app

def register_extensions(app):
	db.init_app(app)
	migrate.init_app(app, db)
	login_manager.init_app(app)
	jwt.init_app(app)
	app.config.update(import_mail_settings(app)) #post extension operation
	mail.init_app(app)
	from app.ssp_module import models
	from app.desk import models

def register_blueprints(app):
	from .ssp_module.routes import ssp_bp
	from .api.route import api_bp
	from .desk.routes import desk_bp
	app.register_blueprint(ssp_bp)
	app.register_blueprint(api_bp)
	app.register_blueprint(desk_bp)

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

def import_mail_settings(app):
	with app.app_context():
		from app.desk.models import EmailSetting
		from app.utils import get_decryption
		email = EmailSetting.query.one()
		dict_ = {
			"MAIL_SERVER": email.email_server,
		 	"MAIL_PORT": email.email_port,
			"MAIL_USE_TLS": email.mail_ttl,
			"MAIL_USE_SSL": email.mail_ssl,
			"MAIL_USERNAME": email.username,
			"MAIL_PASSWORD": get_decryption(email.password_hash)
		}
		mail_settings = {
			"MAIL_SERVER": 'smtp.gmail.com',
		 	"MAIL_PORT": 465,
			"MAIL_USE_TLS": False,
			"MAIL_USE_SSL": True,
			"MAIL_USERNAME": 'khushal.t@indictranstech.com',
			"MAIL_PASSWORD": "testpassword"
		}
		print("****************",dict_,mail_settings)
		return dict_




