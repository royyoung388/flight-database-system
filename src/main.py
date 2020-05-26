import cgitb
import sys

from PyQt5 import QtSql, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from src import FlightWindow, create, query_flight, ClientWindow, RecordWindow, buy_ticket, is_ticket_empty, \
    AllClientWindow, PriceWindow
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.login()
        self.open()
        self.flight_window = FlightWindow()
        self.client_window = ClientWindow()
        self.record_window = RecordWindow()
        self.all_client_window = AllClientWindow()
        self.price_window = PriceWindow()

        self.table.set_buy(self.buy)
        self.table.set_price(self.price)

        self.on_query_flight_clicked()

    def open(self):
        # 添加一个sqlite数据库连接并打开
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('flight.db')
        if not db.open():
            QMessageBox.critical(self, "数据库错误", "无法打开sqlite数据库", QMessageBox.Ok, QMessageBox.Ok)
            quit(1)
        create()

    def price(self, row):
        flight_id = self.table.model().index(row, 0).data()
        flight_name = self.table.model().index(row, 1).data()
        start = self.table.model().index(row, 2).data()
        end = self.table.model().index(row, 3).data()

        self.price_window.show_info(flight_id, flight_name, start, end)
        self.price_window.show()

    def buy(self, row):
        client_id, action = QtWidgets.QInputDialog.getText(self, '证件号', '请输入证件号', QtWidgets.QLineEdit.Normal)
        if not client_id and action:
            QMessageBox.warning(self, "错误", "输入有误", QMessageBox.Ok, QMessageBox.Ok)
            return
        elif not action:
            return

        flight_id = self.table.model().index(row, 0).data()
        flight_name = self.table.model().index(row, 1).data()
        start = self.table.model().index(row, 2).data()
        end = self.table.model().index(row, 3).data()
        grade = self.table.model().index(row, 4).data()

        empty = is_ticket_empty(flight_id, flight_name)
        if empty == False:
            msg = buy_ticket(client_id, flight_id, flight_name, start, end, grade)
            if msg != 'success':
                QMessageBox.information(self, "数据库错误", msg, QMessageBox.Ok, QMessageBox.Ok)
            else:
                QMessageBox.about(self, "成功", "购买成功")
                self.record_window.query(client_id)
                self.record_window.show()
                self.on_query_flight_clicked()
        elif empty == True:
            QMessageBox.information(self, "错误", "该航班的舱位无剩余机票", QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "数据库错误", empty, QMessageBox.Ok, QMessageBox.Ok)

    @pyqtSlot()
    def on_query_flight_clicked(self):
        """
        查询航班按钮
        :return:
        """
        flight_id = self.flight_no.text()
        flight_name = self.flight_name.text()
        start = self.start.text()
        end = self.end.text()

        model = query_flight(flight_id, flight_name, start, end)
        self.table.setModel(model)

    @pyqtSlot()
    def on_add_flight_clicked(self):
        """
        添加航班信息
        :return:
        """
        self.flight_window.show()
        self.on_query_flight_clicked()

    @pyqtSlot()
    def on_add_client_clicked(self):
        """
        添加客户
        :return:
        """
        self.client_window.show()

    @pyqtSlot()
    def on_query_record_clicked(self):
        """
        查询订单
        :return:
        """
        client_id, action = QtWidgets.QInputDialog.getText(self, '证件号', '请输入证件号', QtWidgets.QLineEdit.Normal)
        if not client_id and action:
            QMessageBox.warning(self, "错误", "输入有误", QMessageBox.Ok, QMessageBox.Ok)
        elif action:
            self.record_window.query(client_id)
            self.record_window.show()

    @pyqtSlot()
    def on_query_client_clicked(self):
        """
        查询所有顾客
        :return:
        """
        self.all_client_window.query()
        self.all_client_window.show()


if __name__ == '__main__':
    cgitb.enable(format='text')
    app = QApplication(sys.argv)
    welcom = MainWindow(app)
    welcom.show()
    app.exec_()
    sys.exit(app.exec_())
