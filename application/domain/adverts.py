from datetime import datetime, timedelta


class Advert:
	def __init__(self, title, description, price):
		self.title = title
		self.description = description
		self.price = price


	def set_creation_date(self):
		self.creation_date = datetime.utcnow()


	def set_expiration_date(self, delta_seconds):
		self.expiration_date = self.creation_date + timedelta(seconds=delta_seconds)


	def get_params(self):
		return (self.title, self.description, self.price, self.creation_date, self.expiration_date)