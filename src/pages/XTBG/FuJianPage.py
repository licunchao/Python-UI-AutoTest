from selenium.webdriver.common.by import By

from src.common.CommonOperation import CommonOperation


class  FuJianPage(CommonOperation):
    fujian_kuangjia = (By.TAG_NAME,"iframe")
    wenjian_kuang = (By.ID,"file")
    shangchuan_anniu = (By.ID,"button_upload")
    guanbi_anniu = (By.CLASS_NAME,"d-close")  #不在框架中

    #
    def  tianJiaFujianOper(self,wait,browser,file):
        self.switchFrame("default",wait,browser)
        self.switchFrame(self.fujian_kuangjia,wait,browser)
        self.tianZhi_to_yuansu(wait, self.wenjian_kuang,  file)
        self.dianJiYuansu(wait,self.shangchuan_anniu)


    #
    def guanBiYemianOper(self, wait, browser):
        self.switchFrame("default", wait, browser)
        self.dianJiYuansu(wait,self.guanbi_anniu)