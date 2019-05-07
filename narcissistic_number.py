import ssl,json,base64,sys,random
import urllib
from urllib import request,parse 
from http import cookiejar

from PyQt5.QtCore import Qt,QCoreApplication
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton, QMainWindow, QHBoxLayout, QVBoxLayout,  QLineEdit
from PyQt5.QtGui import QPixmap

#设置忽略SSL验证
ssl._create_default_https_context = ssl._create_unverified_context
#声明一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()
#利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
handler=request.HTTPCookieProcessor(cookie)
#通过CookieHandler创建opener
opener = request.build_opener(handler)

headers = {
	"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "RAIL_EXPIRATION=1557502844145; RAIL_DEVICEID=ECCWUO3R_BVL62e0mKrR0PPOvlXcEUgZF7ekHk2eRZA5EAWvc9QE-KV01KgM73PikQ4tX3-AKA2iA8PB63ys83oNKE6aG4xlGzcXe7_AuyAJGsWh4vk8CBhGFjExtrzv8KeCdVvvcx6DjsVm0jUCL51v4k1Pm8xK",
}

request.install_opener(opener)

def login(username,password,code):
    req = request.Request("https://kyfw.12306.cn/otn/login/init", headers = headers)
    result=request.urlopen(req).read()
    result = result.decode("utf-8")
    print(cookie)



    request.urlretrieve("https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&"+str(random.random()),"code.png")
    code = input("请输入验证码:")
    data   = {
        "answer": code,
        "login_site": "E",
        "rand": "sjrand",
    }

    data = parse.urlencode(data).encode('utf-8')
    req = request.Request("https://kyfw.12306.cn/passport/captcha/captcha-check", data = data, headers = headers, method = "POST")
    result=request.urlopen(req).read()
    result = result.decode("utf-8")
    print(cookie)
    print(result)
    #username = input("请输入登录名:")
    #password = input("请输入密  码:")
    #username = "zhang743208535@163.com"
    #password = "342511abc"
    data   = {
        "username": username,
        "password": password,
        "appid":"otn",
    }
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request("https://kyfw.12306.cn/passport/web/login", data = data, headers = headers, method = "POST")
    result = request.urlopen(req).read()
    result = result.decode("utf-8")
    print(cookie)
    print(result)
login("zhang743208535@163.com","342511abc","2")


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.number = []
        self.initUI()
    def initUI(self):
        acc_title = QLabel('账   号')
        pass_title = QLabel('密   码')

        self.acc_edit = QLineEdit()
        self.pass_edit = QLineEdit()
        self.pass_edit.setEchoMode(QLineEdit.Password)

        self.btn_ok = QPushButton("确定", self)
        self.btn_on = QPushButton("取消", self)

        lbl = QLabel(self)
        pixmap = QPixmap("code.jpg")
        lbl.setPixmap(pixmap)
        lbl.setScaledContents (True)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(acc_title, 1, 0)
        grid.addWidget(self.acc_edit, 1, 1)
        grid.addWidget(pass_title, 2, 0)
        grid.addWidget(self.pass_edit, 2, 1)
        #参数表示控件名，行，列，占用行数，占用列数
        grid.addWidget(lbl, 3, 0 ,1 ,0)

        grid.addWidget(self.btn_ok, 4, 0)
        grid.addWidget(self.btn_on, 4, 1)

        self.btn_ok.clicked.connect(self.buttonClicked)
        self.btn_on.clicked.connect(self.buttonClicked)

        self.setLayout(grid)
        #self.setGeometry(300, 300, 300, 300)
        self.adjustSize()
        self.setWindowTitle('code')
        self.show()

    def buttonClicked (self, e):
        sender = self.sender()
        if sender == self.btn_ok:
            username = self.acc_edit.text()
            password = self.pass_edit.text()
            code = ",".join(self.number)
            login(username,password,code)
        elif sender == self.btn_on:
            self.btn_on.clicked.connect(QCoreApplication.quit)
    def mouseMoveEvent(self, e):
    	pass
    def mousePressEvent (self,  event):
    	self.number += [str(event.x()-13), str(event.y()-42)]
    	print( ",".join(self.number))
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())
