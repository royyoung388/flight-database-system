# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'record.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_record(object):
    def setupUi(self, record):
        record.setObjectName("record")
        record.resize(711, 535)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(record)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 8, -1, 8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(record)
        self.label.setMinimumSize(QtCore.QSize(112, 12))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name = QtWidgets.QLabel(record)
        self.name.setText("")
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)
        self.label_2 = QtWidgets.QLabel(record)
        self.label_2.setMinimumSize(QtCore.QSize(112, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.id = QtWidgets.QLabel(record)
        self.id.setText("")
        self.id.setObjectName("id")
        self.horizontalLayout.addWidget(self.id)
        self.label_5 = QtWidgets.QLabel(record)
        self.label_5.setMinimumSize(QtCore.QSize(112, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.phone = QtWidgets.QLabel(record)
        self.phone.setText("")
        self.phone.setObjectName("phone")
        self.horizontalLayout.addWidget(self.phone)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.table = QtWidgets.QTableView(record)
        self.table.setObjectName("table")
        self.verticalLayout_2.addWidget(self.table)

        self.retranslateUi(record)
        QtCore.QMetaObject.connectSlotsByName(record)

    def retranslateUi(self, record):
        _translate = QtCore.QCoreApplication.translate
        record.setWindowTitle(_translate("record", "Form"))
        self.label.setText(_translate("record", "姓名："))
        self.label_2.setText(_translate("record", "证件号码："))
        self.label_5.setText(_translate("record", "电话："))
