# from flask import Flask
# from config import Config
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import click
# # from flask_login import LoginManager
# # from flask_mail	import Mail
# # from flask_jwt_extended import JWTManager
# from .api.route import api_bp
# from .ssp_module.routes import ssp_bp
# from .import cli


# # mail_settings = {
# #     "MAIL_SERVER": 'smtp.gmail.com',
# #     "MAIL_PORT": 465,
# #     "MAIL_USE_TLS": False,
# #     "MAIL_USE_SSL": True,
# #     "MAIL_USERNAME": 'khushal.t@demo.com',
# #     "MAIL_PASSWORD": '********'
# # }

# ssp_app = Flask(__name__, template_folder='./templates', static_folder='./static')
# ssp_app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# ssp_app.register_blueprint(ssp_bp)
# ssp_app.register_blueprint(api_bp)
# ssp_app.config.from_object(Config)
# db = SQLAlchemy(ssp_app)
# migrate = Migrate(ssp_app, db)

# ssp_app.cli.add_command(cli.new_site)
# # ssp_app.config.update(mail_settings)
# # jwt = JWTManager(ssp_app)
# # mail =  Mail(ssp_app)
# # login = LoginManager(ssp_app)
# # login.init_app(ssp_app)


# # @ssp_app.route('/')
# # def index():
# # 	from flask import render_template
# # 	return render_template('index.html')


# # from . import cli
# # print("#####")
