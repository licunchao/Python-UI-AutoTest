from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions


class  LoginPage:
    #属性   用户名框，  密码框， 登录按钮
    # 属性名 =  属性值
    #属性名是自定义的；  属性值是这个元素的定位信息（格式建议是元组）
    username_kuang = (By.NAME,"loginId")  #表示的是：name="loginId"的元素
    passwd_kuang = (By.NAME,"password") #表示的是：name="password"的元素
    login_anniu = (By.ID,"button_submit")

    duanyan_normal_login = (By.TAG_NAME,"a") #定位页面上第一个a标签；找到页面上的第一个a标签
    duanyan_feifa_login = (By.CSS_SELECTOR,'[style="max-width:440px;"]') #找style属性值是xxxx的元素

    #方法3： 针对弹框的操作； 获取文本；  给非法登录的用例使用
    def  getTanKuangText(self,waitObject):
        # 定位这个元素，然后获取文本
        return waitObject.until(expected_conditions.presence_of_element_located( self.duanyan_feifa_login )).text

    #方法2： 针对退出登录的操作；  获取文本  给正常登陆的用例使用
    def  getTuiChuText(self,waitObject):
        #定位这个元素，然后获取文本
        result = waitObject.until(expected_conditions.presence_of_element_located( self.duanyan_normal_login )).text
        return result   #返回获取到的文本信息，因为在用例层要进行断言。

    #方法： 针对元素的操作： 先定位到元素，然后进行操作
    #参数1： waitObject  定位元素是需要显性等待对象的，但是这个是用例层产生的，到时候传进来；
    #参数2： username  需要填写一个用户名，但是这个在csv文件中；到时候会读取，然后传进来
    def  loginOper(self,waitObject,username,password):
        #先定位到用户名框，然后填值
        # 定位登录名框
        waitObject.until(expected_conditions.presence_of_element_located( self.username_kuang   )).send_keys( username )
        # 先定位到密码框，然后填值
        waitObject.until(expected_conditions.presence_of_element_located(  self.passwd_kuang  )  ).send_keys(password)
        # 先定位到登录按钮，然后点击
        waitObject.until(expected_conditions.presence_of_element_located(  self.login_anniu  )).click()
