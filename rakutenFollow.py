
#!/usr/bin/env python
# coding: utf-8

import time
import tweepy
import const
from Twitter import Twitter
import re
import random

def follow(api,search_results):

    # 取得したユーザーを１件ずついいね、フォローしていく
    ulist=[]
    cnt=0
    #ミュートリスト取得
    muteList=api.mutes_ids()
    for user in search_results:
        #ulist.append(result)
        #print(result)
        #user=api.get_user(result)
        if cnt>3:
            break
        #print(user)
        if not user._json["following"] and not user.id in muteList and not user.follow_request_sent:
            try: # フォロー
                api.create_friendship(user.id)
                print('Followed : ' + str(user.screen_name))
                time.sleep(random.random()*5)
                api.create_mute(user.screen_name)
                print('muted:'+user.screen_name)
                time.sleep(random.random()*5)
                cnt=cnt+1
            except Exception as e:
                print(e)


def main():
    api = Twitter().getApi()
    #search_results =tweepy.Cursor(api.followers, screen_name='RakutenJP', count=2).items()
    #follow(api,search_results)
    search_results2=tweepy.Cursor(api.followers, screen_name='AmazonJP', count=3).items()
    follow(api,search_results2)   
    # 取得したユーザーを１件ずついいね、フォローしていく
    ulist=[]
    cnt=0
    #ミュートリスト取得
    muteList=api.mutes_ids()
    for user in search_results:
        #ulist.append(result)
        #print(result)
        #user=api.get_user(result)
        if cnt>3:
            break
        #print(user)
        if not user._json["following"] and not user.id in muteList and not user.follow_request_sent:
            try: # フォロー
                api.create_friendship(user.id)
                print('Followed : ' + str(user.screen_name))
                time.sleep(random.random()*5)
                api.create_mute(user.screen_name)
                print('muted:'+user.screen_name)
                time.sleep(random.random()*5)
                cnt=cnt+1
            except Exception as e:
                print(e)
        
  
if __name__ == '__main__':
#    if random.randint(1,10)>6:
    main()