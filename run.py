# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 下午2:51
# @Author  : WangJuan
# @File    : run.py

import pytest, time
from utils.environment import Environment
from utils.shell import Shell
from utils import L
import sys

"""
run all case:
    python3 run.py

run one module case:
    python3 run.py test/test_home.py

run case with key word:
    python3 run.py -k <keyword>

"""

if __name__ == '__main__':
    env = Environment()
    xml_report_path = env.get_environment_info().xml_report
    html_report_path = env.get_environment_info().html_report
    # 开始测试
    args = ['-s', '-q', '--allure_features=My stdio1', '--alluredir', xml_report_path]
    # args = ['-s', '-q'],'--allure_features=My stdio'
    self_args = sys.argv[1:]
    pytest.main(args)
    # 生成html测试报告
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)
    #
    try:
        Shell.invoke(cmd)
    except:
        L.e("Html测试报告生成失败,确保已经安装了Allure-Commandline")
    # 查找html报告并发送
    # time.sleep(2)
    # from utils.mail import Mail
    # mail = Mail()
    # mail.sendMail()
