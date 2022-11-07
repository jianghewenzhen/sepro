# -*- coding:utf-8 -*-

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget

from tools.jsonMode import QJsonModel
from ui.biaogeUI import Ui_bgForm


class biaogeMain(QWidget, Ui_bgForm):
    # _signalBg = QtCore.pyqtSignal(str)

    def __init__(self):
        super(biaogeMain, self).__init__()
        self.setupUi(self)
        self.json_name = ''  # 单个json文件名
        self.pushButton_search.clicked.connect(self.findMsg)

    def textShow(self):  # 在右侧窗口显示提示
        self.textEdit.clear()
        log = '解析文件：' + self.json_name
        self.textEdit.append(log)
        self.toBg()

    def toBg(self):  # 在中间显示json内容
        # self.treeView.clear()
        self.setStyleSheet(
            "QTreeView::item:selected{color:#080808;background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #66FE81,stop:1 #56FE73);}")  # 改变选中时状态和颜色
        model = QJsonModel()  # 定义json数据模型
        self.treeView.setModel(model)  # treeview采用当前模型
        model.load(self.json_name)  # 解析json文件
        self.treeView.show()  # 结果显示

    def findMsg(self):  # 未完成搜索
        msg = self.lineEdit.text()
        if msg != '':
            pass
