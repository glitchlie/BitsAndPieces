from application.domain.users import User
from application.services.database import pg_adapter


def register_user(firstname, middlename, lastname, email, password, company):
	user = User(firstname, middlename, lastname, email, password, company)
	
	pg = pg_adapter()

	status = pg.add_user(user)

	return status
