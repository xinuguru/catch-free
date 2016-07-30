#!/usr/bin/env python
# coding: utf-8

import urllib2
import re
import json
import webbrowser
import random
import time

def isFree(url):
    time.sleep(random.random() * 100)
    html = urllib2.urlopen(url).read()
    jsobjects = re.findall("<script.*>its.serverData=(.*)</script>", html)

    if jsobjects:
        serverData = json.loads(jsobjects[0])
        return serverData["pageData"]["isFree"]

    return False

urls = [
    "https://itunes.apple.com/kr/app/teoboseukaen-yeongsujeung/id342548956?mt=8",
    # more itunes urls


random.seed()
for url in urls:
    if isFree(url):
        webbrowser.open(url, new=2, autoraise=True)
