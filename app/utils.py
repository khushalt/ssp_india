import random
import string
import datetime
from flask_jwt_extended import decode_token, create_access_token
from app.app import mail, create_app
from flask_mail import Message
from flask import render_template, flash
import traceback


def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def get_reset_token(userid):
	expires = datetime.timedelta(days=365)
	return create_access_token(identity=userid, expires_delta = expires)

def decode_user_token(token):
	return decode_token(token)

def send_mail(subject, recipients, flash_msg = 'Mail Sent',body = None, template= None, data=None):
	"""
	param: subject- Subject of the mail
	param: recipients is list of recipients to send the mail
	param: body if required can be rendered as part of tamplate or simple body content
	param: tamplate is html file path to be rendered on the mail
	param: data is data support to template
	"""
	
	try:
		msg = Message(subject,
				    sender = create_app().config.get('MAIL_USERNAME'),
				    recipients= recipients)
		if body: msg.body = body
		if template: 
			msg.html = render_template('reset_password_mail.html',data=data)
		mail.send(msg)
		flash(flash_msg, "success")
	except Exception as e:
		print(">>>>>>",e,traceback.print_exc())
		flash("Please check with the Settings", "danger")