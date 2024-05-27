from fake_useragent import UserAgent
import asyncio
import time
# import aiohttp
from lxml import etree
import random
import sqlite3
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
import threading
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
import requests
import time
from lxml import etree
from  selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

#url_news = input('请输入目标网址：')#''#目标页面-最新
url_top = ''#最热
url_topnum = ''#最多

#https://bbs.3dmgame.com/forum-3492-{}.html  #小说
#https://www.dy2018.com/19/ #电影
#Playwright
import re

sem = threading.Semaphore(2)  # 限制线程的最大数量
def reduce_spaces(s):
    return re.sub(r'\s+', ' ', s).strip()

type_list = ['NAV_WOMAN','NAV_MAN']
value_list = []
#browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
class JdSpider:
    def __init__(self):
        #https://www.dy2018.com/{} 电影
        #http://www.biqugess.co/class/{}/1/小说
        self.url = 'https://www.converse.com.cn/shop/{}'
        self.services = [Service('./chromedriver101.0.4951.41.exe'),Service('./chromedriver101.0.4951.41.exe')]

    def get_page(self,i,driver):
        url = self.url.format(type_list[i])
        res = driver.get(url)#打开电影页面

        time.sleep(10)
        print(res)
        file_names = driver.find_elements(By.XPATH, '//div[contains(@class,"products")]//div[contains(@class,"product-item-container")]//div[contains(@class,"img-box")]')
        print(len(file_names))
        #获取二级页面列表
        m_links = [file_name.find_elements(By.XPATH, 'a')[0].get_attribute('href') for file_name in file_names]

        print(m_links)
        for i,m_link in enumerate(m_links):
            #print(real_url)
            driver.get(m_link)
            time.sleep(1)
            try:
                content_list = driver.find_elements(By.XPATH, '//div[contains(@class,"sizes")]/div[contains(@class,"content")]')
                content_reverse_list = content_list[::-1]
                title = driver.find_element(By.XPATH, '//div[contains(@class,"product-info-base")]//div[contains(@class,"title")]/span').text
                for content in  content_reverse_list:
                        if not 'content no-neqty' in content.get_attribute('class'):
                            print(title + ' ' + content.text)
                            break

            except NoSuchElementException as err:
                pass
                print('空二级页面')

    def browser_work(self,i):
        options = webdriver.ChromeOptions()
        service = Service('/usr/local/bin/chromedriver')
        # 禁用JavaScript
        options.add_argument('--disable-javascript')
        # 启用无头模式
        #options.add_argument('--headless')

        # 使用上述配置初始化WebDriver
        # options.add_extension('./AdBlock_v3.11.2.crx')
        options.add_argument("--disable-blink-features=AutomationControlled")
        # driver = webdriver.Chrome(options=options, service=service)
        
        options.add_argument("--start-maximized") 
        options.add_argument('--log-level=3') 
    
        # Provide the path of chromedriver present on your system. 
        driver = webdriver.Chrome(service=service, options=options) 
        driver.set_window_size(1920,1080) 
        
        
        self.get_page(i,driver)
        driver.quit()

    def run_thread(self,i):
        with sem:  # 锁定线程的最大数量
            print(threading.current_thread().name)
            print('-' * 20)
            self.browser_work(i)
            # sleep(1)
            print('*' * 20)

    def main(self):
        ts = []

        for i in range(1):
            t = threading.Thread(target=self.run_thread, args=(i,))
            ts.append(t)
            t.start()
        for t in ts:
            t.join()

jdSpider = JdSpider()
jdSpider.main()