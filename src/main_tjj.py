# coding=utf-8
import sys
from time import sleep

from appium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException

from utils import load_json_config

reload(sys)
sys.setdefaultencoding('utf-8')

desired_caps = load_json_config("../config/config-tjj-al100.json")
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

sleep(2)
# 1.首次启动权限申请 (autoAcceptAlerts 属性会自动获取权限)
for perIndex in [0, 5]:
    try:
        driver.find_element_by_id('com.android.packageinstaller:id/permission_allow_button').click()
        sleep(2)
    except NoSuchElementException:
        break

# 2.关闭首页推荐弹框
try:
    driver.find_element_by_id('com.huanshou.taojj:id/iv_close').click()
    sleep(1)
except NoSuchElementException:
    print 'find_element_by_id：  iv_close    error!'

# 3.模拟输入 关键词 搜索，键盘确认
try:
    driver.find_element_by_id('com.huanshou.taojj:id/tv_home_search').click()
    driver.find_element_by_id('com.huanshou.taojj:id/search_complete_tv').send_keys(unicode("口红"))
    # 回车 66 
    driver.press_keycode('66')
    driver.hide_keyboard()
    sleep(3)

    # 点击 item 0,
    # activity ：com.taojj.module.goods.activity.MallSearchActivity
    search_result_list = driver.find_elements_by_xpath(
        "//android.support.v7.widget.RecyclerView/*[@class='android.widget.RelativeLayout']")
    search_result_list.__getitem__(0).click()

    # 购买
    # activity ：com.taojj.module.goods.activity.CommodityDetailActivity¬
    driver.find_element_by_id('com.huanshou.taojj:id/commodity_detail_group_layout').click()

    # 登陆
    # activity ：com.taojj.module.user.activity.LoginActivity
    # 微信，res_id : com.huanshou.taojj:id/wx_login_tv_layout
    # 其他，res_id : com.huanshou.taojj:id/pick_other_login_way_tv
    #     手机号，res_id : com.huanshou.taojj:id/phone_login_layout
    #     qq，res_id : com.huanshou.taojj:id/QQ_login_layout

    # qq 授权登陆
    driver.find_element_by_id("com.huanshou.taojj:id/pick_other_login_way_tv").click()
    driver.find_element_by_id("com.huanshou.taojj:id/QQ_login_layout").click()

    sleep(2)

    # 失败，无法进行授权登陆 
    driver.start_activity('com.tencent,mobileqq', 'com.tencent.open.agent.AuthorityActivity')
    driver.find_element_by_id("com.tencent.mobileqq:id/ivTitleBtnLeft").click()
    driver.find_element_by_xpath(
        "//android.widget.LinearLayout/*[@class='android.widget.Button']").click()

    sleep(2)


except WebDriverException, data:
    print data.message

# 4。模拟购买

sleep(6)
driver.quit()
