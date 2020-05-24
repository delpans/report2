from Commonlib.commonlib import Commonshare
import time

class Login(Commonshare):
    def login(self,user,pwd):
        self.open_url('https://www.pconline.com.cn/')
        #定位到登录按钮进行点击，点击之后进入太平洋登陆界面
        self.click('text','登录')
        #定位并输入密码
        self.input_data('name','username',user)
        self.input_data('name','password',pwd)

        self.click('name','button')
    def login_out(self,user,pwd):
        self.login(user,pwd)
        self.click('css', '#Jnb-tit-user > i:nth-child(2)')
        self.click('css', '.nb-user-tf > a:nth-child(2)')

    def video(self):
        self.open_url('https://www.pconline.com.cn/')
        #定位到登录按钮进行点击，点击之后进入太平洋登陆界面
        self.click('text','视频')
        time.sleep(3)
        self.current_handle()
if __name__ == '__main__':
    log = Login()
    log.login('18652984541', 'zwd5201314')