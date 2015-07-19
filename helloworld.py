import sys
import os
import ConfigParser
from twilio.rest import TwilioRestClient 

def genTwilioPropFn(config):
    def get(prop):
        return config.get('twilio', prop)
    return get
 
if len(sys.argv) < 2:
    print "Twilio config file argument required"
    sys.exit(1)

cfg = sys.argv[1]
if not os.path.isfile(cfg):
    print cfg, "is not a valid config file"

config = ConfigParser.ConfigParser()
config.read(cfg)

twilioProps = genTwilioPropFn(config)
client = TwilioRestClient(
    twilioProps('ACCOUNT_SID'),
    twilioProps('AUTH_TOKEN'),
)
 
rc = client.messages.create( 
    to    = twilioProps('TEST_NUMBER'), 
    from_ = twilioProps('ACCOUNT_NUMBER'), 
    body  = "hello, world",  
)

print "rc:", str(rc)
