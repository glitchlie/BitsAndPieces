from os import path, stat


class Photo:
	def __init__(self, file, filename):
		self.file = file
		self.type = file.filename.split(".")[-1]
		self.filename = filename


	def save(self, filepath, idx=0):
		full_filepath = path.join(filepath, self.filename + "." + self.type)
		self.file.save(full_filepath)

		return self.filename + "." + self.type, stat(full_filepath).st_size