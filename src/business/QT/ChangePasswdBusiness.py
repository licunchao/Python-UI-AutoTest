from src.common.TestData_ConfigInfo import TestData_ConfigInfo
from src.pages.QT.ChangePasswdPage import ChangePasswdPage


class ChangePasswdBusiness(ChangePasswdPage):
    #功能方法1：  保存密码修改功能
    def  baoCunMimaFunction(self,line,wait,browser):
        #读取测试数据
        data = TestData_ConfigInfo().getTestData("ChangePasswdTestData.csv",line)
        #把读出来的测试数据，写到页面上
        self.shuRuMiMaOper(wait,browser,data[0],data[1],data[2])
        #点击保存按钮
        self.dianJiBaoCunOper(wait)


    #功能方法2：取消密码修改功能
    def  quXiaoMimaFunction(self,wait,browser):
        #读取测试数据
        data = TestData_ConfigInfo().getTestData("ChangePasswdTestData.csv",1)
        #把读出来的测试数据，写到页面上
        self.shuRuMiMaOper(wait,browser,data[0],data[1],data[2])
        #点击取消
        self.dianJiQuXiaoOper(wait)