#!/usr/bin/python

import sys
import os
import ConfigParser
import unittest
import random

from twilio.rest import TwilioRestClient 

import getawww

def _getRandomGreeting(greetings):
    return random.choice(greetings)

def _genTwilioPropFn(config):
    def get(prop):
        return config.get('twilio', prop)
    return get
 

###################
## PUBLIC INTERFACE

def sendMsg(config):
    twilioProps = _genTwilioPropFn(config)
    client = TwilioRestClient(
        twilioProps('ACCOUNT_SID'),
        twilioProps('AUTH_TOKEN'),
    )

    greetings = twilioProps('GREETINGS').split('|')
    body = '\n'.join([_getRandomGreeting(greetings), getawww.getAwww()])
 
    rc = client.messages.create( 
        to    = twilioProps('TEST_NUMBER'), 
        from_ = twilioProps('ACCOUNT_NUMBER'), 
        body  = body,
    )

#################
## TESTING

class SomeBasics(unittest.TestCase):
    
    def setUp(self):
        cfg = "test.cfg"
        self.assertTrue(os.path.isfile(cfg))

        config = ConfigParser.ConfigParser()
        config.read(cfg)        

        self.config = config

    def test_greeting(self):
        twilioProps = _genTwilioPropFn(self.config)
        greetings = twilioProps('GREETINGS').split('|')
        self.assertEqual(3, len(greetings))

        print _getRandomGreeting(greetings)

        greetingsSet = set()
        for i in range(10):
            greetingsSet.add(_getRandomGreeting(greetings))
        self.assertEqual(3, len(greetingsSet))

if __name__ == '__main__':
    unittest.main()






