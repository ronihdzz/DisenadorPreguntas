# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InteractuadorDescargas.ui'
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
        self.tableWidget.setGeometry(QtCore.QRect(20, 110, 431, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(40, 10, 181, 31))
        self.comboBox.setObjectName("comboBox")
        self.btn_verCuestionarios = QtWidgets.QPushButton(Form)
        self.btn_verCuestionarios.setGeometry(QtCore.QRect(260, 10, 31, 31))
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
        self.label_11.setGeometry(QtCore.QRect(250, 40, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.bel_autorCuestionarios = QtWidgets.QLabel(Form)
        self.bel_autorCuestionarios.setGeometry(QtCore.QRect(180, 70, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bel_autorCuestionarios.setFont(font)
        self.bel_autorCuestionarios.setStyleSheet("border-radius:5px;\n"
"border : 1px solid black;\n"
"background : white;")
        self.bel_autorCuestionarios.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_autorCuestionarios.setObjectName("bel_autorCuestionarios")

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
        self.label_11.setText(_translate("Form", "Cargar "))
        self.label.setText(_translate("Form", "Cuestionarios de:"))
        self.bel_autorCuestionarios.setText(_translate("Form", "Nadie"))

import IMAG_rc
