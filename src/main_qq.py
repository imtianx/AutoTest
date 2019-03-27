# coding=utf-8
import sys
from time import sleep

from appium import webdriver
from utils import load_json_config

reload(sys)
sys.setdefaultencoding('utf-8')

desired_caps = load_json_config("../config/config-qq-al100.json")
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
try:
    sleep(2)
    # login qq
    driver.find_element_by_id('com.tencent.mobileqq:id/btn_login').click()
    name = driver.find_element_by_id('com.tencent.mobileqq:id/name')
    name.clear()
    name.click()
    name.send_keys("qq account")
    pwd = driver.find_element_by_id('com.tencent.mobileqq:id/password')
    pwd.clear()
    pwd.click()
    pwd.send_keys("qq pwd")

    # 失败，手动滑块验证

    sleep(3)
    driver.find_element_by_id('com.tencent.mobileqq:id/login').click()
except Exception, error:
    print error.message

sleep(10)
driver.quit()
