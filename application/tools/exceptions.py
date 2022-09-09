class emailExistsError(Exception):
	def __init__(self, email):
		self.email = email


	def __str__(self):
		return f"User with email {self.email} already exists"


class companyNotRegisteredError:
	def __init__(self, company_name):
		self.company_name = company_name


	def __str__(self):
		return f"Company {self.company_name} is not registered"


class userNotExistsError:
	def __init__(self, email):
		self.email = email


	def __str__(self):
		return f"User with email {self.email} does not exist"


class wrongUserPassword:
	def __init__(self, email):
		self.email = email


	def __str__(self):
		return f"Wrong password for user with email {self.email}"