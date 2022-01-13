from selenium import webdriver
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import const
import urllib.request
import os

#class affiURL:
def affiLogin(chro):
    chro.get('https://grp02.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=p11')
    
    user=chro.find_element_by_id('loginInner_u')
    user.send_keys(const.loginUser)
    
    password=chro.find_element_by_id('loginInner_p')
    password.send_keys(const.loginPass)
    
    loginButton = chro.find_element_by_xpath('//*[@id="loginInner"]/p[1]/input')
    loginButton.click()

    #chro.switch_to.window(chro.window_handles[0]) 
 
    chro.get('https://login.account.rakuten.com/sso/authorize?client_id=affiliate_jp_web&redirect_uri=https://affiliate.rakuten.co.jp/auth/callback&response_type=code&scope=openid&ui_locales=ja-JP&state=https%3A%2F%2Faffiliate.rakuten.co.jp#/sign_in')
    time.sleep(2)
    user=chro.find_element_by_id('user_id')
    user.send_keys(const.loginUser)
    time.sleep(5)
    next_button=chro.find_element_by_xpath('//*[@id="cta"]')
    next_button.click()
    

    time.sleep(20)
    password=chro.find_element_by_id('password_current')
    time.sleep(2)
    password.send_keys(const.loginPass)

    time.sleep(5)
    loginButton2 = chro.find_elements_by_id('cta')
    loginButton2[1].click()
    
    time.sleep(10)
    
    
    return chro


def affiURL(chro,url):
    chro.get('https://affiliate.rakuten.co.jp/')

    time.sleep(1)
    element=chro.find_element_by_id('u')
    element.send_keys(url[0])
    #input url
    element = chro.find_element_by_xpath('//*[@id="freelink"]/div/div/div/button')
    time.sleep(1)
    element.click()
    time.sleep(1)
    try:   
        title=chro.find_element_by_xpath('//*[@id="preview_box"]/table/tbody/tr/td[2]/div/table/tbody/tr/td[2]/p/a').text
        price=chro.find_element_by_xpath('//*[@id="preview_box"]/table/tbody/tr/td[2]/div/table/tbody/tr/td[2]/p/span[1]').text
    except: 
        title=chro.find_element_by_xpath('//*[@id="preview_box"]/table/tbody/tr/td/div/table/tbody/tr/td[2]/p/a').text
        price=chro.find_element_by_xpath('//*[@id="preview_box"]/table/tbody/tr/td/div/table/tbody/tr/td[2]/p/span[1]').text

    time.sleep(1)
    #画像ダウンロード
    element1=chro.find_element_by_xpath('//*[@id="item_link_type"]/label[2]')
    element1.click()
    src= chro.find_element_by_xpath('//*[@id="preview_box"]/a/img').get_attribute('src')
    try:
        urllib.request.urlretrieve(src, './affiImg/temp.jpg')
    except:
        os.remove('./affiImg/temp.jpg')
        urllib.request.urlretrieve(src, './affiImg/temp.jpg')
        
    time.sleep(1)
    #get shortURL
    try:
        element=chro.find_element_by_xpath('//*[@id="item_link_type"]/label[4]')
    except:
        element=chro.find_element_by_xpath('//*[@id="item_link_type"]/label[2]')
    element.click()
    
    time.sleep(1)
    affiUrl=chro.find_element_by_id('preview_box').get_attribute("textContent")
    #print(affiUrl)
    
    #imgファイル取得
    imgFileNameList=affiUrl.split('/')
    imgFileName=imgFileNameList[len(imgFileNameList)-1]
    
    time.sleep(1)
    # ファイル名の変更
    try:
        os.rename('./affiImg/temp.jpg', './affiImg/'+imgFileName+'.jpg') 
    except:
        os.remove('./affiImg/temp.jpg')
    return "@@"+str(title)+"@@"+"["+str(price)+"]"+"@@"+str(affiUrl)

