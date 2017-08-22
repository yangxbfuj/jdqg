# _*_coding:utf-8_*_
from selenium import webdriver
import datetime
import time

path = "./chromedriver"
driver = webdriver.Chrome(path)


# 自动登录脚本
def login(username, pwd):
    driver.get("https://www.jd.com/")
    if driver.find_element_by_link_text("你好，请登录"):
        driver.find_element_by_link_text("你好，请登录").click()
    if driver.find_element_by_link_text("账户登录"):
        driver.find_element_by_link_text("账户登录").click()
    login_path = driver.current_url
    if driver.find_element_by_name("loginname"):
        driver.find_element_by_name("loginname").send_keys(username)
    if driver.find_element_by_name("nloginpwd"):
        driver.find_element_by_name("nloginpwd").send_keys(pwd)
    if driver.find_element_by_id("loginsubmit"):
        driver.find_element_by_id("loginsubmit").click()
    time.sleep(1)
    now_path = driver.current_url
    if driver.find_elements_by_link_text("芒果from成都"):
        print "登录成功"
        return True
    else:
        print "登录失败"
        return False


def order_on_time(time_str, minute):
    driver.get("https://cart.jd.com/cart.action")
    driver.find_element_by_link_text("去结算").click()
    while True:
        now = datetime.datetime.now()
        print "循环刷新时间" + now.strftime('%Y-%m-%d %H:%M:%S')
        if now.strftime('%Y-%m-%d %H:%M:%S') == time_str:
            while True:
                try:
                    old_url = driver.current_url
                    driver.find_element_by_id('order-submit').click()
                    new_url = driver.current_url
                    if not old_url == new_url:
                        print "订单生成"
                        return True
                except:
                    time.sleep(1)
        time.sleep(1)


# def order(time_str, minute):
#     if order_on_time(time_str, minute):
#         if driver.find_element_by_id('order-submit'):
#             driver.find_element_by_id('order-submit').click()
#     else:
#         print "False"


def user():
    login("username", "password")


user()

if __name__ == '__main__':
    order_on_time('2017-08-22 10:00:00', 1)
