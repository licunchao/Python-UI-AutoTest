#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File: Test_ConfigInfo.py
# @Author: lichao
# @Time: 2024-06-18 22:35
# @Software: PyCharm


import csv

import os.path


class Test_ConfigInfo:
    def getConfigData(self, filename):
        dirpath = os.path.dirname(__file__)  # 获取当前文件的路径
        configfile = os.path.join(dirpath, '..\\..\\data\\', filename)  # 将当前文件路径和需要打开的文件路径拼接
        with open(configfile, 'r', encoding="utf-8") as f:
            filecontent = csv.reader(f)  # 打开csv文件，获取文件内容
            configdict = dict(filecontent)  # 将文件内容转换为字典
        return configdict  # 返回转换后的字典


if __name__ == '__main__':
    test = Test_ConfigInfo()
    print(test.getConfigData("conf.csv"))
