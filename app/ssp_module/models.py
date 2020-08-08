from app.app import db, login_manager
from app.app import create_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    email = db.Column(db.String(120), index=True, unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128),  nullable=True)
    creation = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=True)
    full_name = db.Column(db.String(180),  nullable=False)

    def __repr__(self):
        return 'User {}'.format(self.email) 

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return (self.email)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


