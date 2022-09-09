from redis import Redis
from application.config import Config
import json


class redis_adapter:
	def __init__(self):
		self.read_conf()
		self.redis = Redis(host=self.host,
						   port=self.port)


	def read_conf(self):
		conf = Config()

		self.host = conf.redis_host
		self.port = conf.redis_port


	def set_session(self, cookie, user_obj):
		user_data = json.dumps(user_obj.form_dict())
		self.redis.set(cookie, user_data)


	def get_user_by_sesion_cookie(self, cookie):
		return self.redis.get(cookie)


	def delete_session(self, cookie):
		self.redis.delete(cookie)