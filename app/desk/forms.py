from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email

class EmailSettings(FlaskForm):
	mail_server =  StringField('Email Server', validators=[DataRequired(), Length(min=2, max=20)])
	mail_port = StringField('Email Port', validators=[DataRequired()])
	mail_tls = BooleanField('Is Mail TLS')
	mail_ssl = BooleanField('Is Mail SSL')
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Submit')