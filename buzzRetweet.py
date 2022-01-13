import tweepy
import const
import time
import random
from Twitter import Twitter
import json

def main():
    api=Twitter().getApi()
    search_words="@TwTimez"
    search_results = api.search(q=search_words,result_type='recent',count=20)
    
    cnt=0
    for result in search_results:
        try:
            tweet=api.get_status(result.retweeted_status.in_reply_to_status_id)
            if tweet.retweet_count>5000 and tweet.retweet_count<tweet.favorite_count and not tweet.retweeted:
                time.sleep(random.random()*15)
                cnt=cnt+1
                if cnt>3:
                    break
                api.retweet(tweet.id)
                print(tweet.text)
            else:
                print('less')
        except Exception as e:
            print(e)
            
if __name__ == '__main__':
#    if random.randint(1,10)>6:
    main()
