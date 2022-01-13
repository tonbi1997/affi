#!/usr/bin/env python
# coding: utf-8


from selenium import webdriver
import const
import time
import random
from pyvirtualdisplay import Display
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
def getSale(chro,i,j):
    
    element=chro.find_element_by_xpath('//*[@id="six_timesale"]/div[2]/div/div/div/ul['+str(i)+']/li['+str(j)+']/div/div/a/p')
    title=element.text
    
    element=chro.find_element_by_xpath('//*[@id="six_timesale"]/div[2]/div/div/div/ul['+str(i)+']/li['+str(j)+']/div/div/a/div[3]/p/span[1]')
    price=element.text
    
    
    element=chro.find_element_by_xpath('//*[@id="six_timesale"]/div[2]/div/div/div/ul['+str(i)+']/li['+str(j)+']')

    #クリック前のハンドルリスト
    handles_befor =chro.window_handles

    #(リンク)要素を新しいタブで開く
    actions=None
    
    actions = ActionChains(chro)
    #Mac以外なのでコントロールキー
    actions.key_down(Keys.CONTROL)
    actions.click(element).key_up(Keys.CONTROL).perform() 
    
    #クリック後のハンドルリスト
    handles_after = chro.window_handles

    #ハンドルリストの差分
    handle_new = list(set(handles_after) - set(handles_befor))

    #新しいタブに移動
    chro.switch_to.window(handle_new[0])

    url=chro.current_url
    
    chro.close()

    chro.switch_to.window(chro.window_handles[0]) 
     
    print(url)
    return [str(url),title,price]

 

def main():
    breakFlg=False
    hrefList=[]
    chro=Chro().chrome()


    chro.get('https://event.rakuten.co.jp/bargain/timesale/')
    
    for i in range(1,5):
        for j in range(1,3):
            try:
                hrefList.append(getSale(chro,i,j))
            except:
                try:
                    hrefList.append(getSale(chro,i,j))
                except:
                    print('miss')
    print(hrefList)

    affiList=[]
    affiLogin(chro)
    for url in hrefList:
        try:
            affi='24hタイムセール!!!'+affiURL(chro,url)
            affiList.append(affi)
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

