from src.common.TestData_ConfigInfo import TestData_ConfigInfo
from src.pages.QT.LoginPage import LoginPage


class  LoginBusiness(LoginPage):
    #定义一个方法：实现登录功能的方法； 用来测试登录功能自动化的
    #参数1： line  读第几行数据；  跟用例层有关，到时候传进来
    #参数2：waitObject  显性等待对象； 跟用例层有关，到时候传进来
    def  loginFunction(self,line,waitObject): #形参；形式上的参数；至于具体传什么不知道
        # 先从csv文件中读取登录的测试数据； 使用到：TestData_ConfigInfo类的方法
        data = TestData_ConfigInfo().getTestData("LoginTestData.csv",   line) #读哪一行跟用例有关；
        # 再把数据传入到登录页面上； 使用LoginPage类中的方法
        self.loginOper(waitObject, data[0],data[1]  )

    #方法2： 实现预制登录功能  给其他功能进行预制登录的；例如：密码修改功能， 发送事项功能，发布公告
    def  loginDefault(self,line,waitObject):
        data = TestData_ConfigInfo().getTestData("zhanghao.csv",line)  #后面发送事项还需要预制登录；也担心密码修改会影响它；
        self.loginOper(waitObject,data[0],data[1])

