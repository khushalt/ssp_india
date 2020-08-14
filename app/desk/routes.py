from flask import Blueprint, render_template, flash, request
from flask_login import login_required
from .forms import EmailSettings
from app import delta
from .models import EmailSetting
from app.app import db

desk_bp = Blueprint('desk', __name__, url_prefix='/desk')

@desk_bp.route('/emailconfig', methods=['GET', 'POST'])
@login_required
def eamil_config():
	form = EmailSettings()
	is_email = EmailSetting.query.all()
	if request.method == 'GET':
		if is_email:
			email_ = EmailSetting.query.filter_by(username=is_email[0].username).first()
			return render_template('/desk/email_settings.html', title="Email Settings", form= form, values= email_)
	elif request.method == 'POST':
		try:
			if form.validate_on_submit():
				if not is_email:
					email = EmailSetting(username = request.form.get('email'), email_server = 'smtp.gmail.com',
										email_port = request.form.get('mail_port'), mail_ttl = 1 if request.form.get('mail_tls') else 0,
										mail_ssl = 1 if request.form.get('mail_ssl') else 0)
					email.set_password(request.form.get('password'))
					db.session.add(email)
					db.session.commit()
					flash("Email Submitted Successfully", 'success')
				else:
					email_ = EmailSetting.query.filter_by(username=is_email[0].username).first()
					update_email(email_)
					flash("Document updated successfully","success")
			return render_template('/desk/email_settings.html', title="Email Settings", form= form, values= email_)
		except Exception as e:
			flash("Something went wrong, please check log for more details", "danger")
			print(">>>>>",e)
			return render_template('/desk/email_settings.html', title="Email Settings", form= form)

def update_email(email_):
	#pass email object it will save to db
	email_.username = request.form.get('email')
	email_.email_port = request.form.get('mail_port')
	email_.mail_ssl = 1 if request.form.get('mail_ssl') else 0
	email_.mail_ttl = 1 if request.form.get('mail_tls') else 0
	email_.set_password(request.form.get('password'))
	db.session.commit()