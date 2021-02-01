from time import sleep
import unittest
from selenium import webdriver

driver = webdriver.Chrome("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver")
driver.get("http://zg.xin.com/zg2020/home/login")
sleep(1)
driver.find_element_by_class_name('accountLogin___CwXEi').click()
driver.find_element_by_class_name('inputTxt___3kcxF').send_keys('zhangpeng3')
sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/input').send_keys('Wheeljack0917')
driver.find_element_by_class_name('LoginBtn___InSzX').click()
sleep(2)
driver.find_element_by_class_name('btnsDiv___Yvkjo').click()
print('开始添加线索')
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/p/input').send_keys('13520000005')
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/p/button').click()
sleep(3)
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/input[1]').send_keys('测试')
driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button').click()
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div/div[1]/span[2]/a').click()
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[2]/span[1]/input').send_keys('23739218')
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/div[2]/div[4]/div[2]/div[2]/span[2]/button').click()
from time import sleep
import unittest
from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\zhaohongwei2\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver")
driver.get("http://zg.xin.com/zg2020/home/login")
sleep(1)
driver.find_element_by_class_name('accountLogin___CwXEi').click()
driver.find_element_by_class_name('inputTxt___3kcxF').send_keys('zhangpeng3')
sleep(1)
driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/input').send_keys('Wheeljack0917')
driver.find_element_by_class_name('LoginBtn___InSzX').click()
sleep(2)
driver.find_element_by_class_name
