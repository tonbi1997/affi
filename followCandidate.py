#!/usr/bin/env python
# coding: utf-8


import tweepy
import const
from Twitter import Twitter
def main():
    api = Twitter().getApi()

    followerList=[]
    cursor = -1
    cnt=0
    while cursor != 0:
        api = Twitter().getApi()
        itr = tweepy.Cursor(api.friends_ids, id='@RakutenJP"', cursor=cursor).pages()
        
        try:
            for friends_ids in itr.next():
                if cnt>1000:
                    break            
                try:
                    user = api.get_user(friends_ids)
                    user_info = [user.screen_name]
                    if user.followers_count<user.friends_count:
                        followerList.append(user_info)
                        cnt=cnt+1
                except tweepy.error.TweepError as e:
                    print(e.reason)
                    break
        except ConnectionError as e:
            print(e.reason)
        cursor = itr.next_cursor


    with open('followCandidate.txt', 'w') as f:
        for user in followerList:
            f.write("%s\n" % user[0])
            
    f.close()

    with open('followCandidate.txt') as f:
        l = f.readlines()
        print(type(l))
        print(l)
    f.close()


if __name__ == '__main__':
    main()
