import unittest

#继承Testcase类，Testcase类是测试用例类
class Test(unittest.TestCase):
    def setUp(self):
        print('hello')

    def tearDown(self):
        print('bye')
    def test001(self):
        print('001')

    def test002(self):
        print('002')

    def test003(self):
        print('003')

if __name__ == '__main__':
    #unittest.main()
    #创建测试套件
    suit = unittest.TestSuite()
    #定义一个测试用例列表
    case_list = ['test001', 'test002', 'test003']
    for case in case_list:
        suit.addTest(Test(case))
    #运行测试用例，verbosity= 2为每一个测试用例输出报告，run的参数是蚕食套件
    unittest.TextTestRunner(verbosity=2).run(suit)