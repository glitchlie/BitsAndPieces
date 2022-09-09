import psycopg2
from application.tools.generators import generate_alphanum_str
from application.tools.exceptions import emailExistsError, userNotExistsError, companyNotRegisteredError
from application.domain.users import User
from application.domain.companies import Company

from application.config import Config
import re
from datetime import datetime


class pg_adapter:
	def __init__(self):
		#self.logger = logging.getLogger("pg_logger")
		#self.logger.setLevel(logging.DEBUG)

		self.email_re = re.compile("Key \(email\)\=\(([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)\) already exists.")
		self.user_id_re = re.compile("Key \(user_id\)\=\(([a-zA-Z0-9]+)\) already exists.")
		self.advert_id_re = re.compile("Key \(advert_id\)\=\(([a-zA-Z0-9]+)\) already exists.")

		self.connect()


	def read_creds(self):
		conf = Config()
		self.creds = conf.get_db_config()


	def connect(self):
		self.read_creds()

		self.conn = psycopg2.connect(**self.creds)
		self.cur = self.conn.cursor()


	def generate_id(self, length):
		return generate_alphanum_str(length)


	def add_user(self, user):
		company_name = user.company
		company_obj = self.get_company_by_name(company_name)

		if company_obj:
			company_id = company_obj.id
			user_id = self.generate_id(16)
			# Insert user data
			query = """INSERT INTO 
					       d_user(user_id, firstname, middlename,
					              lastname, email, 
					              password_hash, created_at)
					   VALUES
					       (%s, %s, %s, %s, %s, %s, %s);"""
			try:
				self.cur.execute(query, (user_id, ) + user.get_params())

			except psycopg2.errors.UniqueViolation as unique_exception:
				msg_str = str(unique_exception)

				if self.email_re.search(msg_str):
					#self.logger.exception("User with such email exists!")
					return emailExistsError(user.email)

				elif self.user_id_re.search(msg_str):
					#self.logger.exception("User with such id exists!")

					self.add_user(user) # Prevent infinite recursion!

			# Insert conjunction data
			query = """INSERT INTO 
					       f_user_company(user_id, company_id,
					              		  conjunction_created, is_active)
					   VALUES
					       (%s, %s, %s, %s);"""

			self.cur.execute(query, (user_id, company_id, datetime.now(), True))

			self.conn.commit()
		else:
			return companyNotRegisteredError(company_name)


	def get_user(self, email):
		query = """SELECT
					   u.user_id,
				       u.firstname,
				       u.middlename,
				       u.lastname,
				       u.email,
				       u.password_hash,
				       u.created_at,
				       c.company_name
				   FROM
				   	   f_user_company AS u_c
				   LEFT JOIN
				       d_user AS u
				   ON
				       u_c.user_id = u.user_id
				   LEFT JOIN
				       d_company AS c
				   ON
				       u_c.company_id = c.company_id
				   WHERE
				       email = %s;"""
		try:
			self.cur.execute(query, (email, ))
			user_data = self.cur.fetchone()

			return self.make_user_obj(user_data)

		except:
			return None


	def make_user_obj(self, user_data):
		user_obj = User(user_data[1], 
						user_data[2], 
						user_data[3], 
						user_data[4], 
						None,
						user_data[7])
		user_obj.id = user_data[0]
		user_obj.password_hash = user_data[5]

		return user_obj


	def make_company_obj(self, company_data):
		print(company_data)
		company_obj = Company(company_data[1],
							  company_data[2],
							  company_data[3],
							  company_data[4],
							  company_data[5],
							  company_data[6])
		company_obj.id = company_data[0]

		return company_obj


	def get_company_by_name(self, company_name):
		query = """SELECT
				       company_id,
					   company_name,
					   company_description,
					   foundation_date,
					   itn,
					   psm,
					   address,
					   creation_date
				   FROM
				       d_company
				   WHERE
				       company_name = %s;"""
		try:
			self.cur.execute(query, (company_name, ))
			company_data = self.cur.fetchone()

			return self.make_company_obj(company_data)

		except:
			print("Error name")
			
			return None


	def add_advert(self, advert, user_id):
		advert_query = """INSERT INTO 
				              d_advert(advert_id, title, description,
				              		   price, creation_date, 
				              		   expires_in)
						  VALUES
				    		  (%s, %s, %s, %s, %s, %s);"""

		conj_query = """INSERT INTO 
				            f_user_advert(advert_id, 
				              			  user_id,
				              			  conjunction_created,
				              			  is_active)
						VALUES
				    		(%s, %s, %s, %s);"""

		advert_id = self.generate_id(16)
		
		try:
			self.cur.execute(advert_query, (advert_id, ) + (advert.get_params()))
			self.cur.execute(conj_query, (advert_id, user_id, datetime.now(), True))

			self.conn.commit()
			return advert_id

		except psycopg2.errors.UniqueViolation as unique_exception:
			msg_str = str(unique_exception)

			if self.advert_id_re.match(msg_str):
				self.logger.exception("Advert with such id exists!")
				
				self.add_advert(self, advert, user_id) # Prevent infinite recursion!


	def get_users_adverts(self, user_id):
		query = """SELECT
				       d_adv.advert_id,
				       d_adv.title,
				       d_adv.price,
				       array_agg(d_ph.full_filename) AS filenames
				   FROM
					   f_user_advert AS f_adv
				   LEFT JOIN
					   d_advert AS d_adv
				   ON
					   f_adv.advert_id = d_adv.advert_id
				   LEFT JOIN
					   f_advert_photo AS f_ph
				   ON
					   f_ph.advert_id = f_adv.advert_id
				   LEFT JOIN
					   d_photo AS d_ph
				   ON
					   f_ph.filename = d_ph.filename
				   WHERE
					   f_adv.user_id = %s
					   AND
					   f_adv.is_active = true
				   GROUP BY
				   	   d_adv.advert_id,
				   	   d_adv.title,
				   	   d_adv.price;"""
		
		self.cur.execute(query, (user_id, ))

		return self.cur.fetchall()


	def save_photos(self, filenames, filesizes, advert_id):
		photo_query = """INSERT INTO 
				         	 d_photo(filename, 
				         	 		 full_filename, 
				         	 		 filesize_bytes)
						 VALUES
				    		 (%s, %s, %s);"""

		conj_query = """INSERT INTO 
				            f_advert_photo(filename,
				              			   advert_id,
				              			   conjunction_created)
						VALUES
				    		(%s, %s, %s);"""

		for filename, filesize in zip(filenames, filesizes):
			self.cur.execute(photo_query, (filename.split(".")[0], filename, filesize, ))
			self.cur.execute(conj_query, (filename.split(".")[0], advert_id, datetime.now()))

		self.conn.commit()
