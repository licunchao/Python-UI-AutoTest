from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.common.CommonOperation import CommonOperation


class  ChangePasswdPage(CommonOperation):
    #界面元素：  首页上的密码修改链接，  旧密码框，新密码框，确认密码框，保存按钮；
    #取消按钮（如果要测试取消修改密码功能，就需要，如果不测试就不需要）；框架iframe标签
    shouye_mimaxiugai = (By.LINK_TEXT,"密码修改")
    mima_kuangjia = (By.XPATH,'//iframe[  contains(@src,"/oa/common/tools/updatePassword.jsp")    ]')
    jiu_mima_kuang = (By.ID, "oldpassword")
    xin_mima_kuang = (By.ID, "newpassword")
    quRen_mima_kuang = (By.ID, "passwordagain")
    baocun_anniu = (By.ID, "button_save")
    quxiao_anniu = (By.ID, "button_cancel")

    #方法1： 主要是针对3个框的操作
    def  shuRuMiMaOper(self,wait,browser,oldPasswd,newPasswd,againPasswd):
        #先点击首页上的密码修改链接
        self.dianJiYuansu(wait,self.shouye_mimaxiugai)
        #切框架：切到密码框架
        #wait.until(expected_conditions.frame_to_be_available_and_switch_to_it( self.mima_kuangjia  ))#结合显性等待方式的切框架；
        self.switchFrame(self.mima_kuangjia,wait,browser)
        #输入旧密码
        self.tianZhi_to_yuansu(wait,self.jiu_mima_kuang,oldPasswd)
        #输入新密码
        self.tianZhi_to_yuansu(wait,self.xin_mima_kuang,newPasswd)
        #输入确认密码
        self.tianZhi_to_yuansu(wait,self.quRen_mima_kuang,againPasswd)

    #方法2：针对保存按钮的操作
    def  dianJiBaoCunOper(self,wait):
        self.dianJiYuansu(wait, self.baocun_anniu)

    #方法3：针对取消按钮的操作
    def dianJiQuXiaoOper(self,wait):
        self.dianJiYuansu(wait, self.quxiao_anniu)

