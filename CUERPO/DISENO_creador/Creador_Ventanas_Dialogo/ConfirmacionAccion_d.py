# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConfirmacionAccion_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 326)
        self.lineEdit_firma = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_firma.setGeometry(QtCore.QRect(100, 240, 221, 31))
        self.lineEdit_firma.setStyleSheet("border-radius:5px;\n"
"border : 1px solid black;\n"
"background : white;")
        self.lineEdit_firma.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_firma.setObjectName("lineEdit_firma")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 0, 101, 21))
        self.label.setObjectName("label")
        self.textEdit_indicaciones = QtWidgets.QTextEdit(Dialog)
        self.textEdit_indicaciones.setGeometry(QtCore.QRect(40, 30, 341, 101))
        self.textEdit_indicaciones.setStyleSheet("border-radius:10px;\n"
"border : 2px solid black;\n"
"background : white;")
        self.textEdit_indicaciones.setObjectName("textEdit_indicaciones")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 140, 161, 21))
        self.label_2.setObjectName("label_2")
        self.lineEdit_wordRepetir = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_wordRepetir.setGeometry(QtCore.QRect(100, 170, 221, 31))
        self.lineEdit_wordRepetir.setStyleSheet("border-radius:5px;\n"
"border : 1px solid black;\n"
"background : white;")
        self.lineEdit_wordRepetir.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_wordRepetir.setObjectName("lineEdit_wordRepetir")
        self.btn_aceptar = QtWidgets.QPushButton(Dialog)
        self.btn_aceptar.setGeometry(QtCore.QRect(140, 280, 141, 41))
        self.btn_aceptar.setObjectName("btn_aceptar")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 210, 211, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Confirmacion accion"))
        self.label.setText(_translate("Dialog", "Indicaciones:"))
        self.label_2.setText(_translate("Dialog", "Frase de confirmacion:"))
        self.btn_aceptar.setText(_translate("Dialog", "Aceptar"))
        self.label_3.setText(_translate("Dialog", "Repetir frase de confirmacion:"))

