import time
import connection_helper

from handle_commands import handle_command

if __name__ == '__main__':
	"""
	Initiate the bot and call appropriate handler functions
	"""
	READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
	slack_api = connection_helper.connect()
	if slack_api.rtm_connect():
		print('SLACK_BOT connected and running')
		while True:
			command, channel = connection_helper.parse_slack_response(slack_api.rtm_read())
			if command and channel:
				handle_command(slack_api, command, channel)
			time.sleep(READ_WEBSOCKET_DELAY)
	else:
		print('Connection failed. Invalid Slack token or bot ID?') 