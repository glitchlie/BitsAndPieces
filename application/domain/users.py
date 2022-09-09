from datetime import datetime
from application.tools.generators import generate_alphanum_str

from werkzeug.security import generate_password_hash, check_password_hash


class User():
	def __init__(self, firstname, middlename, lastname, email, password, company):
		self.firstname = firstname
		self.middlename = middlename
		self.lastname = lastname
		self.email = email

		if password:
			self.set_password(password)

		self.company = company
		self.created_at = datetime.utcnow()


	def set_password(self, password):
		self.password_hash = generate_password_hash(password)


	def check_password(self, password):
		return check_password_hash(self.password_hash, password)


	def get_params(self):
		return (self.firstname, self.middlename, self.lastname, self.email, self.password_hash, self.created_at)


	def generate_id(self):
		self.id = generate_alphanum_str(16)


	def form_dict(self):
		user_dict = {
			"firstname": self.firstname,
			"middlename": self.middlename,
			"lastname": self.lastname,
			"email": self.email,
			"id": self.id,
			"company": self.company
		}

		return user_dict
