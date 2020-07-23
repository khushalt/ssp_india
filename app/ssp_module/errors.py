from flask import render_template
from app.ssp_module import create_app

@create_app().errorhandler(404)
def not_found_error(error):
    return render_template('error/404.html'), 404