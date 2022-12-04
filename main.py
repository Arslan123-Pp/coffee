import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffee_tb.ui', self)
        self.con = sqlite3.connect("coffee.db")
        self.cur = self.con.cursor()
        self.select_data()

    def select_data(self):
        res = self.cur.execute('SELECT * FROM coffees').fetchall()

        for i, row in enumerate(res):
            self.tw.setRowCount(
                self.tw.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tw.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())