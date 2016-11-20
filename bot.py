from configparser import SafeConfigParser

DATABASE_CONFIG_FILEPATH = __file__.strip('/bot.py') + r'credentials.cfg'


def credentials_parser(file_path=DATABASE_CONFIG_FILEPATH):
	parser = SafeConfigParser()
	parser.read(file_path)
	return parser


def get_jira_credentials(parser):
	"""Returns jira credentials"""
	return parser.get('jira', 'user'), parser.get('jira', 'pass')
