import configparser

config = configparser.RawConfigParser()
config.read('Configuration/config.ini')


def get_username():
	return config.get(section='common info', option='username')


def get_password():
	return config.get(section='common info', option='password')


def get_url():
	return config.get(section='common info', option='base_url')