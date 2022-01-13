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
    # 指定した条件（検索ワード、検索件数）に一致するユーザ情報を取得
    search_word = '相互'
    search_results = api.search(q=search_word, count=30)
    cnt=0
    # 取得したユーザーを１件ずついいね、フォローしていく
    for result in search_results:

        status_id=result.id
        status_text=result.text
        user_name = result.user.name
        user_id = result.user.id
        #ミュートリスト取得
        muteList=api.mutes_ids()
        if cnt>0:
            break
        if not result._json["user"]["following"] and not result.id in muteList:
            try: # いいね
                api.create_favorite(status_id)
                print('Liked Status : ' + str(status_text))
                time.sleep(random.random()*15)
            except Exception as e:
                print(e)
            try: # フォロー
                api.create_friendship(user_id)
                print('Followed : ' + str(user_name) + '(@' + str(user_id) + ')')
                time.sleep(random.random()*15)
                api.create_mute(result.user.screen_name)
                print('muted:'+result.user.screen_name)
                time.sleep(random.random()*15)
            except Exception as e:
                print(e)
            cnt=cnt+1
    
    
if __name__ == '__main__':
#    if random.randint(1,10)>6:
    main()
