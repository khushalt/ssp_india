from flask import Blueprint, render_template, flash, request
from flask_login import login_required
from .forms import EmailSettings
from app import delta

desk_bp = Blueprint('desk', __name__, url_prefix='/desk')

@desk_bp.route('/emailconfig', methods=['GET', 'POST'])
@login_required
def config_web():
	form = EmailSettings()
	if request.method == 'GET':
		return render_template('/desk/email_settings.html', title="Email Settings", form= form)
	elif request.method == 'POST':
		try:
			if form.validate_on_submit():
				delta.get_value("",filters={})
				flash("Email Submitted Successfully")
			return render_template('/desk/email_settings.html', title="Email Settings", form= form)
		except Exception as e:
			return render_template('/desk/email_settings.html', title="Email Settings", form= form)
