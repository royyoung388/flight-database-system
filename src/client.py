from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox

from src import create_client
from ui.ui_client import Ui_client


class ClientWindow(QWidget, Ui_client):
    def __init__(self, parent=None):
        super(ClientWindow, self).__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_add_client_clicked(self):
        id = self.id.text()
        name = self.name.text()
        phone = self.phone.text()

        if not (id and name and phone):
            QMessageBox.warning(self, "错误", "客户信息不能为空", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if create_client(name, id, phone):
                QMessageBox.warning(self, "成功", "客户信息添加成功", QMessageBox.Ok, QMessageBox.Ok)
                self.hide()
