import tweepy
import const
import time
import random

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
    api=Twitter().getApi()
    search_words="相互フォロー"
    search_results = api.search(q=search_words,result_type='recent',count=10)
    
    limit_cnt=10
    cnt=0
    for result in search_results:
        tweet_id = result.id
        print(result.favorited)
        print(result.text)
        time.sleep(random.random()*15)
        try:
            if not result.favorited:
                api.create_favorite(tweet_id)
                time.sleep(random.random()*15)
                api.create_mute(result.user.screen_name)
                print(result)
                print('muted:'+result.user.screen_name)
                cnt+=1
                if cnt>limit_cnt:
                    break
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()