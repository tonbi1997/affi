#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
import const
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from xvfbwrapper import Xvfb
from affiURL import affiLogin
from affiURL import affiURL
from Chro import Chro

#タイムセール情報取得
def getPointUpRank(chro,i):
    element=chro.find_element_by_xpath('//*[@id="rnkRankingMain"]/div['+str(i)+']/div[3]/div[1]/div/div/div/div[1]/a')
    #element=chro.find_element_by_xpath('//*[@id="rnkRankingItemListBox"]/dl['+str(i)+']/dd[2]/dl/dt/dl/dt/a')
    #クリック前のハンドルリスト
    handles_befor =chro.window_handles

    #(リンク)要素を新しいタブで開く
    actions=None
    
    actions = ActionChains(chro)
    #Mac以外なのでコントロールキー
    actions.key_down(Keys.CONTROL)
    actions.click(element).key_up(Keys.CONTROL).perform() 
    

    title=element.text
    
    element=chro.find_element_by_xpath('//*[@id="rnkRankingMain"]/div['+str(i)+']/div[3]/div[2]/div[1]/div[1]')
    price=element.text
    
    #クリック後のハンドルリスト
    handles_after = chro.window_handles

    #ハンドルリストの差分
    handle_new = list(set(handles_after) - set(handles_befor))

    #新しいタブに移動
    chro.switch_to.window(handle_new[0])

    print(chro.current_url)
    url=chro.current_url
    
    chro.close()

    chro.switch_to.window(chro.window_handles[0]) 

    return [str(url),title,price]



def main():
    breakFlg=False
    hrefList=[]
    chro=Chro().chrome()


    #chro.get('https://ranking.rakuten.co.jp/')
    chro.get('https://ranking.rakuten.co.jp/realtime/101311/')
    for i in range(1,30):
        try:
            hrefList.append(getPointUpRank(chro,i))
        except:
            try:
                hrefList.append(getPointUpRank(chro,i))
            except:
                print('miss')
    print(hrefList)

    affiList=[]
    affiLogin(chro)
    for url in hrefList:
        try:
            affi='今売れてる商品!!!'+affiURL(chro,url)
            affiList.append(affi)
            print(affi)
            
        except:
            try:
                affi='今売れてる商品!!!'+affiURL(chro,url)
                affiList.append(affi)
                print(affi)
                
            except:
                print('miss')
    chro.close()



    with open('affiUrl.txt', 'w') as f:
        f.write("\n".join(affiList))
            
    f.close()


    print(affiList)

if __name__ == '__main__':
    display=Xvfb()
    display.start()
    main()
    display.stop()

