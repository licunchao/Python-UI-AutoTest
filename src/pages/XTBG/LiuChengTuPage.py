from selenium.webdriver.common.by import By

from src.common.CommonOperation import CommonOperation


class  LiuChengTuPage(CommonOperation):
    # 元素：框架， 确定按钮
    liucheng_tu_kuangjia = (By.TAG_NAME,"iframe")
    liucheng_tu_queding_anniu = (By.ID,"button_cancel")

    #方法1：点击确定按钮
    def  dianJiQueding_liucheng_tu(self,wait,browser):
        #切到默认框架
        self.switchFrame("default",wait,browser)
        #切到流程图框架
        self.switchFrame(self.liucheng_tu_kuangjia,wait,browser)
        #点击确定按钮
        self.dianJiYuansu(wait,self.liucheng_tu_queding_anniu)