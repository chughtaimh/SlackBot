import argparse
import os

from configparser import SafeConfigParser, DuplicateSectionError

CURRENT_DIRECTORY = os.path.dirname(__file__)
DATABASE_CONFIG_FILEPATH = CURRENT_DIRECTORY + "credentials.cfg"


def setup():
	arg_parser = argparse.ArgumentParser()
	arg_parser.add_argument("token", 	 help="Insert slack token   >>")
	arg_parser.add_argument("jira_user", help="Insert jira username >>")
	arg_parser.add_argument("jira_pass", help="Insert jira password >>")
	args = arg_parser.parse_args()

	cfg_parser = SafeConfigParser()
	cfg_parser.read(DATABASE_CONFIG_FILEPATH)

	cfg_parser.add_section('slack')
	cfg_parser.set('slack', 'token', args.token)

	cfg_parser.add_section('jira')
	cfg_parser.set('jira', 'user', args.jira_user)
	cfg_parser.set('jira', 'pass', args.jira_pass)

	with open(DATABASE_CONFIG_FILEPATH, 'w') as config_file:
		cfg_parser.write(config_file)


if __name__ == '__main__':
	setup()
