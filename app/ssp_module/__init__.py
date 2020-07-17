from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


ssp_app = Flask(__name__, template_folder='../templates', static_folder='../static')
ssp_app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login = LoginManager(ssp_app)
login.init_app(ssp_app)
ssp_app.config.from_object(Config)
db = SQLAlchemy(ssp_app)
migrate = Migrate(ssp_app, db)

from app.ssp_module import views, models, errors