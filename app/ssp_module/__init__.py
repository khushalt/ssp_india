from flask import Flask

ssp_app = Flask(__name__, template_folder='../templates', static_folder='../static')

from app.ssp_module import views