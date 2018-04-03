from slackclient import SlackClient
import time
import os
import sys

token = ''
#token = ''

# dashboard       : C9Q9L695K
# decompte        : C9YJQEHGW
# general         : C0H56QDRA
# walkingmachine  : G0M1C8ND6

authorized_channels = ['C9Q9L695K','C9YJQEHGW', 'C0H56QDRA', 'G0M1C8ND6']




slack_client = SlackClient(token)

link = '<https://cdn.meme.am/instances/400x/33568413.jpg|That would be great>'

if slack_client.rtm_connect():
    defined_channel = "all"

    if len(sys.argv) > 1:
        defined_channel = str(sys.argv[1])

    print 'Currently listening on channel : ', defined_channel

    while True:
        events = slack_client.rtm_read()
        for event in events:
            #print str(event)
            #print event
            if (
                'channel' in event and
                'text' in event and
                event.get('type') == 'message'
            ):
                channel = event['channel']
                text = event['text']



                #print str(channel)
                if channel in authorized_channels:
                    try:
                        os.system("gtts-cli " + '"' + text.lower() + '"' + " -l 'fr' -o /tmp/test.mp3")
                        os.system("mpg123 /tmp/test.mp3")
                        os.system("rm /tmp/test.mp3")
                        print text.lower()
                    except:
                        os.system("gtts-cli " + '"' + "Le dernier message contient des accents. Erreur"+ '"' + " -l 'fr' -o /tmp/test.mp3")
                        os.system("mpg123 /tmp/test.mp3")
                        os.system("rm /tmp/test.mp3")
        time.sleep(1)
else:
    print('Connection failed, invalid token?')
