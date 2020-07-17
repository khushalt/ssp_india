from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from app.api.route import api_bp
from flask_mail	import Mail


mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'khushal.t@demo.com',
    "MAIL_PASSWORD": '********'
}

ssp_app = Flask(__name__, template_folder='../templates', static_folder='../static')
ssp_app.config.update(mail_settings)
ssp_app.register_blueprint(api_bp)
ssp_app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
mail =  Mail(ssp_app)
login = LoginManager(ssp_app)
login.init_app(ssp_app)
ssp_app.config.from_object(Config)
db = SQLAlchemy(ssp_app)
migrate = Migrate(ssp_app, db)

from app.ssp_module import views, models, errors