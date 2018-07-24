import connection_helper

def test_can_connect():
	slack_api = connection_helper.connect()
	assert slack_api.rtm_connect() is True