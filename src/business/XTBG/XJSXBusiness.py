from src.common.TestData_ConfigInfo import TestData_ConfigInfo
from src.pages.XTBG.JianLiuChengPage import JianLiuChengPage
from src.pages.XTBG.LiuChengTuPage import LiuChengTuPage
from src.pages.XTBG.XJSXPage import XJSXPage


class  XJSXBusiness(XJSXPage,JianLiuChengPage,LiuChengTuPage):

    #发送事项的功能
    def  faSongShiXiangFunction(self,line,wait,browser):
        #先读取测试数据：
        data = TestData_ConfigInfo().getTestData("XJSXTestData.csv",line)  #
        #点击左侧新建事项
        self.dianJiXJSX(wait,browser)
        #准备流程：
        if  data[2] !="": #流程不为空，即：有流程
            #弄流程
            #点击新建事项页面上的流程框
            self.dianJiLiuChengkuang(wait,browser)
            #在建流程页面上：添加人员：（有可能是1个人有可能是多个人）
            names = data[3]
            name_list = names.split(":")
            name_list.pop(-1)
            for  name  in  name_list:
                #把name这个人添加进去
                self.tianJiaRenYuanOper(wait,browser,name)
            #在建流程页面上：如果是串行流程，就点击串行框
            if data[2] =="串行":
                self.dianJiChuanxing(wait,browser)
            #在建流程页面上：点击确定按钮
            self.dianJiQueding_liucheng(wait,browser)
            #在流程图页面上：点击确定按钮
            self.dianJiQueding_liucheng_tu(wait,browser)

        #准备标题
        if  data[0] !="":
            self.shuRuBiaotiOper(wait,browser,data[0])

        #准备内容
        if data[1] !="":
            self.shuRuNeirongOper(wait,browser,data[1])

        #点击发送按钮
        self.dianJiFasong(wait,browser)


    #保存事项的功能
    # def baoCunShiXiangFunction(self):
    #     # 先读取测试数据：
    #
    #     # 准备内容
    #
    #     # 准备标题
    #
    #     # 准备流程：





        # 点击保存按钮
