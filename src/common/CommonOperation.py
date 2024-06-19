#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @File: CommonOperation.py
# @Author: lichao
# @Time: 2024-06-19 20:27
# @Software: PyCharm
import os.path
import time


class CommonOperation:
    def __init__(self, driver):
        self.driver = driver

    def getPicture(self):
        dirpath = os.path.dirname(__file__)  # 获取当前文件路径
        currenttime = time.strftime("%Y-%m-%d %H%M%S")  # 获取当前系统时间
        filename = currenttime + ".png"  # 定义图片名称
        filepath = os.path.join(dirpath, "..\\..\\pictures\\", filename)  # 拼接图片路径
        self.driver.get_screenshot_as_file(filepath)  # 截图

    def findElement(self, element):
        pass


if __name__ == '__main__':
    from selenium import webdriver
    from src.common.GetFileInfo import GetFileInfo

    driver = webdriver.Chrome()
    driver.maximize_window()
    test = GetFileInfo()
    test1 = CommonOperation(driver)
    url = test.getData_byLine("conf.csv", 1)[1]
    driver.get(url)
    time.sleep(5)
    test1.getPicture()
    driver.quit()
