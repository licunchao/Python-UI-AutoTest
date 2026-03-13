from selenium.webdriver.common.by import By

from src.common.CommonOperation import CommonOperation


class  JianLiuChengPage(CommonOperation):
    #框架， 搜索框，查询按钮，添加全部按钮，串行单选框，确定按钮;
    liucheng_kuangjia = (By.TAG_NAME,"iframe")
    sousuo_kuang = (By.ID,"deptEmpName")
    chaxun_anniu = (By.CSS_SELECTOR,'[title="点击查询"]')
    quanbu_anniu = (By.CSS_SELECTOR,'[title="添加全部"]')
    chuanxing_kuang = (By.ID,"instanceType_2")
    liucheng_queding_anniu = (By.CSS_SELECTOR,'[title="确定"]')  #确定按钮很多页面都可能会有，尽量避免重名
    #方法1：  添加人员的方法：  搜索框，查询按钮，添加全部按钮
    def  tianJiaRenYuanOper(self,wait,browser,name):
        #切到默认框架
        self.switchFrame("default",wait,browser)
        #切到流程框架
        self.switchFrame(self.liucheng_kuangjia,wait,browser)
        #搜索框：写名字
        self.clear_sendKeys(wait,self.sousuo_kuang,name)
        #点击查询按钮
        self.dianJiYuansu(wait,self.chaxun_anniu)
        #点击添加全部按钮
        self.dianJiYuansu(wait,self.quanbu_anniu)


    #方法2：点击串行的方法
    def dianJiChuanxing(self,wait,browser):
        #切到默认框架
        self.switchFrame("default",wait,browser)
        #切到流程框架
        self.switchFrame(self.liucheng_kuangjia,wait,browser)
        #点击串行
        self.dianJiYuansu(wait,self.chuanxing_kuang)


    #方法3：点击确定的方法
    def  dianJiQueding_liucheng(self,wait,browser):
        #切到默认框架
        self.switchFrame("default",wait,browser)
        #切到流程框架
        self.switchFrame(self.liucheng_kuangjia,wait,browser)
        #点击确定按钮
        self.dianJiYuansu(wait,self.liucheng_queding_anniu)