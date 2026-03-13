from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from src.common.CommonOperation import CommonOperation


class  XJSXPage(CommonOperation):
    #界面元素： 左侧新建事项链接，标题框，流程框（操作：点击，进入到第二个页面），内容框，立即发送按钮；框架
    zuoce_xjsx_lianjie = (By.LINK_TEXT,"新建事项")
    xjsx_kuangjia = (By.ID,"iframe_main")
    biaoti_kuang = (By.ID,"subject") #在新建事项框架中
    liucheng_kuang = (By.ID,"trackInput")  #在新建事项框架中
    neirong_kuangjia  = (By.ID,"baidu_editor_0")   #在新建事项框架中
    neirong_kuang = (By.TAG_NAME,"body") #在内容框架中
    fasong_anniu = (By.ID,"button_send")   #在新建事项框架中
    baomi_xialakuang = (By.ID,"secretLevel")  #保密下拉选择框
    #保密选项：可以定义成3个；不推荐的
    # putong_xuanxiang = (By.CSS_SELECTOR,'[value="270"]')
    # jimi_xuanxiang = (By.CSS_SELECTOR,'[value="271"]')
    # juemi_xuanxiang = (By.CSS_SELECTOR,'[value="272"]')
    #可以定义成1个： 建议配置成字典格式
    baomi_xuanxiang = {
                       "普通":(By.CSS_SELECTOR,'[value="270"]'),
                       "机密":(By.CSS_SELECTOR,'[value="271"]'),
                       "绝密":(By.CSS_SELECTOR,'[value="272"]')
                       }  #字典：  可以通过key， 来获取value(定位信息），拿到定位信息就可以定位到选项
                          #从csv文件中取到key(机密）， 然后机密，拿到：(By.CSS_SELECTOR,'[value="271"]')； 定位机密选项，可以click
    #baomi_xuanxiang_liebiao = [(By.CSS_SELECTOR,'[value="270"]'),(By.CSS_SELECTOR,'[value="271"]'),(By.CSS_SELECTOR,'[value="272"]')]


    guanlian_xiangmu_kuang = (By.ID,"projectName")

    tianjia_fujian = (By.ID,"button_attach")

    #方法：点击添加附件
    def  dianJiFujian(self, wait, browser):
        # 切到默认框架
        self.switchFrame("default", wait, browser)
        # 切到新建事项框架
        self.switchFrame(self.xjsx_kuangjia, wait, browser)
        #点击添加附件
        self.dianJiYuansu(wait,self.tianjia_fujian)

    #方法：针对关联项目框的操作
    def  guanLianXiangmuOper(self, wait, browser):
        # 切到默认框架
        self.switchFrame("default", wait, browser)
        # 切到新建事项框架
        self.switchFrame(self.xjsx_kuangjia, wait, browser)
        #1.先定位到这个框；  赋值给变量：element
        element = wait.until(expected_conditions.presence_of_element_located(self.guanlian_xiangmu_kuang))
        # 2.删除这个框的只读属性； 结合js语句技术；准备删除只读属性的js语句；
        js = 'arguments[0].removeAttribute("readonly")'  #表示：删除只读属性；   删除哪个元素的？
        # 3.执行js语句；将这个框中的只读属性删除掉 （selenium中提供了执行js语句的方法）
        browser.execute_script(js,element)  #删除element元素中的只读顺序性
        # 4.就可以给这个框中写值了
        element.send_keys("sdkfjsdkfsdf")

    #方法： 针对保密程度的操作
    def  baoMiChengduOper(self, wait, browser,  baomi_chengdu):
        # 切到默认框架
        self.switchFrame("default", wait, browser)
        # 切到新建事项框架
        self.switchFrame(self.xjsx_kuangjia, wait, browser)
        #先点击下拉选择框
        self.dianJiYuansu(wait,self.baomi_xialakuang)
        #再点击其中一个选项;例如： 点击机密
        self.dianJiYuansu(wait,  self.baomi_xuanxiang[baomi_chengdu] )

        # if baomi_chengdu == "普通":
        #     index = 0
        #     #self.dianJiYuansu(wait, self.putong_xuanxiang)
        # elif baomi_chengdu == "机密":
        #     index = 1
        #     #self.dianJiYuansu(wait, self.jimi_xuanxiang)
        # else:
        #     index = 2
        #     #self.dianJiYuansu(wait, self.juemi_xuanxiang)
        # self.dianJiYuansu(wait, self.baomi_xuanxiang_liebiao[index])



    #方法1： 针对左侧新建事项连接的操作
    def  dianJiXJSX(self,wait,browser):
        #切到默认框架
        self.switchFrame("default",wait,browser)
        #点击新建事项连接
        self.dianJiYuansu(wait,self.zuoce_xjsx_lianjie)

    #方法2：针对发送按钮的操作
    def  dianJiFasong(self,wait,browser):
        #切到默认框架
        self.switchFrame("default",wait,browser)
        #切到新建事项框架
        self.switchFrame(self.xjsx_kuangjia,wait,browser)
        #点击立即发送按钮
        self.dianJiYuansu(wait,self.fasong_anniu)

    #方法3：针对标题框的操作
    def  shuRuBiaotiOper(self, wait, browser,biaoti):
        # 切到默认框架
        self.switchFrame("default", wait, browser)
        # 切到新建事项框架
        self.switchFrame(self.xjsx_kuangjia, wait, browser)
        #输入标题
        self.tianZhi_to_yuansu(wait,self.biaoti_kuang,biaoti)

    #方法4：针对流程框的操作（点击）
    def  dianJiLiuChengkuang(self, wait, browser):
        # 切到默认框架
        self.switchFrame("default", wait, browser)
        # 切到新建事项框架
        self.switchFrame(self.xjsx_kuangjia, wait, browser)
        #点击流程框
        self.dianJiYuansu(wait,self.liucheng_kuang)

    #方法5：针对内容框的操作
    def  shuRuNeirongOper(self, wait, browser,neirong):
        # 切到默认框架
        self.switchFrame("default", wait, browser)
        # 切到新建事项框架
        self.switchFrame(self.xjsx_kuangjia, wait, browser)
        #切到内容框架
        self.switchFrame(self.neirong_kuangjia,wait,browser)
        #输入内容
        self.tianZhi_to_yuansu(wait,self.neirong_kuang, neirong)

