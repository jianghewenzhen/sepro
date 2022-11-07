# -*- coding:utf-8 -*-
import os
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox

from tools.infoGzip import gzipjy
from ui.xuanzeUI import Ui_Form


class infoMain(QWidget, Ui_Form):
    _signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super(infoMain, self).__init__()
        self.setupUi(self)
        self.pushButton_openfile.clicked.connect(self.openFile)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_ok.clicked.connect(self.tarFiles)

    def openFile(self):
        file_name, file_type = QFileDialog.getOpenFileName(self, "选择文件", os.getcwd(), "Text Files(*.info)")  # pyqt文件选择
        # print(file_name)
        self.lineEdit_file.setText(file_name)  # 将文件名称放在输入框中显示出来

    def tarFiles(self):
        new_json_name = None  # 由于传递参数，定义初始变量
        file_name = self.lineEdit_file.text()  # 获取当前选择的路径名称
        try:
            data = gzipjy(file_name)  # gzip方式解压文件
            new_json_name = file_name.replace('info', 'json')  # 按info文件来一份json文件
            with open(new_json_name, 'w', encoding='utf-8') as f:  # 按字符串方式写json文件
                f.write(data)
            self.show_message('提取成功！')
            self.close()  # 关闭当前子页面
        except:
            self.show_message('提取失败！')
        self._signal.emit(new_json_name)  # 传递当前处理为文件名称

    def show_message(self, msg):
        QMessageBox.information(self, "提示", msg,
                                QMessageBox.Yes)  # 最后的Yes表示弹框的按钮显示为Yes，默认按钮显示为OK,不填QMessageBox.Yes即为默认

    # def lian(self, data):
    #     for key in data.keys():
    #         print(key)
    #         print(data[key])
    #         if type(data[key]) == 'dict':
    #
    #             self.lian(data[key])
    #         elif type(data[key]) == 'list':
    #             for d in data[key]:
    #                 print(d)
    #                 if type(d) == 'dict':
    #                     self.lian(data[key])
    #         else:
    #             pass


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = infoMain()
#     win.show()
#     sys.exit(app.exec_())
