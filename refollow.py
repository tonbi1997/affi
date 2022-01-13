import time
import tweepy
import const
from Twitter import Twitter
import re
import random

def intersect_list(lst1, lst2):

    lst2 = lst2.copy()
    for element in lst2:
        try:
            lst2.remove(element)
        except ValueError:
            continue
        else:
            print(element)
            #print("love each other")
    return lst2

def main():
    api = Twitter().getApi()
    twitterId="@rakuten_saleInf"

    followers = api.followers_ids(twitterId)
    friends = api.friends_ids(twitterId)
    following_me_list = intersect_list(friends, followers)
    cnt=0
    for f in following_me_list:
        if api.get_user(f).followers_count>api.get_user(f).friends_count*0.8:
            if cnt<10:
                time.sleep(random.random()*5)
                print("ID:{}のフォローしました。".format(api.get_user(f).screen_name))
                api.create_friendship(f)
                cnt=cnt+1
    print(cnt)
            
if __name__ == '__main__':
#    if random.randint(1,10)>6:
    main()

