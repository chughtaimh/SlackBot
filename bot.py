import json

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

	def listen(self, type, command, interval=1):
		"""Opens socket connection to Slack API and listens for incoming events
		every :interval: seconds."""
		while True:
			try:
				msg = json.loads(self.server.websocket_safe_read())
				self.control_flow(msg, type, command)
			except WebSocketConnectionClosedException:
				self.connect(is_reconnect=True)

			time.sleep(interval)

	def control_flow(self, msg, type, command):
		"""Controls flow of events based on message :type:. If a message of type
		:type: is detected, :command: function is executed.
		args:
			msg 	-> dict		:	json message object from self.listen
			type 	-> str 		: 	message type
			command -> function	:	command to execute when :type: is detected
		"""
		if not msg: 						
			return
		elif msg['type'] != type:
			return
		else:
			command()
