# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InteractuadorCompartidos_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 270)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 441, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.rdBtn_borrar = QtWidgets.QRadioButton(Form)
        self.rdBtn_borrar.setGeometry(QtCore.QRect(360, 20, 91, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdBtn_borrar.setFont(font)
        self.rdBtn_borrar.setObjectName("rdBtn_borrar")
        self.rdBtn_descargar = QtWidgets.QRadioButton(Form)
        self.rdBtn_descargar.setGeometry(QtCore.QRect(230, 20, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rdBtn_descargar.setFont(font)
        self.rdBtn_descargar.setObjectName("rdBtn_descargar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre del cuestionario"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Data time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "?"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "LLave"))
        self.rdBtn_borrar.setText(_translate("Form", "Borrarlo"))
        self.rdBtn_descargar.setText(_translate("Form", "Descargarlo"))

