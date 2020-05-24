import unittest
from Testcase.testcase import Testcase
from Commonlib.HTMLTestRunner import HTMLTestRunner

class Test(unittest.TestCase):
    def test_suit(self):
        #创建测试套件
        mysuit = unittest.TestSuite()

        #向测试套件中添加测试用例
        case_list = ['test_001','test_002','test_003','test_004','test_005']
        for case in case_list:
            mysuit.addTest(Testcase(case))
        #使用runner运行测试用例
        #unittest.TextTestRunner(verbosity=2).run(mysuit)

        #生成html格式测试报告的步骤
        with open('../report.html', 'wb')as f:
            HTMLTestRunner(
                stream=f,                 #设定测试数据写入哪个文件
                title='第一个测试报告',    #设定测试报告标题
                description='itcast 软件测试第一版',
                verbosity=2
            ).run(mysuit)

if __name__ == '__main__':
    unittest.main()