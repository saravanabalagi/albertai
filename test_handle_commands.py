from handle_commands import handle_reply

def test_handle_reply_string_reply():
	assert isinstance(handle_reply('hi'), str)
	assert isinstance(handle_reply('Hello!'), str)
	assert isinstance(handle_reply('How\'d you do'), str)