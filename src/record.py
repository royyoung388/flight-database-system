from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox

from src import query_client, query_record
from ui.ui_record import Ui_record


class RecordWindow(QWidget, Ui_record):
    def __init__(self, parent=None):
        super(RecordWindow, self).__init__()
        self.setupUi(self)

    def query(self, client_id):
        print(client_id)

        msg, values = query_client(client_id)
        if msg != 'success':
            QMessageBox.warning(self, "数据库错误", values, QMessageBox.Ok, QMessageBox.Ok)
        elif values:
            self.id.setText(values[0])
            self.name.setText(values[1])
            self.phone.setText(values[2])

        self.table.setModel(query_record(client_id))
