import random, string


def generate_alphanum_str(length):
		return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))


def generate_cookie_str(length):
		return ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + ".-") for _ in range(length))