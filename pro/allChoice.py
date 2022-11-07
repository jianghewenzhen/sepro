# -*- coding:utf-8 -*-
import os
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
from tools.infoGzip import gzipjy
from tools.seproToFiles import jieyaOne, un_tar
from ui.xuanzeUI import Ui_Form


class allMain(QWidget, Ui_Form):
    _signalALL = QtCore.pyqtSignal(list)  # 定义传递变量，传递的数据为列表类型

    def __init__(self):
        super(allMain, self).__init__()
        self.setupUi(self)
        self.pushButton_openfile.clicked.connect(self.openFile)
        self.all_name = []  # 存放所有的json文件名称
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_ok.clicked.connect(self.tarFiles)

    def openFile(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, "选择文件", os.getcwd(), "Text Files(*.sepro)")  # pyqt文件选择
        # print(file_name)
        self.lineEdit_file.setText(file_name)  # 将文件名称放在输入框中显示出来

    def tarFiles(self):
        file_name = self.lineEdit_file.text()  # 获取当前选择的路径名称
        try:
            jieyaOne(file_name)  # 调用将sepro提取project
            un_tar()  # 将project解压成文件夹
            self.walkFile()  # 遍历解压成json
        except:
            self.show_message('sepro提取失败！')

    def walkFile(self):
        ss = 'project'  # 由于程序写死，第一次解压就会放在project文件夹中
        self.all_name = []  # 重新清空所有的json文件
        for root, dirs, files in os.walk(ss):  # 固定用法，遍历获取当前文件夹中的所有文件
            for f in files:
                file_name = os.path.join(root, f)  # 提取所有文件
                if file_name.endswith('.info'):  # 过滤出info文件
                    self.tarFiles2(file_name)  # 将info文件进行解压
        self._signalALL.emit(self.all_name)  # 向主页面传递当前所有的的json文件名称
        self.show_message('提取完成！')
        self.close()  # 关闭当前子页面

    def tarFiles2(self, file_name):  # 根据文件名解压成json文件
        try:
            data = gzipjy(file_name)  # gzip方式解压文件
            new_json_name = file_name.replace('info', 'json')  # 按info文件来一份json文件
            self.all_name.append(new_json_name)  # 将新的json文件增加到总的列表中
            with open(new_json_name, 'w', encoding='utf-8') as f:  # 按字符串方式写json文件
                f.write(data)
        except:
            self.show_message(file_name + '提取失败！')

    def show_message(self, msg):
        QMessageBox.information(self, "提示", msg,
                                QMessageBox.Yes)  # 最后的Yes表示弹框的按钮显示为Yes，默认按钮显示为OK,不填QMessageBox.Yes即为默认

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = allMain()
#     win.show()
#     sys.exit(app.exec_())
