import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog
import sqlite3


con = sqlite3.connect("coffee.db")
cur = con.cursor()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('coffee_tb.ui', self)
        self.select_data()

        self.btn.clicked.connect(self.add)
        self.btnp.clicked.connect(self.per)

    def select_data(self):
        res = cur.execute('SELECT * FROM coffees').fetchall()

        for i, row in enumerate(res):
            self.tw.setRowCount(
                self.tw.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tw.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def per(self):
        res = cur.execute('SELECT * FROM coffees').fetchall()
        self.tw.setRowCount(len(res))
        print(self.tw.rowCount())
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.tw.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def add(self):
        dialog = ClssDialog(self)
        dialog.exec_()

    def closeEvent(self, event):
        con.close()


class ClssDialog(QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.btnadd.clicked.connect(self.closed)
        self.btnok.clicked.connect(self.run)

    def closed(self):
        id_ = self.lnid.text()
        name = self.nameln.text()
        degree = self.cbd.currentText()
        g = self.cbg.currentText()
        txt = self.text.toPlainText()
        pr = self.price.text()
        vl = self.volume.text()
        if name and txt and pr.isdigit() and vl.isdigit() and not id_.isdigit():
            cur.execute(f"""INSERT INTO coffees(name,degree,ground,taste_descr,price,volume)
VALUES ('{name}','{degree}','{g}','{txt}','{pr}Р','{vl}г')""")
            con.commit()
            self.close()
        if name and txt and pr.isdigit() and vl.isdigit() and id_.isdigit():
            cur.execute(f"""UPDATE coffees
SET name = '{name}', degree = '{degree}', ground = '{g}', taste_descr = '{txt}',
price = '{pr}Р', volume = '{vl}г'
WHERE ID = {int(id_)}""")
            con.commit()
            self.close()

    def run(self):
        id_ = self.lnid.text()
        if id_.isdigit():
            res = cur.execute(f'SELECT * FROM coffees WHERE ID = {int(id_)}').fetchone()
            self.nameln.setText(res[1])
            self.cbd.setCurrentText(res[2])
            self.cbg.setCurrentText(res[3])
            self.text.setPlainText(res[4])
            self.price.setText(res[5][:-1])
            self.volume.setText(res[6][:-1])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
