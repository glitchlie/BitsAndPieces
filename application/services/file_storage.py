from application.domain.photo import Photo
import os
import yaml
#import logging
from os import path

from application.config import Config


class file_storage:
	def __init__(self):
		#self.logger = logging.getLogger("file_storage_logger")
		#self.logger.setLevel(logging.DEBUG)

		self.config = None
		self.read_config()


	def read_config(self):
		cfg = Config()
		self.config = cfg.get_file_storage_config()


	def create_save_path(self):
		if self.config and not os.exists(self.config["storage_path"]):
			os.mkdir(self.config["storage_path"], parents=True)


	def save_photos(self, photos, advert_id):
		filenames = list()
		filesizes = list()

		for idx, photo in enumerate(photos):
			photo_obj = Photo(photo, advert_id + "_" + str(idx))
			
			filename, filesize = photo_obj.save(self.config["storage_path"])
			filenames.append(filename)
			filesizes.append(filesize)

		return filenames, filesizes


	def get_save_path(self):
		return self.config["file_storage"]["storage_path"]