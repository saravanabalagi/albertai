def handle_command(slack_api, command, channel):
	"""
	Recieves commands directed for the bot, if they are valid perform action 
	else resends clarification
	"""
	message = handle_reply(command)
	slack_api.rtm_send_message(channel, message)

def handle_reply(command):
	EXAMPLE_COMMAND = 'do'
	message = None

	if command.lower().startswith(EXAMPLE_COMMAND) or command.lower().startswith('what'):
		message = 'Yes, code me further to do that!'
	elif command.lower().startswith('hi') or command.lower().startswith('hey') or command.lower().startswith('hello') or command.lower().startswith('who are you'):
		message = 'Hey, I\'m your personal assistant, how may I help you?'
	elif command.lower().startswith('are you alive'):
		message = 'Yes....! I am alive and doing fine :)'
	else:
		print('Invalid Command: Not Understood')
		message = 'Invalid Command: Not Understood'
	return message