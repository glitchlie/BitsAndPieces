class Config:
	def __init__(self):
		# DATABASE
		self.database_host = "db_host"
		self.database_database = "db_name"
		self.database_user = "db_user"
		self.database_password = "db_password"
		# REDIS
		self.redis_host = "redis_host"
		self.redis_port = "redis_port"
		# FILE STORAGE
		self.file_storage_storage_path = "files_path"


	def get_db_config(self):
		creds = {
			"host": self.database_host,
			"database": self.database_database,
			"user": self.database_user,
			"password": self.database_password
		}

		return creds


	def get_file_storage_config(self):
		cfg = {
			"storage_path": self.file_storage_storage_path
		}

		return cfg
