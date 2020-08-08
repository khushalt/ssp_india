from app.app import db
from werkzeug.security import generate_password_hash, check_password_hash


class EmailSettings(db.Model):
    username = db.Column(db.String(120), index=True, unique=True, nullable=False, primary_key=True)
    password_hash = db.Column(db.String(128),  nullable=True)
    email_server = db.Column(db.String(120), index=True, unique=True, nullable=False)
    email_port = db.Column(db.String(120), index=True, unique=True, nullable=False)
    mail_ttl = db.Column(db.Boolean())
    mail_ssl = db.Column(db.Boolean())
    creation = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime, nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)