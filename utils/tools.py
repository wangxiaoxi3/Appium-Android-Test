# -*- coding: utf-8 -*-
# @Time    : 2018/6/7 下午2:51
# @Author  : WangJuan
# @File    : tools.py

import os
from utils.shell import Shell
from utils import L


class Device:
    @staticmethod
    def get_android_devices():
        android_devices_list = []
        for device in Shell.invoke('adb devices').splitlines():
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                android_devices_list.append(device)
        return android_devices_list


class Find:
    # 输入目录路径，输出最新文件完整路径
    @staticmethod
    def find_new_file(dis, n):
        """
        查找目录下最新的文件
        :param dis:
        :param n:
        :return:
        """
        file_lists = os.listdir(dis)
        file_lists.sort(key=lambda fn: os.path.getmtime(dis + "/" + fn)
        if not os.path.isdir(dis + "/" + fn) else 0)
        file_new_list = []
        for i in range(1, n):
            file = os.path.join(dis, file_lists[-i])
            file_new_list.append(file)
        return file_new_list

    @staticmethod
    def find_screen(key):
        """
        根据关键字查找相应图片
        :param key:
        :return:
        """
        dis = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/screenshot/'

        ll = os.listdir(dis)
        last_list = []
        for i in ll:
            if key in i:
                last_list.append(i)
        last_list.sort(key=lambda fn: os.path.getmtime(dis + "/" + fn) if not os.path.isdir(dis + "/" + fn) else 0)
        file = dis + last_list[-1]
        print('错误截图：', file)
        ff = open(file, 'rb').read()
        return ff


if __name__ == '__main__':
    devices = Device.get_android_devices()
    L.i("devices: ", devices)
