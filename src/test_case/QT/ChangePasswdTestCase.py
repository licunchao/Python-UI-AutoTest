import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from src.business.QT.ChangePasswdBusiness import ChangePasswdBusiness
from src.business.QT.LoginBusiness import LoginBusiness
from src.common.CommonOperation import CommonOperation
from src.common.TestData_ConfigInfo import TestData_ConfigInfo


class  ChangePasswdTestCase(unittest.TestCase):
    # 初始化：   得登录成功：打开浏览器，访问oa，进行默认登录
    def  setUp(self):
        self.browser, self.wait = CommonOperation().chuShiHua()
        #进行预制登录
        LoginBusiness().loginDefault(1,self.wait)
        #从数据库中查询加密后的旧密码
        self.zhanghao = TestData_ConfigInfo().getTestData("zhanghao.csv", 1)
        sql_select = "SELECT PASSWORD FROM oa_tbl_employee WHERE loginId='%s';" % (self.zhanghao[0])
        sqlResult = CommonOperation().connDB_execSQL(sql_select)
        self.oldPasswd = sqlResult[0][0]

    # tearDown(): 退出浏览器
    def tearDown(self):
        self.browser.quit()
        #在数据库中通过update语句恢复旧密码
        sql_update = "UPDATE oa_tbl_employee  SET  PASSWORD='%s'  WHERE loginId='%s';" % (self.oldPasswd, self.zhanghao[0])
        CommonOperation().connDB_execSQL(sql_update)

    # testXXX() 合法用例：修改为8位
    def  testChangePasswd8(self):
        try:
            passwdObject = ChangePasswdBusiness()
            passwdObject.baoCunMimaFunction(1,self.wait,self.browser)
            #断言
        except:
            CommonOperation().getPicture(self.browser,"passwd8")
            raise
    # testXXX() 合法用例：修改为20位
    def  testChangePasswd20(self):
        try:
            passwdObject = ChangePasswdBusiness()
            passwdObject.baoCunMimaFunction(2,self.wait,self.browser)
            #断言
        except:
            CommonOperation().getPicture(self.browser,"passwd20")
            raise
    # testXXX() 合法用例：修改为10位
    # testXXX() 非法用例：修改为7位
    # testXXX() 非法用例：修改为21位
    # testXXX() 非法用例：修改为不一致位
    # testXXX() 取消修改密码的用例
    def  testQuxiaoChangePasswd(self):
        try:
            passwdObject = ChangePasswdBusiness()
            passwdObject.quXiaoMimaFunction(self.wait,self.browser)
            #断言
        except:
            CommonOperation().getPicture(self.browser,"quxiaoPasswd")
            raise


