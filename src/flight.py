from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox

from src import *
from ui.ui_flight import Ui_flight


class FlightWindow(QWidget, Ui_flight):
    def __init__(self, parent=None):
        super(FlightWindow, self).__init__()
        self.setupUi(self)

    @pyqtSlot()
    def on_add_flight_clicked(self):
        id = self.id.text()
        name = self.name.text()
        start = self.start.text()
        end = self.end.text()
        class1count = int(self.class1count.text()) if self.class1count.text() else 0
        class1price = float(self.class1price.text()) if self.class1price.text() else 0.
        class2count = int(self.class2count.text()) if self.class2count.text() else 0
        class2price = float(self.class2price.text()) if self.class2price.text() else 0.
        class3count = int(self.class3count.text()) if self.class3count.text() else 0
        class3price = float(self.class3price.text()) if self.class3price.text() else 0.

        if not (id and name and start and end):
            QMessageBox.warning(self, "错误", "航班信息不能为空", QMessageBox.Ok, QMessageBox.Ok)
        else:
            if self.add(id, name, start, end, class1count, class1price, class2count, class2price, class3count,
                            class3price):
                QMessageBox.warning(self, "成功", "航班信息添加成功", QMessageBox.Ok, QMessageBox.Ok)
                self.hide()

    def add(self, id, name, start, end, class1count, class1price, class2count, class2price, class3count,
                   class3price):
        msg = create_flight(id, name, start, end)
        if msg != 'success':
            QMessageBox.warning(self, "数据库错误", msg, QMessageBox.Ok, QMessageBox.Ok)
            return False

        msg = create_seat(id, '经济舱', class1count, class1count, class1price)
        if msg != 'success':
            QMessageBox.warning(self, "数据库错误", msg, QMessageBox.Ok, QMessageBox.Ok)
            return False

        msg = create_seat(id, '商务舱', class2count, class2count, class2price)
        if msg != 'success':
            QMessageBox.warning(self, "数据库错误", msg, QMessageBox.Ok, QMessageBox.Ok)
            return False

        msg = create_seat(id, '头等舱', class3count, class3count, class3price)
        if msg != 'success':
            QMessageBox.warning(self, "数据库错误", msg, QMessageBox.Ok, QMessageBox.Ok)
            return False

        return True