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

#chrome起動
class Chro:
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--blink-settings=imagesEnabled=false')
        self.options.set_headless(False)
        self.capabilities = DesiredCapabilities.CHROME.copy()
        self.capabilities['acceptInsecureCerts'] = True
        
    def chrome(self):
        self.chro =  webdriver.Chrome(chrome_options=self.options, desired_capabilities=self.capabilities)
        return self.chro

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
     
    return str(url)


#タイムセール情報取得
def getPointUp24(chro,i):
    element=chro.find_element_by_xpath('//*[@id="riSDAdTimeSale6"]/div/ul/li['+str(i)+']/div/ul/li[5]/ul/li/a/img')

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

    print(chro.current_url)
    url=chro.current_url
    
    chro.close()

    chro.switch_to.window(chro.window_handles[0]) 
     
    return str(url)


#タイムセール情報取得
def getSale(chro,i,j):
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

    print(chro.current_url)
    url=chro.current_url
    
    chro.close()

    chro.switch_to.window(chro.window_handles[0]) 
     
    return str(url)




def affiLogin(chro):
    chro.get('https://grp02.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=p11')
    
    user=chro.find_element_by_id('loginInner_u')
    user.send_keys(const.loginUser)
    
    password=chro.find_element_by_id('loginInner_p')
    password.send_keys(const.loginPass)
    
    loginButton = chro.find_element_by_xpath('//*[@id="loginInner"]/p[1]/input')
    loginButton.click()

    #chro.switch_to.window(chro.window_handles[0]) 
    chro.get('https://affiliate.rakuten.co.jp/')
    return chro


def affiURL(chro,url):
    chro.get('https://affiliate.rakuten.co.jp/')
    element=chro.find_element_by_id('u')
    element.send_keys(url)
    
    #input url
    element = chro.find_element_by_xpath('//*[@id="freelink"]/div/div/div/button')
    element.click()
    
    #get shortURL
    element=chro.find_element_by_xpath('//*[@id="item_link_type"]/label[4]')
    element.click()
    url=chro.find_element_by_id('preview_box').get_attribute("textContent")
    
    return str(url)

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
                print('miss')
    print(hrefList)

    affiList=[]
    affiLogin(chro)
    for url in hrefList:
        try:
            affiList.append(affiURL(chro,url))
        except:
            print('miss')
    chro.close()



    with open('affiUrl.txt', 'w') as f:
        f.write("\n".join(affiList))
            
    f.close()


    print(affiList)

if __name__ == '__main__':
    #display=xvfb()
    #display.start()
    main()
    #driver.stop()