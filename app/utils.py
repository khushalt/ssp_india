import random
import string
import datetime
from flask_jwt_extended import decode_token, create_access_token

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def get_reset_token(userid):
	expires = datetime.timedelta(days=365)
	return create_access_token(identity=userid, expires_delta = expires)

def decode_user_token(token):
	return decode_token(token)