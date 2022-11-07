# -*- coding:utf-8 -*-

import os
import sys
import json
from PyQt5 import QtCore
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from ui.biaoge2UI import Ui_bg2Form
from tools.jsonMode import QJsonModel

class biaogeMain2(QWidget, Ui_bg2Form):
    # _signalBg = QtCore.pyqtSignal(str)
    def __init__(self):
        super(biaogeMain2, self).__init__()
        self.setupUi(self)
        self.all_name = []  # 定义所有的json文件名列表
        self.all_tab_dic = {}  # 定义tab widget变量字典
        self.all_layout_dic = {}  # 定义layout变量字典
        self.all_tree_dic = {}  # # 定义tree变量字典

    def toBg(self):
        # print(self.all_name)
        # 改变选中时状态和颜色
        self.setStyleSheet(
            "QTreeView::item:selected{color:#080808;background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #66FE81,stop:1 #56FE73);}")
        for name in self.all_name:  # 遍历所有的json名称
            file_name = name.split("\\")[-1].replace('.json', '')  # 由于json文件名中含有路径，只提取文件名
            self.all_tab_dic[file_name] = QtWidgets.QWidget()  # 定义页面tab元素
            self.all_tab_dic[file_name].setObjectName('tab_'+file_name)  # 设置tab元素名称
            self.all_layout_dic[file_name] = QtWidgets.QVBoxLayout(self.all_tab_dic[file_name])  # 定义页面layout元素
            self.all_layout_dic[file_name].setObjectName('Layout_'+file_name)  # 设置layout元素名称
            self.all_tree_dic[file_name] = QtWidgets.QTreeView(self.all_tab_dic[file_name])  # 定义页面tree元素
            self.all_tree_dic[file_name].setObjectName("treeView_"+file_name)  # 设置tree元素名称
            self.all_layout_dic[file_name].addWidget(self.all_tree_dic[file_name])  # 将tree元素放在layout中显示
            self.tabWidget.addTab(self.all_tab_dic[file_name], file_name)  # 将tab放在widget中
        # 可以和上面合并
        for name in self.all_name:
            model = QJsonModel()  # 重新初始化采用的json模型
            model.load(name)  # 模型数据显示
            file_name = name.split("\\")[-1].replace('.json', '')
            self.all_tree_dic[file_name].setModel(model)
            self.all_tree_dic[file_name].show()






