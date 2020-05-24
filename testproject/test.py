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
    unittest.main()




#unittest.main()运行时，框架自动寻找TestCase子类，并且运行
#在TestCase类中，只能把test开头的方法当作测试用例，然后执行
#setup()用于在测试用例执行前被调用，teardown（）用于清理，在测试用例执行之后调用