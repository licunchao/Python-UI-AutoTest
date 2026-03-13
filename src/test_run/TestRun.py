import os
import unittest
from time import strftime

from BeautifulReport import BeautifulReport


class  TestRun:

    #定义方法：执行用例，生成测试报告的方法
    def runCases(self):
        dirPath = os.path.dirname(__file__)
        # 1.先找到这些用例(xxxx.py)(路径 + 多个文件名.py)，把这些用例组装到测试套件中；
        casePath = os.path.join(dirPath,"..","test_case") #测试用例路径
        taojian = unittest.defaultTestLoader.discover(casePath,pattern="*TestCase.py") #找casePath路径下：所有的以TestCase.py结尾的文件，执行所有的用例
        # 2.准备测试报告文件； （路径 ， 测试报告文件名.html), 测试报告文件名中要包含系统时间
        reportPath = os.path.join(dirPath,"..","..","reports") #测试报告存放路径
        sysTime = strftime("%Y%m%d%H%M%S")
        reportName = sysTime+"OAReport.html"  #测试报告文件名
        # 3.把用例的执行结果写入到测试报告中。
        result = BeautifulReport(taojian)  #实例化BeautifulReport对象，要执行套件中的用例
        result.report(description="haha",filename=reportName,report_dir=reportPath)  #把用例的执行结果，写入到测试报告中


if __name__=="__main__":
    TestRun().runCases()