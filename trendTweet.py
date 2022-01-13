#!/usr/bin/env python
# coding: utf-8

import time
import tweepy
import const
from Twitter import Twitter
import re
import random

def main():

    api=Twitter().getApi()
    results = api.trends_place(id = 23424856)
    preTwitterList = []
    for location in results:
            for trend in location["trends"]:
                    preTwitterList.append(re.sub('#', "", trend["name"]))

    tweetContent=""
    for i in preTwitterList:
        if len(tweetContent)<100:
            tweetContent=tweetContent+" #"+i

    print(tweetContent)
    api.update_status(tweetContent)

if __name__ == '__main__':
    main()




