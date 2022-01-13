#!/usr/bin/env python
# coding: utf-8


import tweepy
import const

class Twitter:
    def __init__(self):
        self.CK=const.CK
        self.CS=const.CS
        self.AT=const.AT
        self.AS=const.AS

    def getApi(self):
        # Twitterオブジェクトの生成
        auth = tweepy.OAuthHandler(self.CK, self.CS)
        auth.set_access_token(self.AT, self.AS)
        api=tweepy.API(auth)
        return api
def main():
    api = Twitter().getApi()

    friends_id = []
    friends = tweepy.Cursor(api.friends_ids, screen_name='@rakuten_saleInf').pages

    for f in friends():
        friends_id.extend(f)
        
        followers_id = []
    followers = tweepy.Cursor(api.followers_ids, screen_name='@rakuten_saleInf').pages

    for i in followers():
        followers_id.extend(i)
        
    fuckList=list(set(friends_id)-set(followers_id))


    cnt=0
    for i in fuckList:
        if cnt<5:
            api.destroy_friendship(i)
            cnt+=1

if __name__ == '__main__':
    main()