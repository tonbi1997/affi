# -*- coding: utf-8 -*-
import datetime
import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # オプションを使うために必要
from Chro import Chro
from xvfbwrapper import Xvfb

def func():
    I=0
    #自動ログイン開始
    #opt = webdriver.ChromeOptions()
    #opt.add_argument('--headless')
    #chro =  webdriver.Chrome(executable_path=r'D:\masa\Anaconda3\chromedriver')#,chrome_options=opt)
    #chro =  webdriver.Chrome(chrome_options=opt)
    chro=Chro().chrome()
    chro.get("https://pairs.lv/#/login")
    #Facebookページ遷移〜ペアーズログインページ遷移
    chro.find_element_by_xpath('//*[@id="root"]/div[1]/main/div/div[1]/button/span').click()
    time.sleep(1)
    handle_array = chro.window_handles
    chro.switch_to.window(handle_array[-1])
    email=chro.find_element_by_name('email')
    email.send_keys('ilovemaou@me.com')
    password=chro.find_element_by_name('pass')
    password.send_keys('j1997227')
    time.sleep(3)
    chro.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div/div[3]/label[2]/input').click()
    time.sleep(10)
    chro.switch_to.window(handle_array[-2])
    #src= "https://pairs.lv/#/search/one/%s"%str(I)
    chro.get('https://pairs.lv/search')  
    time.sleep(5)
    chro.get('https://pairs.lv/search')
    time.sleep(5)
    chro.get('https://pairs.lv/search')
    time.sleep(5)
    chro.get('https://pairs.lv/search')
    time.sleep(5)
    
    
    # In[12]:
    
    
    row=0
    for i in range(0,11):
        try:
            chro.find_element_by_xpath('/html/body/div[1]/div[1]/main/ul/li['+str(i)+']/div/div/a[1]/div/div[2]/div').click()       
            break
        except:
            continue
    
    time.sleep(1+random.random())
    #１０００人に到達するまで繰り返す（足跡間隔はランダムで5〜10秒の間）
    cnt=int(400*random.random())+500
    I=cnt
    handle_array = chro.window_handles
    chro.switch_to.window(handle_array[-1])
    
    
    # In[ ]:
    
    
    row=0
    for i in range(1,11):
        try:
            href=chro.find_element_by_xpath('//*[@id="dialog-root"]/div['+str(i)+']/div/div[1]/div/div[3]/div[2]/a').click()  
            row=i
            break
        except:
            continue
    
    while I >1:
        I=I-1
        try:
            time.sleep(2+0.6*random.random())
            print('//*[@id="dialog-root"]/div['+str(row)+']/div/div[1]/div/div[3]/div[2]/a')
            href=chro.find_element_by_xpath('//*[@id="dialog-root"]/div['+str(row)+']/div/div[1]/div/div[3]/div[2]/a').get_attribute('href')
            chro.find_element_by_xpath('//*[@id="dialog-root"]/div['+str(row)+']/div/div[1]/div/div[3]/div[2]/a').click()  
        except:
            chro.get(href)
            time.sleep(5+0.6*random.random())
            for i in range(0,15):
                try:

                    href=chro.find_element_by_xpath('//*[@id="dialog-root"]/div['+str(i)+']/div/div[1]/div/div[3]/div[2]/a').click()  
                    row=i
                    break
                except:
                    continue
            continue
        time.sleep(3+0.6*random.random())
        print(href)
        
    
    
    # In[ ]:
    
    
    dt_now = datetime.datetime.now()
    print(dt_now)
    print(str(cnt)+"人に足跡を付けました")
    chro.close()
    #１０００人に到達したらプログラムを終了
if __name__=='__main__':
    display=Xvfb()
    display.start()
    func()
    display.stop()
    func() 
