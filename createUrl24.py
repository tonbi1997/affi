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
def getPointUp24(chro,i):
    time.sleep(3)
    element=chro.find_element_by_xpath('//*[@id="riSDAdTimeSale6"]/div/ul/li['+str(i)+']/div/ul/li[5]/ul/li/a/img')

    #クリック前のハンドルリスト
    handles_befor =chro.window_handles

    #(リンク)要素を新しいタブで開く
    actions=None
    
    actions = ActionChains(chro)
    #Mac以外なのでコントロールキー
    actions.key_down(Keys.COMMAND)
    
    time.sleep(3)
    actions.click(element)
    actions.perform()
    time.sleep(3)
    
    element=chro.find_element_by_xpath('//*[@id="riSDAdTimeSale6"]/div/ul/li['+str(i)+']/div/ul/li[2]/a')
    title=element.text
    print(title)
    
    element=chro.find_element_by_xpath('//*[@id="riSDAdTimeSale6"]/div/ul/li['+str(i)+']/div/ul/li[6]/ul/li[2]/span')
    price=element.text
    print(price)
    
    time.sleep(3)
    
    #クリック後のハンドルリスト
    handles_after = chro.window_handles

    #ハンドルリストの差分
    handle_new = list(set(handles_after) - set(handles_befor))

    #新しいタブに移動
    chro.switch_to.window(handle_new[0])
    print(chro.current_url)
    url=chro.current_url
    
    time.sleep(3)
    chro.close()

    chro.switch_to.window(chro.window_handles[0]) 

    return [str(url),title,price]



def main():
    breakFlg=False
    hrefList=[]
    chro=Chro().chrome()


    chro.get('https://event.rakuten.co.jp/superdeal/timesale/')
    
    for i in range(1,3):
        try:
            hrefList.append(getPointUp24(chro,i))
        except:
            try:
               hrefList.append(getPointUp24(chro,i))
            except:
                print('miss')
    print(hrefList)

    affiList=[]
    affiLogin(chro)
    for url in hrefList:
        try:
            print(affiList.append('24h限定ポイントアップ!!!'+affiURL(chro,url)))
        except:
            print('miss')
    chro.close()



    with open('affiUrl.txt', 'a') as f:
        f.write("\n".join(affiList))
            
    f.close()


    print(affiList)

if __name__ == '__main__':
    #display=Xvfb()
    #display.start()
    main()
    #display.stop()