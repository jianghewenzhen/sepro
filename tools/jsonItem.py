from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt, QJsonDocument, QVariant, QJsonValue, QJsonParseError
from PyQt5.QtGui import QIcon, QBrush, QFont
class QJsonTreeItem(object):
    def __init__(self, parent=None):
        self.mParent = parent  # 父名
        self.mChilds = []  # 子列表
        self.mType = None
        self.mValue = ''  # 没有的数据不显示

    def appendChild(self, item):  # 增加子列表元素
        self.mChilds.append(item)

    def child(self, row: int):  # 转化成整型并返回
        return self.mChilds[row]

    def parent(self):  # 返回父名
        return self.mParent

    def childCount(self):  # 返回子列表长度
        return len(self.mChilds)

    def row(self):  #
        if self.mParent is not None:
            return self.mParent.mChilds.index(self)
        return 0

    def setKey(self, key:str):
        self.mKey = key
        # self.mKey = '"{}"'.format(key)

    def setValue(self, value:str):
       self.mValue = value

    def setType(self, type:QJsonValue.Type):
        self.mType = type

    def key(self):
        return self.mKey

    def value(self):
        if isinstance(self.mValue, str) and self.mValue != '':
            return '"{}"'.format(self.mValue)
        else:
            return self.mValue

    def type(self):
        return self.mType

    def load(self, value, parent=None):

        rootItem = QJsonTreeItem(parent)
        rootItem.setKey("root")
        jsonType = None

        try:
            value = value.toVariant()
            jsonType = value.type()
        except AttributeError:
            pass

        try:
            value = value.toObject()
            jsonType = value.type()

        except AttributeError:
            pass

        if isinstance(value, dict):
            # process the key/value pairs
            for key in value:
                v = value[key]
                child = self.load(v, rootItem)
                # child.setKey(key)
                child.setKey('"{}"'.format(key))
                try:
                    child.setType(v.type())
                except AttributeError:
                    child.setType(v.__class__)
                rootItem.appendChild(child)

        elif isinstance(value, list):
            # process the values in the list
            for i, v in enumerate(value):
                child = self.load(v, rootItem)
                child.setKey('{ %s }' % str(i))  # 额外增加了标识突出
                # child.setValue('')
                child.setType(v.__class__)
                rootItem.appendChild(child)

        else:
            # value is processed
            # print(value)
            rootItem.setValue(value)
            try:
                rootItem.setType(value.type())
                # print(value.type())
            except AttributeError:
                if jsonType is not None:
                    rootItem.setType(jsonType)
                else:
                    rootItem.setType(value.__class__)
                    # print(value.__class__)

        return rootItem