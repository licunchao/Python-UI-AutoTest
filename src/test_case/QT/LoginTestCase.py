import unittest  #python中自带的一个单元测试的框架；使用untitest提供的用例结构；以及断言方法
from time import strftime

import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from src.business.QT.LoginBusiness import LoginBusiness
from src.common.CommonOperation import CommonOperation
from src.common.TestData_ConfigInfo import TestData_ConfigInfo


class  LoginTestCase(unittest.TestCase):
    #初始化操作：要打开浏览器；要填网址等等
    def  setUp(self):
        # self.browser = webdriver.Firefox() #打开一个火狐浏览器，并且赋值给变量browser（就表示火狐浏览器）
        # #从url.csv中取网址
        # urlDict = TestData_ConfigInfo().getConfigData("url.csv")
        # self.browser.get( urlDict["url"]  )
        # #实例化一个显性等待对象
        # self.wait  = WebDriverWait(self.browser,10)
        self.browser,self.wait = CommonOperation().chuShiHua()

    # 登陆的 用例： 正常登陆
    def testNormalLogin(self):
        try:
            # 调用业务层：登陆的功能
            loginObject = LoginBusiness()  #实例化登陆业务LoginBusiness类的对象
            loginObject.loginFunction(1, self.wait)  # 实参：实际的数据 调用登陆业务中的登录功能方法
            # 断言
            #获取实际结果
            result = loginObject.getTuiChuText(self.wait)
            #将实际结果跟预期结果进行比较；  unittest框架中的断言方法： assertEqual() 等等
            self.assertEqual("退出登录",result)
        except:
            # 截图
            CommonOperation().getPicture(self.browser, "NormalLogin")
            raise  # 继续抛出错误信息；如果不加就没有错误信息；不方便定位；而且是绿色的

    #登陆的 用例： 密码错误登陆
    def  testErrorPasswd(self):
        try:
            loginObject = LoginBusiness()
            loginObject.loginFunction(2, self.wait)  # 实参：实际的数据
            # 断言
            # 获取实际结果
            result = loginObject.getTanKuangText(self.wait)
            # 将实际结果跟预期结果进行比较；  unittest框架中的断言方法： assertEqual() 等等
            self.assertEqual("亲，用户名或密码错误！",result)
        except:
            # 截图
            CommonOperation().getPicture(self.browser, "ErrorPasswd") #不带参数名，注意前后的位置；
            #CommonOperation().getPicture(name="ErrorPasswd",browser=self.browser)
            raise  # 继续抛出错误信息；如果不加就没有错误信息；不方便定位；而且是绿色的

    # 登陆的 用例： 用户名错误登陆
    def testErrorUsername(self):
        try:
            loginObject = LoginBusiness()
            loginObject.loginFunction(3, self.wait)  # 实参：实际的数据
            # 断言
            # 获取实际结果
            result = loginObject.getTanKuangText(self.wait)
            # 将实际结果跟预期结果进行比较；  unittest框架中的断言方法： assertEqual() 等等
            self.assertEqual("亲，用户名或密码错误！", result)
        except:
            #截图
            CommonOperation().getPicture(self.browser,"ErrorUsername")
            raise  #继续抛出错误信息；如果不加就没有错误信息；不方便定位；而且是绿色的

    #收尾的操作：退出浏览器
    def  tearDown(self):
        self.browser.quit()


# if __name__ == "__main__":
#     unittest.main()

    #可以测试套件 testSuite ;  unittest.main()     unitests  for  testNormalLogin (执行这一个用例）  unittest  in  xxxx.py  把这个文件中的所有用例都执行






