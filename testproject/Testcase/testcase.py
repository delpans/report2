import unittest
import time
from Business.Login import Login
class Testcase(unittest.TestCase):
    def setUp(self):
        print('start')

    def tearDown(self):
        print('end')
    #登陆成功
    def test_001(self):
        log = Login()
        #正确账户密码登录
        log.login('18652984541', 'zwd5201314')
        #获取用于断言的登录用户名
        data = log.get_text('id', 'JuserName')
        self.assertEquals('zhaweidong', data)

    #验证账号密码都不输入直接点击登录的测试用例
    def test_002(self):
        log = Login()
        #正确账户密码登录
        log.login('', '')
        #获取用于断言的登录用户名
        data = log.get_text('css', '.rTips')
        self.assertEquals('用户名和密码必须输入', data)

    def test_003(self):
        log = Login()
        #正确账户密码登录
        log.login('asdasd', '')
        #获取用于断言的登录用户名
        data = log.get_text('css', '.rTips')
        self.assertEquals('必须输入', data)

    def test_004(self):
        log = Login()
        #正确账户密码登录
        log.login('186529845411', 'adasda')
        #获取用于断言的登录用户名
        data = log.get_text('css', '.rTips')
        self.assertEquals('用户名或密码错误，请重新输入', data)

    def test_005(self):
        log = Login()
        #正确账户密码登录
        log.login_out('18652984541', 'zwd5201314')
        time.sleep(3)
        data = log.get_text('text', '登录')
        self.assertEquals('登录', data)
    #定位第二个页面url
    def test_006(self):
        log = Login()
        #正确账户密码登录
        log.video()
        time.sleep(3)
        data = log.current_url()
        self.assertEquals('https://v.pconline.com.cn/',data)

if __name__ == '__main__':
    unittest.main()