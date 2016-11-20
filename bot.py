from configparser import SafeConfigParser
from slackclient import SlackClient

DATABASE_CONFIG_FILEPATH = __file__.strip('/bot.py') + r'credentials.cfg'


def credentials_parser(file_path=DATABASE_CONFIG_FILEPATH):
	"""Returns a credentials SafeConfigParser object from :file_path: 
	location."""
	parser = SafeConfigParser()
	parser.read(file_path)
	return parser
