from application.domain.users import User
from application.services.database import pg_adapter
from application.services.redis import redis_adapter
from application.tools.exceptions import emailExistsError, userNotExistsError, companyNotRegisteredError, wrongUserPassword

import json


def login_user(session_cookie, email, password):
	pg = pg_adapter()
	redis = redis_adapter()

	user = pg.get_user(email)

	if user:
		pwd_check = user.check_password(password)

		if pwd_check:
			redis.set_session(session_cookie, user)

			return user
		else:
			return wrongUserPassword(email)
	else:
		return userNotExistsError(email)


def check_user_login(session_cookie):
	pg = pg_adapter()
	redis = redis_adapter()

	user_data = redis.get_user_by_sesion_cookie(session_cookie)
	
	return json.loads(user_data)


def delete_session(session_cookie):
	redis = redis_adapter()
	redis.delete_session(session_cookie)
