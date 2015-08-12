import subprocess
import os
import sys
from HTMLParser import HTMLParser

TAG = "entry unvoted"

p       = subprocess.Popen(["curl", "http://www.reddit.com/r/Awww/hot?limit=10"], 
                           stdout=subprocess.PIPE)
out, rc = p.communicate()
p.wait()

class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.traversingInterestingItem = False

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if 'class' in d and d['class'] == 'entry unvoted':
            print self.get_starttag_text()

    def handle_endtag(self, tag):
        pass
            
        # if TAG == tag:
        #     print "Encountered an end tag :", tag
    # def handle_data(self, data):
    #     print "Encountered some data  :", datax

parser = MyHTMLParser()
parser.feed(out)

#print out
