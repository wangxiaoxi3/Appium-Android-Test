# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 下午3:17
# @Author  : WangJuan
# @File    : config.py
from configparser import ConfigParser
import os
from utils import L


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


class Config:
    DEFAULT_CONFIG_DIR = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, "data/config.ini")))
    BASE_PATH_DIR = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    # # titles:
    TITLE_NAME = "name"
    TITLE_MAIL = "mail"
    # [name]
    VALUE_APP = "apk"
    VALUE_APP_ACTIVITY = "app_activity"
    VALUE_APP_PACKAGE = "app_package"
    # [mail]
    VALUE_SMTPSERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    def __init__(self):
        self.path = Config.DEFAULT_CONFIG_DIR
        self.cp = ConfigParser()
        self.cp.read(self.path)
        L.i('初始化config...config path: ' + self.path)
        apk_name = self.get_config(Config.TITLE_NAME, Config.VALUE_APP)
        self.apk_path = Config.BASE_PATH_DIR + '/apk/' + apk_name
        self.xml_report_path = Config.BASE_PATH_DIR + '/report/xml'
        self.html_report_path = Config.BASE_PATH_DIR + '/report/html'
        self.pages_yaml_path = Config.BASE_PATH_DIR + '/page/yaml'
        self.env_yaml_path = Config.BASE_PATH_DIR + '/data/environment_info.yaml'
        self.app_activity = self.get_config(Config.TITLE_NAME, Config.VALUE_APP_ACTIVITY)
        self.app_package = self.get_config(Config.TITLE_NAME, Config.VALUE_APP_PACKAGE)

        self.smtpserver = self.get_config(Config.TITLE_MAIL, Config.VALUE_SMTPSERVER)
        self.sender = self.get_config(Config.TITLE_MAIL, Config.VALUE_SENDER)
        self.receiver = self.get_config(Config.TITLE_MAIL, Config.VALUE_RECEIVER)
        self.username = self.get_config(Config.TITLE_MAIL, Config.VALUE_USERNAME)
        self.password = self.get_config(Config.TITLE_MAIL, Config.VALUE_PASSWORD)

    def set_config(self, title, value, text):
        self.cp.set(title, value, text)
        with open(self.path, "w+") as f:
            return self.cp.write(f)

    def add_config(self, title):
        self.cp.add_section(title)
        with open(self.path, "w+") as f:
            return self.cp.write(f)

    def get_config(self, title, value):
        return self.cp.get(title, value)

