#!/usr/bin/python

import sys
import os
import ConfigParser

import sendmsg

if len(sys.argv) < 2:
    print "Twilio config file argument required"
    sys.exit(1)

cfg = sys.argv[1]
if not os.path.isfile(cfg):
    print cfg, "is not a valid config file"

config = ConfigParser.ConfigParser()
config.read(cfg)

sendmsg.sendMsg(config)        
