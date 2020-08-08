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
	if request.method == 'GET':
		return render_template('/desk/email_settings.html', title="Email Settings", form= form)
	elif request.method == 'POST':
		try:
			if form.validate_on_submit():
				email = EmailSetting(username = request.form.get('email'), email_server = 'smtp.gmail.com',
									email_port = request.form.get('mail_port'), mail_ttl = request.form.get('mail_tls'),
									mail_ssl = request.form.get('mail_ssl'))
				email.set_password(request.form.get('password'))
				db.session.add(email)
				db.session.commit()
				flash("Email Submitted Successfully", 'success')
			return render_template('/desk/email_settings.html', title="Email Settings", form= form)
		except Exception as e:
			flash("Something went wrong, please check log for more details", "danger")
			print(e)
			return render_template('/desk/email_settings.html', title="Email Settings", form= form)
