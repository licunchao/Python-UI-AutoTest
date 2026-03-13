import csv
import os


class  TestData_ConfigInfo:    #建议类名和模块名一样；当然不一样也可以
    # 方法一：读取测试数据文件内容的:读取任何的csv测试数据文件的 ；
    #参数1：  fileName  从外面传进来一个文件名， 传什么读什么；由调用的人来决定读哪一个csv文件；
    #参数2： line  指定返回哪一行数据； 例如：line  1 返回第一行； line  3  返回第三行
    def  getTestData(self,fileName,line):
        # 1）先找到这个csv文件；(路径 + 文件名.csv)
        dirPath = os.path.dirname(__file__)  ##获取当前文件所在的路径；并且赋值给变量dirPath
        dataFile = os.path.join(dirPath,"..","..","data",fileName) #要读取一个csv测试数据文件，但是是哪一个不知道。
        # 2）打开这个csv文件
        with  open(dataFile,'r',encoding="utf8")  as  f: #打开一个文件，读内容，支持汉字。打开之后赋值给变量f
            # 3）读取这个文件中的内容；  采用csv库（python自带的）；
            fileContent =  csv.reader(f) #读出来的是迭代器；提高代码效率；开发用的多
            # 4）把内容变成列表格式；
            list_data = list(fileContent) #把迭代器直接转换成列表
        # 5）把读取的数据要返回出去，按行返回 （因为后续要使用这个数据，要写到页面上）
        #返回一行数据,至于是哪一行不清楚；
        return  list_data[line-1]

    #方法二：读取配置文件内容的
    def  getConfigData(self,fileName):
        # 1）先找到这个csv文件；(路径 + 文件名.csv)
        dirPath = os.path.dirname(__file__)  ##获取当前文件所在的路径；并且赋值给变量dirPath
        configFile = os.path.join(dirPath, "..", "..", "config", fileName)  # 要读取一个csv测试数据文件，但是是哪一个不知道。
        # 2）打开这个csv文件
        with  open(configFile, 'r', encoding="utf8")  as  f:  # 打开一个文件，读内容，支持汉字。打开之后赋值给变量f
            # 3）读取这个文件中的内容；  采用csv库（python自带的）；
            fileContent = csv.reader(f)  # 读出来的是迭代器；提高代码效率；开发用的多
            # 4）把内容变成字典格式；
            configDict = dict(fileContent)
        # 5）把读取的数据要返回出去，全部返回 （因为后续要使用配置信息）
        return configDict



if  __name__ =="__main__":
    object = TestData_ConfigInfo()
    # data = object.getTestData("LoginTestData.csv",3)   #读取一行数据，返回给变量data
    # print(data)
    dict = object.getConfigData("db.csv")
    print(dict)