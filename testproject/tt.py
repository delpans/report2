from selenium import webdriver
import unittest

d = webdriver.Firefox()
d.get('https://www.pconline.com.cn/')

handles = d.window_handles
d.
class Testcase(unittest.TestCase):
    def test_1(self):
        self.assertEquals('bu登录',data)

if __name__ == '__main__':
    unittest.main()