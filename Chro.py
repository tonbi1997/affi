
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
        #self.chro = webdriver.Chrome()
        return self.chro