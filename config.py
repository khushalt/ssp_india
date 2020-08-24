import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://rSZ52hcRBj:rRbMHS7oO9@localhost/flaskapp'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    secret_key = 'L8ZuiOeEQna8xyrAFYuDWFGXLeupB6V9M2-7PXgbGwA='

