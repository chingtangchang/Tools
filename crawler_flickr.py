
from selenium import webdriver
import time
import urllib
 
# crawler url
url = 'https://www.flickr.com/search/?text=%E6%96%B0%E5%9E%A3%E7%B5%90%E8%A1%A3&view_all=1'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)
pos = 0

for i in range(1):
    pos += i*500 # ¨C¦¸¤U?500
    js = "document.documentElement.scrollTop=%d" % pos
    driver.execute_script(js)
    time.sleep(2) 
    
    


from urllib.parse import unquote
import requests,os
from urllib.request import urlretrieve
import re
from bs4 import BeautifulSoup
from urllib.error import HTTPError

xpath = '//div[@class="main search-photos-results"]/div/div/div'
local = "C:\\Users\\asus\\Desktop\\img_crawer\\"
web_element = driver.find_elements_by_xpath(xpath)
get_link = None
num = 0

for i in web_element:
    get_link = i.get_attribute('style')
    link = "http:" + get_link.split("url(\"")[1].split("\");")[0]
    link = link.replace("_m", "")
    _link = link.split(".")
    _link[-2] = _link[-2] + "_z"
    link = ".".join(_link)
    img = local + str(num) + ".jpg"
    print(link)
    urlretrieve(link, img)
    if num == 10:
        break
    num += 1
#     break
    