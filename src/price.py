from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox

from src import query_seat, modify_price
from ui.ui_price import Ui_price


class PriceWindow(QWidget, Ui_price):
    def __init__(self, parent=None):
        super(PriceWindow, self).__init__()
        self.setupUi(self)

    def show_info(self, flight_id, flight_name, start, end):
        self.flight_id.setText(flight_id)
        self.flight_name.setText(flight_name)
        self.start.setText(start)
        self.end.setText(end)
        self.query_price(flight_id)

    def query_price(self, flight_id):
        msg, price, count = query_seat(flight_id, '经济舱')
        if msg == 'success':
            self.class1count.setText(str(count))
            if price:
                self.class1price.setText(str(price))
            else:
                self.class1price.setDisabled(True)
        else:
            QMessageBox.critical(self, "数据库错误", price, QMessageBox.Ok, QMessageBox.Ok)

        msg, price, count = query_seat(flight_id, '商务舱')
        if msg == 'success':
            self.class2count.setText(str(count))
            if price:
                self.class2price.setText(str(price))
            else:
                self.class2price.setDisabled(True)
        else:
            QMessageBox.critical(self, "数据库错误", price, QMessageBox.Ok, QMessageBox.Ok)

        msg, price, count = query_seat(flight_id, '头等舱')
        if msg == 'success':
            self.class3count.setText(str(count))
            if price:
                self.class3price.setText(str(price))
            else:
                self.class3price.setDisabled(True)
        else:
            QMessageBox.critical(self, "数据库错误", price, QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_modify_price_clicked(self):
        if self.class1count.text() > '0':
            msg = modify_price(self.flight_id.text(), '经济舱', float(self.class1price.text()))
            if msg != 'success':
                QMessageBox.critical(self, "数据库错误", msg, QMessageBox.Ok, QMessageBox.Ok)
                return

        if self.class2count.text() > '0':
            msg = modify_price(self.flight_id.text(), '商务舱', float(self.class2price.text()))
            if msg != 'success':
                QMessageBox.critical(self, "数据库错误", msg, QMessageBox.Ok, QMessageBox.Ok)
                return

        if self.class3count.text() > '0':
            msg = modify_price(self.flight_id.text(), '头等舱', float(self.class3price.text()))
            if msg != 'success':
                QMessageBox.critical(self, "数据库错误", msg, QMessageBox.Ok, QMessageBox.Ok)
                return

        QMessageBox.information(self, "成功", '航班票价修改成功', QMessageBox.Ok, QMessageBox.Ok)
