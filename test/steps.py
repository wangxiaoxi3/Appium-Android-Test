import allure
from base.actions import ElementActions
from page.pages import *


@allure.step(title="fb登录")
def login_fb(action: ElementActions):
    # 选择
    action.click(MainPage.select_all)

    # 关闭广告
    action.sleep(2)
    action.back_press()
    action.sleep(5)
    action.click(MainPage.nav_drawer)
    action.click(MainPage.login)

    action.click(LoginPage.fb)
    action.sleep(10)


@allure.step(title="Google登录")
def login_google(action: ElementActions):
    # 选择
    action.click(MainPage.select_all)

    # 关闭广告
    action.sleep(2)
    action.back_press()
    action.sleep(5)
    action.click(MainPage.nav_drawer)
    action.click(MainPage.login)

    action.click(LoginPage.google)
    action.click(LoginPage.google_choose)
    action.sleep(10)


@allure.step(title="fb账号登录")
def login_fb_email(action: ElementActions):
    # 选择
    action.click(MainPage.select_all)

    # 关闭广告
    action.sleep(2)
    action.back_press()
    action.sleep(5)
    action.click(MainPage.nav_drawer)
    action.click(MainPage.login)

    action.text(LoginPage.login_mail, 'papayatest2@163.com')
    action.text(LoginPage.login_password, 'papaya123')
    action.click(LoginPage.login_button)
    action.sleep(10)


@allure.step(title="账号登录")
def login_google_email(action: ElementActions):
    # 选择
    action.click(MainPage.select_all)

    # 关闭广告
    action.sleep(2)
    action.back_press()
    action.sleep(5)
    action.click(MainPage.nav_drawer)
    action.click(MainPage.login)

    action.text(LoginPage.login_mail, 'papayatest1@gmail.com')
    action.text(LoginPage.login_password, 'papaya123')
    action.click(LoginPage.login_button)
    action.sleep(10)


@allure.step(title="不登录")
def login_later(action: ElementActions):
    # 选择
    action.click(MainPage.select_all)

    # 关闭广告
    action.sleep(2)
    action.back_press()
    action.sleep(5)

