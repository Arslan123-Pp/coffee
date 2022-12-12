import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


con = sqlite3.connect("data/coffee.db")
cur = con.cursor()


class MyWidget(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(716, 460)
        self.tw = QtWidgets.QTableWidget(Form)
        self.tw.setGeometry(QtCore.QRect(5, 0, 701, 401))
        self.tw.setObjectName("tw")
        self.tw.setColumnCount(7)
        self.tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw.setHorizontalHeaderItem(6, item)
        self.btn = QtWidgets.QPushButton(Form)
        self.btn.setGeometry(QtCore.QRect(0, 410, 171, 41))
        self.btn.setObjectName("btn")
        self.btnp = QtWidgets.QPushButton(Form)
        self.btnp.setGeometry(QtCore.QRect(190, 410, 131, 41))
        self.btnp.setObjectName("btnp")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tw.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.tw.horizontalHeaderItem(1)
        item.setText(_translate("Form", "name"))
        item = self.tw.horizontalHeaderItem(2)
        item.setText(_translate("Form", "degree"))
        item = self.tw.horizontalHeaderItem(3)
        item.setText(_translate("Form", "ground/in_grains"))
        item = self.tw.horizontalHeaderItem(4)
        item.setText(_translate("Form", "taste_descr"))
        item = self.tw.horizontalHeaderItem(5)
        item.setText(_translate("Form", "price"))
        item = self.tw.horizontalHeaderItem(6)
        item.setText(_translate("Form", "volume"))
        self.btn.setText(_translate("Form", "Добавить/изменить"))
        self.btnp.setText(_translate("Form", "Перезагрузить"))
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
        for i, row in enumerate(res):
            for j, elem in enumerate(row):
                self.tw.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def add(self):
        window = QtWidgets.QDialog()
        ui = ClssDialog()
        ui.setupUi(window)

        window.move(0, 0)
        window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        window.show()
        window.exec_()

    def closeEvent(self, event):
        con.close()


class ClssDialog(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 420)
        self.rstlbl = QtWidgets.QLabel(Form)
        self.rstlbl.setGeometry(QtCore.QRect(10, 660, 831, 16))
        self.rstlbl.setText("")
        self.rstlbl.setObjectName("rstlbl")
        self.lblwin = QtWidgets.QLabel(Form)
        self.lblwin.setGeometry(QtCore.QRect(80, 380, 371, 20))
        self.lblwin.setObjectName("lblwin")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 60, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 101, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 101, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(30, 290, 111, 16))
        self.label_6.setObjectName("label_6")
        self.text = QtWidgets.QTextEdit(Form)
        self.text.setGeometry(QtCore.QRect(160, 160, 411, 61))
        self.text.setObjectName("text")
        self.nameln = QtWidgets.QLineEdit(Form)
        self.nameln.setGeometry(QtCore.QRect(160, 10, 401, 21))
        self.nameln.setObjectName("nameln")
        self.cbd = QtWidgets.QComboBox(Form)
        self.cbd.setGeometry(QtCore.QRect(160, 40, 411, 26))
        self.cbd.setObjectName("cbd")
        self.cbd.addItem("")
        self.cbd.addItem("")
        self.cbd.addItem("")
        self.cbg = QtWidgets.QComboBox(Form)
        self.cbg.setGeometry(QtCore.QRect(160, 90, 411, 51))
        self.cbg.setObjectName("cbg")
        self.cbg.addItem("")
        self.cbg.addItem("")
        self.btnadd = QtWidgets.QPushButton(Form)
        self.btnadd.setGeometry(QtCore.QRect(300, 350, 281, 51))
        self.btnadd.setObjectName("btnadd")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(570, 10, 161, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(570, 40, 191, 16))
        self.label_8.setObjectName("label_8")
        self.btnok = QtWidgets.QPushButton(Form)
        self.btnok.setGeometry(QtCore.QRect(690, 60, 91, 61))
        self.btnok.setObjectName("btnok")
        self.price = QtWidgets.QLineEdit(Form)
        self.price.setGeometry(QtCore.QRect(160, 240, 411, 21))
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLineEdit(Form)
        self.volume.setGeometry(QtCore.QRect(160, 290, 411, 21))
        self.volume.setObjectName("volume")
        self.lnid = QtWidgets.QLineEdit(Form)
        self.lnid.setGeometry(QtCore.QRect(570, 70, 113, 21))
        self.lnid.setObjectName("lnid")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lblwin.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("Form", "name:"))
        self.label_2.setText(_translate("Form", "degree:"))
        self.label_3.setText(_translate("Form", "ground_in/grains:"))
        self.label_4.setText(_translate("Form", "taste_descr:"))
        self.label_5.setText(_translate("Form", "price: (Рубль)"))
        self.label_6.setText(_translate("Form", "volume: (Грамм)"))
        self.cbd.setItemText(0, _translate("Form", "Легкий"))
        self.cbd.setItemText(1, _translate("Form", "Средний"))
        self.cbd.setItemText(2, _translate("Form", "Сильный"))
        self.cbg.setItemText(0, _translate("Form", "Молотый"))
        self.cbg.setItemText(1, _translate("Form", "В зернах"))
        self.btnadd.setText(_translate("Form", "Добавить/изменить"))
        self.label_7.setText(_translate("Form", "Если вы хотите изменить"))
        self.label_8.setText(_translate("Form", "напишите номер айди строки"))
        self.btnok.setText(_translate("Form", "Ok"))
        self.btnadd.clicked.connect(self.closed)
        self.btnok.clicked.connect(self.run)

    def closed(self, Form):
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

        if name and txt and pr.isdigit() and vl.isdigit() and id_.isdigit():
            cur.execute(f"""UPDATE coffees
SET name = '{name}', degree = '{degree}', ground = '{g}', taste_descr = '{txt}',
price = '{pr}Р', volume = '{vl}г'
WHERE ID = {int(id_)}""")
            con.commit()

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
    window = QtWidgets.QMainWindow()
    ui = MyWidget()
    ui.setupUi(window)

    window.show()
    sys.exit(app.exec_())
