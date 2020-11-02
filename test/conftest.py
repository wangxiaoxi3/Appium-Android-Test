# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午3:17
# @Author  : WangJuan
# @File    : conftest.py

import pytest
import allure
from appium import webdriver
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from base.actions import ElementActions
from utils.environment import Environment


@pytest.fixture()
def action():
    env = Environment().get_environment_info()

    allure.environment(app=env.apk)
    allure.environment(app_activity=env.app_activity)
    allure.environment(device_name=env.devices[0].device_name)
    allure.environment(platform_name=env.devices[0].platform_name)
    allure.environment(platform_version=env.devices[0].platform_version)

    capabilities = {'platformName': env.devices[0].platform_name,
                    'platformVersion': env.devices[0].platform_version,
                    'deviceName': env.devices[0].device_name,
                    'app': env.apk,
                    'clearSystemFiles': True,
                    'appActivity': env.app_activity,
                    'appPackage': env.app_package,
                    'automationName': 'UIAutomator2',
                    'newCommandTimeout': "2000",
                    'unicodeKeyboard': True,
                    'resetKeyboard': True,
                    'noSign': True,
                    'autoGrantPermissions': True
                    }
    host = "http://localhost:4724/wd/hub"
    driver = webdriver.Remote(host, capabilities)
    yield ElementActions(driver).reset(driver)
    driver.quit()


# @pytest.fixture(scope="module")
# def action2():
#     env = Environment().get_environment_info()
#
#     allure.environment(app=env.apk)
#     allure.environment(app_activity=env.app_activity)
#     allure.environment(device_name=env.devices[0].device_name)
#     allure.environment(platform_name=env.devices[0].platform_name)
#     allure.environment(platform_version=env.devices[0].platform_version)
#
#     capabilities = {'platformName': env.devices[0].platform_name,
#                     'platformVersion': env.devices[0].platform_version,
#                     'deviceName': env.devices[0].device_name,
#                     'app': env.apk,
#                     'clearSystemFiles': True,
#                     'appActivity': env.app_activity,
#                     'appPackage': env.app_package,
#                     'automationName': 'UIAutomator2',
#                     'newCommandTimeout': "2000",
#                     'unicodeKeyboard': True,
#                     'resetKeyboard': True,
#                     'noSign': True
#                     }
#     host = "http://localhost:4723/wd/hub"
#     driver = webdriver.Remote(host, capabilities)
#     yield ElementActions(driver).reset(driver)
#     driver.quit()
