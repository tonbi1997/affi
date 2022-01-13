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
def getPointUp50(chro,i,j):
    element=chro.find_element_by_xpath('/html/body/div[2]/div[7]/div/div[1]/div[2]/div['+str(i)+']/ul/li['+str(j)+']/p[2]/a/img')

    #クリック前のハンドルリスト
    handles_befor =chro.window_handles

    #(リンク)要素を新しいタブで開く
    actions=None
    
    actions = ActionChains(chro)
    #Mac以外なのでコントロールキー
    actions.key_down(Keys.CONTROL)
    actions.click(element).key_up(Keys.CONTROL).perform() 
    
    time.sleep(4)

    element=chro.find_element_by_xpath('//*[@id="SDalcorAdsect"]/li['+str(j)+']/p[3]/a')
    title=element.text
    
    element=chro.find_element_by_xpath('//*[@id="SDalcorAdsect"]/li['+str(j)+']/p[5]')
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


    chro.get('https://event.rakuten.co.jp/superdeal/special/pointback50/')
    for i in range(1,50):
        try:
            hrefList.append(getPointUp50(chro,2,i))
        except:
            try:
                hrefList.append(getPointUp50(chro,2,i))
            except:
              print("miss")

    print(hrefList)
    chro=Chro().chrome()
    affiList=[]
    affiLogin(chro)
    for url in hrefList:
        try:
            affi='50%ポイントバック!!!'+affiURL(chro,url)
            affiList.append(affi)

        except:
          print("miss")
    chro.close()



    with open('affiUrl.txt', 'a') as f:
        #f.write("\n".join(affiList))
        for url in affiList:
            f.write("%s\n" % url)
        
    f.close()


    print(affiList)

if __name__ == '__main__':
    #display=Xvfb()
    #display.start()
    main()
    #display.stop()