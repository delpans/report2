from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
class Commonshare(object):
    #初始化
    def __init__(self):

        #创建浏览器
        self.driver = webdriver.Firefox()
        #最大化
        self.driver.maximize_window()
    #前进
    def driver_forward(self):
        self.driver.forward()

    #后退
    def driver_back(self):
        self.driver.back()

    #打开url
    def open_url(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    #获取标题
    def get_title(self):
        return  self.driver.title

    #获取url
    def current_url(self):
        return self.driver.current_url

    #切换句柄
    def current_handle(self):
        all_handles = self.driver.window_handles
        for handle in all_handles:
            self.driver.switch_to.window(handle)

    #封装定位方法
    def locateElement(self,locate_type,value):
        el = None
        if locate_type == 'id':
            el = self.driver.find_element_by_id(value)
        elif locate_type == 'name':
            el =self.driver.find_element_by_name(value)
        elif locate_type == 'class':
            el = self.driver.find_element_by_class_name(value)
        elif locate_type == 'tag':
            el =self.driver.find_element_by_tag_name(value)
        elif locate_type == 'text':
            el =self.driver.find_element_by_link_text(value)
        elif locate_type == 'partial':
            el = self.driver.find_element_by_partial_link_text(value)
        elif locate_type == 'xpath':
            el =self.driver.find_element_by_xpath(value)
        elif locate_type == 'css':
            el =self.driver.find_element_by_css_selector(value)
        #返回定位元素，定位到元素才返回元素
        if el is not None:
            return el

    #对点击元素的封装
    def click(self,locate_type,value):
       #调用locateElement()
        el = self.locateElement(locate_type,value)
        el.click()

    #对定位到的元素进行文本输入
    def input_data(self,locate_type,value,data):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        el.send_keys(data)

    #上传文件
    def upload_file(self,locate_type,value,file):
        self.input_data(locate_type,value,).send_keys(file)

    #获取定位到的元素的文本内容<a>xxx</a>
    def get_text(self,locate_type, value):
       #调用locateElement()
        el = self.locateElement(locate_type,value)
        return el.text

    # 获取定位到的元素中的标签属性
    def get_attr(self, locate_type, value, data):
        # 调用locateElement()
        el = self.locateElement(locate_type, value)
        return el.get_attribute(data)

    def windows_down(self,x,y):
        js = "window.scrollTo(x,y)"
        self.driver.execute_script(js)
    def windows_up(self,n):
        jd = "var q = document.documentElement.scrollTOP = n"
        self.driver.execute_script(jd)
    #下拉选择框
    #索引定位
    def select_index(self,select_type,value,index):
        ele = self.locateElement(select_type,value)
        Select(ele).select_by_index(index)
    #值定位
    def select_text(self,select_type,value,text):
        ele = self.locateElement(select_type,value)
        Select(ele).select_by_value(text)
    #可视文字定位
    def select_visible_text(self,select_type,value,vis_text):
        ele = self.locateElement(select_type,value)
        Select(ele).select_by_visible_text(vis_text)

    #设置等待时间
    # def force_wait(self, seconds):
    #     sleep(seconds)



    #结束时清理
    def __del__(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    com = Commonshare()
    #com.open_url('http://www.baidu.com')
    com.open_url('https://www.pconline.com.cn/')
    com.get_attr('text', '登录')
    # 定位并输入密码
    # com.input_data('name', 'username','18652984541')
    # com.input_data('name', 'password','zwd5201314')

