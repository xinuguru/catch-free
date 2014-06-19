#!/usr/bin/env python

import urllib2, re, json, webbrowser, random, time

def isFree(url):
    SERVER_DATA = "its.serverData="
    time.sleep(random.random() * 100)
    html = urllib2.urlopen(url).read()
    jsobjects = re.findall("<script.*>(.*?)</script>", html)

    for jsobj in jsobjects:
        if jsobj.startswith(SERVER_DATA):
            serverData = json.loads(jsobj[len(SERVER_DATA):])
            return serverData["pageData"]["isFree"]

urls = [
    #"https://itunes.apple.com/kr/app/instaplace/id565105760?mt=8",
    "https://itunes.apple.com/kr/app/avplayer-mu-inkoding-sogdojojeol/id395680819?mt=8",
    "https://itunes.apple.com/kr/app/teoboseukaen-yeongsujeung/id342548956?mt=8",
    #"https://itunes.apple.com/kr/app/gwan-utd/id599900813?mt=8",
]


random.seed()
for url, free in zip(urls, map(isFree, urls)):
    if free:
        webbrowser.open(url, new=2, autoraise=True)
