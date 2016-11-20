"""Contains utility functions for SlackBot package."""


def get_jira_credentials(parser):
	"""Returns jira credentials."""
	return parser.get('jira', 'user'), parser.get('jira', 'pass')


def get_slack_token(parser):
	"""Returns slack token."""
	return parser.get('slack', 'token')
