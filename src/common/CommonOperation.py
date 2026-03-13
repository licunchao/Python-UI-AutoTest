from time import strftime

import os

import pymysql
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from src.common.TestData_ConfigInfo import TestData_ConfigInfo


class  CommonOperation:

    #通用方法1： 截图；
    def  getPicture(self,browser,name):
        # 截图
        sysTime = strftime("%Y%m%d%H%M%S") #获取系统时间赋值给变量sysTime
        pngName = sysTime + name+".png"  #将系统时间拼接上name参数传进来的名字，拼接上后缀名， 赋值给变量pngName
        dirPath = os.path.dirname(__file__)  #获取当前py文件所在的路径
        pngFile = os.path.join(dirPath, "..", "..", "pictures", pngName)  #准备截图文件所在路径和文件名
        browser.get_screenshot_as_file(pngFile) #进行截图；把截图的内容放入到pngFile文件中

    #通用方法2： 定位元素并且点击
    def  dianJiYuansu(self,wait,element):
        wait.until(expected_conditions.presence_of_element_located(  element )).click()

    #通用方法3：定位元素，然后填值
    def  tianZhi_to_yuansu(self,wait,element,value):
        wait.until(expected_conditions.presence_of_element_located( element  )).send_keys(  value   )

    #定位到框之后，先清空，再输值
    def  clear_sendKeys(self,wait,element,value):
        #定位元素
        yuansu =  wait.until(expected_conditions.presence_of_element_located( element  )) #定位element这个元素赋值给变量yuansu
        #清空
        yuansu.clear()
        #输入
        yuansu.send_keys(value)



    #通用方法4： 封装一个方法可以切3种框架；把上面那3个方法合并到一个方法中。
    #区分3种切框架： 就需要通过一个参数frame；
    # 如果这个参数frame传进来是default；表示切默认；
    # 如果这个参数frame传进来是parent表示切上一级；如果不是前面这2个，切到某一个
    def  switchFrame(self, frame,wait,browser):
        if  frame=="default":
            browser.switch_to.default_content()
        elif frame =="parent":
            browser.switch_to.parent_frame()
        else:
            wait.until(expected_conditions.frame_to_be_available_and_switch_to_it(   frame  ))


    #补充：有的项目中：把定位元素也专门封装到一个方法中,定位之后返回这个元素；  然后再点击，然后再填值

    # def  switchDefault(self):
    #
    # def  switchParent(self):
    #
    # def  switch_to_frame(self):


    #通用方法5： 初始化方法
    def  chuShiHua(self):
        browser = webdriver.Firefox()  # 打开一个火狐浏览器，并且赋值给变量browser（就表示火狐浏览器）
        # 从url.csv中取网址
        urlDict = TestData_ConfigInfo().getConfigData("url.csv")
        browser.get(urlDict["url"])
        # 实例化一个显性等待对象
        wait = WebDriverWait(browser, 10)
        return browser,wait #返回这两个东西；因为在用例层要使用

    #通用方法6： 连接mysql数据库并且执行sql语句
    def  connDB_execSQL(self,sql):
        # 1.准备连接数据库的信息（host, port, dbname, username, passwd)，从db.csv中读取
        dbDict = TestData_ConfigInfo().getConfigData("db.csv")
        print(dbDict)
        # 2. 写代码来连接mysql数据库；获取数据库的连接对象，赋值给变量conn
        conn = pymysql.connect(host=dbDict['Host'], user=dbDict['Username'], password=dbDict['Passwd'],
                               database=dbDict['dbName'], port=int(dbDict['Port']), charset='utf8')
        # 3. 通过数据库的连接，获取数据库的游标
        youbiao = conn.cursor()  #cursor游标英文单词；  获取游标，赋值给变量youbiao
        # 4.在数据库的游标中来执行SQL语句；
        youbiao.execute(sql)  #可能执行select，可能执行update；可能执行insert delete  create  等：
        # 5. 如果是select语句：可以从游标中获取查询结果；如果是其他语句：结果为none
        result = youbiao.fetchall()  #从游标中取出所有的查询结果，赋值给变量result
        # 6. 如果是DML语句；要数据库事务
        conn.commit()  #提交数据库事务
        # 7. 关闭游标，关闭数据库连接
        youbiao.close()
        conn.close()
        # 8. 返回查询结果；
        return  result

if __name__=="__main__":
    # sql = "SELECT loginid,PASSWORD FROM oa_tbl_employee WHERE loginId IN('sup','fuc','xingjj');"
    # sqlResult = CommonOperation().connDB_execSQL(sql)
    # print(sqlResult)
    # print(sqlResult[2][1])
    zhanghao = TestData_ConfigInfo().getTestData("zhanghao.csv",1)
    sql_select = "SELECT PASSWORD FROM oa_tbl_employee WHERE loginId='%s';"%(zhanghao[0])
    print(sql_select)
    sqlResult = CommonOperation().connDB_execSQL(sql_select)
    print(sqlResult)
    oldPasswd = sqlResult[0][0]
    #字符串格式化
    # "SELECT PASSWORD FROM oa_tbl_employee WHERE loginId='sup';"
    #"SELECT PASSWORD FROM oa_tbl_employee WHERE loginId='xingjj';"
    # "SELECT PASSWORD FROM oa_tbl_employee WHERE loginId='songn';"

    sql_update = "UPDATE oa_tbl_employee  SET  PASSWORD='%s'  WHERE loginId='%s';"%(oldPasswd,zhanghao[0])
    print(sql_update)
    CommonOperation().connDB_execSQL(sql_update)

