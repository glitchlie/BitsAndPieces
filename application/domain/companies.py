from datetime import datetime
from application.tools.generators import generate_alphanum_str


class Company():
	def __init__(self, company_name, company_description, foundation_date, itn, psm, address):
		self.name = company_name
		self.description = company_description
		self.foundation_date = foundation_date
		self.itn = itn
		self.psm = psm
		self.address = address


	def get_params(self):
		return (self.name, self.description, self.foundation_date, self.itn, self.psm, self.address)


	def generate_id(self):
		self.id = generate_alphanum_str(16)
