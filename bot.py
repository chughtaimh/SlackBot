from utils import get_slack_token
from configparser import SafeConfigParser
from slackclient import SlackClient

DATABASE_CONFIG_FILEPATH = __file__.strip('/bot.py') + r'credentials.cfg'


def credentials_parser(file_path=DATABASE_CONFIG_FILEPATH):
	"""Returns a credentials SafeConfigParser object from :file_path: 
	location."""
	parser = SafeConfigParser()
	parser.read(file_path)
	return parser


class SlackBot(SlackClient):

	"""Main SlackBot class that extends slackclient.SlackClient"""

	def __init__(self, token):
		"""token = Slack API token"""
		super(SlackBot, self).__init__(token)

	def talk(self, as_user=True, **kwargs):
		"""Makes a chat post message api call to slack.
		Args:
				as_user -> bool	:	Whether or not to include the bot's profile in
														the message
				channel -> str 	:	channel to post message to
				text	-> str 	: 	Message to send
		"""
		return self.api_call('chat.postMessage', as_user=as_user, **kwargs)

	def connect(self, is_reconnect=False):
		"""Connects to Slack API. Set is_reconnect to True in case of 
		timeout."""
		return self.rtm_connect(is_reconnect)
