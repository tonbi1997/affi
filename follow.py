#!/usr/bin/env python
# coding: utf-8

import time
import tweepy
import const
from Twitter import Twitter
import re
import random

def main():
    api = Twitter().getApi()
    with open('followCandidate.txt') as f:
        l = f.readlines()

    f.close()

    followList=[]
    for user in l:
        match = re.search(r'[a-zA-Z0-9]*', user)
        followList.append(match.group(0))
    
    print(followList)
    
    cnt=0
    while cnt<10:
        try:
            if api.get_user(followList[cnt]) is not None:
                api.create_friendship(followList[cnt])
                print('get')
        except:
            print('miss')
        followList.pop(cnt)
        cnt=cnt+1
        time.sleep(random.random()*3)
    with open('followCandidate.txt', 'w') as f:
        for user in followList:
            f.write("%s\n" % user)
            
    f.close()

if __name__ == '__main__':
    main()
