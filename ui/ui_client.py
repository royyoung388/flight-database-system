# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_client(object):
    def setupUi(self, client):
        client.setObjectName("client")
        client.resize(248, 209)
        self.gridLayout_2 = QtWidgets.QGridLayout(client)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.id = QtWidgets.QLineEdit(client)
        self.id.setObjectName("id")
        self.gridLayout_2.addWidget(self.id, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(client)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(client)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(client)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.name = QtWidgets.QLineEdit(client)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 2, 1, 1)
        self.phone = QtWidgets.QLineEdit(client)
        self.phone.setObjectName("phone")
        self.gridLayout_2.addWidget(self.phone, 2, 2, 1, 1)
        self.add_client = QtWidgets.QPushButton(client)
        self.add_client.setObjectName("add_client")
        self.gridLayout_2.addWidget(self.add_client, 3, 0, 1, 3)

        self.retranslateUi(client)
        QtCore.QMetaObject.connectSlotsByName(client)

    def retranslateUi(self, client):
        _translate = QtCore.QCoreApplication.translate
        client.setWindowTitle(_translate("client", "Form"))
        self.label_2.setText(_translate("client", "身份证号"))
        self.label.setText(_translate("client", "姓名"))
        self.label_3.setText(_translate("client", "电话"))
        self.add_client.setText(_translate("client", "添加客户"))
