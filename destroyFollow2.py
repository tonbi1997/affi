import time
import tweepy
import const
from Twitter import Twitter
import re
import random

def intersect_list(lst1, lst2):

    lst1 = lst1.copy()
    for element in lst2:
        try:
            lst1.remove(element)
        except ValueError:
            continue
        else:
            print(element)
            #print("love each other")
    return lst1

def main():
    api = Twitter().getApi()
    twitterId="@rakuten_saleInf"

    followers = api.followers_ids(twitterId)
    friends = api.friends_ids(twitterId)
    not_following_me_list = intersect_list(friends, followers)
    cnt=0
    for f in not_following_me_list[::-1]:
        if api.get_user(f).followers_count<800:
            if cnt<20:
                time.sleep(random.random()*5)
                print("ID:{}のフォローを解除しました。".format(api.get_user(f).screen_name))
            
                api.destroy_friendship(f)
                cnt=cnt+1
    print(cnt)
            
if __name__ == '__main__':
#    if random.randint(1,10)>6:
    main()
