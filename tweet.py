#!/usr/bin/env python
# coding: utf-8


import tweepy
import const
import createUrlRankCD
from xvfbwrapper import Xvfb

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





import random
def getUrl():
    path='affiUrl.txt'
    with open(path,'r') as f:
        urlList = f.readlines()
        f.close()
    size=len(urlList)
    delFig=random.randint(0,size-1)
    url=urlList[delFig].split("@@") 
    print(url)
    print(urlList.pop(delFig))
    
    with open(path, 'w') as f:
        f.writelines(urlList)
        f.close()
    newtext=""
    if len(url[1])>80:
        for i in range(77):
            newtext+=url[1][i]
        newtext+="..."
        url[1]=newtext
    print(url[0])
    text=""
    for i in range(0,len(url)-1):
        text+=url[i]+"\n\n"
    text+='(楽天sale) '#相互フォロー #rakuten \n\n'
    text+=url[len(url)-1]
    fileNameList=url[len(url)-1].split('/')
    fileName='./affiImg/'+fileNameList[len(fileNameList)-1].replace('\n','')+'.jpg'
    return [text,fileName]



def main():
    try:
        url=getUrl()
        print(url)
        api=Twitter().getApi()
        #api.update_status(url)
        try:
            api.update_with_media(status = url[0], filename =url[1])
        except:
            api.update_status(url[0])
    except:
        display=Xvfb()
        display.start()
        createUrlRankCD.main()
        display.stop()
        print('aaa')

        
if __name__ == '__main__':
    main()




