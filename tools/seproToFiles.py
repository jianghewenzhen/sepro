# -*- coding:utf-8 -*-

import base64
import json
import os
import tarfile


def jieyaOne(file_name):
    with open(file_name, 'rb') as f1:
        all_data = f1.read()  # 读出来数据为字节
        new_data = base64.b64decode(all_data)  # decode出来数据为字节
        json_data = json.loads(new_data)  # 转为字典
        proj_data = json_data['proj']  # 提取出来的数据位字符串
        new_data2 = base64.b64decode(proj_data)  # decode出来数据为字节
        with open('project.tar.gz', 'wb') as f2:
            f2.write(new_data2)


def un_tar():
    # untar zip file
    tar = tarfile.open('project.tar.gz')  # tar方式打开文件
    names = tar.getnames()  # 获取里面的所有文件名
    if os.path.isdir('project'):  # 如文件已存在则跳过
        pass
    else:
        os.mkdir('project')  # 文件夹不存在则新建
    # 由于解压后是许多文件，预先建立同名文件夹
    for name in names:
        tar.extract(name, 'project')  # 压缩包里面的所有文件放在新建的文件夹中
    tar.close()
