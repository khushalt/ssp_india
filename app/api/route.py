from flask import Blueprint, jsonify
from flask import request
from werkzeug.security import check_password_hash
from flask_jwt_extended import jwt_required, create_access_token

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/ping')
@jwt_required
def check_connection():
	return "pong"

@api_bp.route('/login', methods=['POST'])
def login_():
	from app.ssp_module.models import User
	username, password = request.form.get('username'), request.form.get('password')
	if not username or not password:
		return {'status':'error','message': 'Missing paramenters'}
	user_ =  User.query.filter_by(email=request.form.get('username')).first()
	
	if user_.check_password(password):
		token = create_access_token(identity=username)
		return {'status': 'success', 'token': token}, 200
	else: return {'status': 'error', 'message': 'Bad Credentails'}, 400
	
