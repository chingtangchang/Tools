
from selenium import webdriver
import time
import urllib
 
# crawler url
url = 'http://pic.sogou.com/pics?query=%CA%D6%BB%FA&w=05009900&p=40030500&_asf=pic.sogou.com&_ast=1422627003&sc=index&sut=1376&sst0=1422627002578'
 
# web element path 
xpath = '//div[@id="imgid"]/ul/li/a/img'
 
# simulation Firefox webdriver
driver = webdriver.Firefox()
 
# maximize web window
driver.maximize_window()
 
img_url_dic = {}
driver.get(url)
 
pos = 0
for i in range(10):
    pos += i*500 # window drop 500dpi
    js = "document.documentElement.scrollTop=%d" % pos
    driver.execute_script(js)
    time.sleep(1) 
    
    
for element in driver.find_elements_by_xpath(xpath):
        img_url = element.get_attribute('src')
        print(img_url)