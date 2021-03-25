# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestOriginales_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(467, 271)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 451, 191))
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
        self.btn_verCuestionarios = QtWidgets.QPushButton(Form)
        self.btn_verCuestionarios.setGeometry(QtCore.QRect(420, 10, 31, 31))
        self.btn_verCuestionarios.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/cargarB.png);\n"
"\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/cargar_A.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/cargarB.png);\n"
"}\n"
"")
        self.btn_verCuestionarios.setText("")
        self.btn_verCuestionarios.setObjectName("btn_verCuestionarios")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(410, 40, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.btn_campachenoTest = QtWidgets.QPushButton(Form)
        self.btn_campachenoTest.setGeometry(QtCore.QRect(340, 10, 31, 31))
        self.btn_campachenoTest.setStyleSheet("QPushButton {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/ramdonTest_1.png);\n"
" }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/ramdonTest_2.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/ramdonTest_1.png);\n"
"}\n"
"")
        self.btn_campachenoTest.setText("")
        self.btn_campachenoTest.setObjectName("btn_campachenoTest")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(320, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Mi califacion"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "?"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Nombre del cuestionario"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Fecha"))
        self.label_11.setText(_translate("Form", "Actualizar"))
        self.label_12.setText(_translate("Form", "Campechano"))

import IMAG_rc
