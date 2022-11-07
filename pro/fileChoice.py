# -*- coding:utf-8 -*-
import os
import sys

from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox

from tools.seproToFiles import jieyaOne, un_tar
from ui.xuanzeUI import Ui_Form


class fileMain(QWidget, Ui_Form):
    def __init__(self):
        super(fileMain, self).__init__()
        self.setupUi(self)
        self.pushButton_openfile.clicked.connect(self.openFile)
        # self.pushButton_cancel.clicked.connect(QCoreApplication.instance().quit)
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
            self.show_message('提取成功！')
            self.close()   # 关闭当前子页面
        except:
            print('工程提取失败')

    def show_message(self, msg):
        QMessageBox.information(self, "提示", msg,
                                QMessageBox.Yes)  # 最后的Yes表示弹框的按钮显示为Yes，默认按钮显示为OK,不填QMessageBox.Yes即为默认

#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = fileMain()
#     win.show()
#     sys.exit(app.exec_())
