#!/usr/bin/python

import subprocess
import os
import sys
from bs4 import BeautifulSoup

def _getImgurLink(titleDoc):
    for link in titleDoc.find_all('a'):
        return link['href']

# yea this is likely to break
def _readFirstLink(rawDoc):
    soup = BeautifulSoup(rawDoc, 'html.parser')

    for title in soup.find_all('p'):
        titleClass = title.get('class', None)
        if not titleClass:
            continue

        titleClass = ' '.join(titleClass)
        if "title" != titleClass:
            continue

        for domain in title.find_all('span'):
            for link in domain.find_all('a'):
                if "imgur" in link["href"]:
                    return _getImgurLink(title)

###################
## PUBLIC INTERFACE

def getAwww():
    p = subprocess.Popen(["curl", "http://www.reddit.com/r/Awww/hot?limit=10"], 
                         stdout=subprocess.PIPE)
    out, rc = p.communicate()
    p.wait()    
    return _readFirstLink(out)

##############
## TESTING

if __name__ == "__main__":
    print getAwww()
