from slackclient import SlackClient
import time
import os
import sys

token = 'token' # Put your slack token here

slack_client = SlackClient(token)

if slack_client.rtm_connect():
    defined_channel = "all"

    if len(sys.argv) > 1:
        defined_channel = str(sys.argv[1])

    print 'Currently listening on channel : ', defined_channel

    while True:
        events = slack_client.rtm_read()
        for event in events:
            print str(event)
            print event
            if (
                'channel' in event and
                'text' in event and
                event.get('type') == 'message'
            ):
                channel = event['channel']
                text = event['text']

                print str(channel)
                if defined_channel == "all" or defined_channel == str(channel):
                    try:
                        os.system("gtts-cli " + '"' + text.lower() + '"' + " -l 'fr' -o /tmp/test.mp3")
                        os.system("mpg123 /tmp/test.mp3")
                        os.system("rm /tmp/test.mp3")
                    except:
                        os.system("gtts-cli " + '"' + "Le dernier message contient des accents. Erreur"+ '"' + " -l 'fr' -o /tmp/test.mp3")
                        os.system("mpg123 /tmp/test.mp3")
                        os.system("rm /tmp/test.mp3")
        time.sleep(1)
else:
    print('Connection failed, invalid token?')
