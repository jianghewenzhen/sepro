# -*- coding:utf-8 -*-
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from pro.allChoice import allMain
from pro.biaoge import biaogeMain
from pro.biaoge2 import biaogeMain2
from pro.fileChoice import fileMain
from pro.infoChoice import infoMain
from ui.mainUI import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('SE程序解析-1.0')  # 修改软件窗口标题
        self.file_choice = fileMain()  # 导入文件选择窗口；sepro提取成文件夹
        self.info_choice = infoMain()  # 导入选择文件窗口，选择info文件进行解压
        self.all_choice = allMain()  # 导入文件选择窗口，sepro全部解压提取

        self.action_sepro.triggered.connect(self.fileChoiceShow)
        self.action_info.triggered.connect(self.infoChoiceShow)
        self.actionseproall.triggered.connect(self.allChoiceShow)

    def fileChoiceShow(self):
        self.file_choice.show()  # 文件选择窗口显示

    def infoChoiceShow(self):
        self.info_choice.show()  # 文件选择窗口显示
        self.info_choice._signal.connect(self.biaogeShow)  # 接收子窗口传递过来的数据并联动单个json文件解析显示

    def allChoiceShow(self):
        self.all_choice.show()  # 文件选择窗口显示
        self.all_choice._signalALL.connect(self.biaogeShow2)  # 接收子窗口传递过来的数据并联动所有json文件解析显示

    def biaogeShow(self, json_name):
        self.allUICloice()  # 所有的窗口页面关闭
        self.biaogeXs = biaogeMain()  # 初始化单个json显示程序
        self.gridLayout.addWidget(self.biaogeXs)  # 将页面放在layout中
        self.biaogeXs.json_name = json_name  # 上个子页面传递过来的数据在赋值给显示程序的全局变量
        self.biaogeXs.textShow()  # 调用程序显示函数，显示单个json的结果
        self.biaogeXs.show()  # 页面显示

    def biaogeShow2(self, all_name):
        self.allUICloice()  # 所有的窗口页面关闭
        self.biaogeXs2 = biaogeMain2()  # 初始化所有json显示程序
        self.gridLayout.addWidget(self.biaogeXs2)  # 将页面放在layout中
        self.biaogeXs2.all_name = all_name  # 上个子页面传递过来的数据在赋值给显示程序的全局变量
        self.biaogeXs2.toBg()  # 调用程序显示函数，显示所有json的结果
        self.biaogeXs2.show()  # 页面显示

    def allUICloice(self):
        for i in range(self.gridLayout.count()):  # 遍历layout中的所有元素
            self.gridLayout.itemAt(i).widget().deleteLater()  # 清除layout中的子页


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec_())
