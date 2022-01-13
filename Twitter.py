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