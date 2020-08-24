# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespMultiplesImagen50_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(899, 488)
        self.txtEdit_respA = QtWidgets.QTextEdit(Form)
        self.txtEdit_respA.setGeometry(QtCore.QRect(520, 10, 371, 101))
        self.txtEdit_respA.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respA.setObjectName("txtEdit_respA")
        self.txtEdit_preg = QtWidgets.QTextEdit(Form)
        self.txtEdit_preg.setGeometry(QtCore.QRect(20, 10, 441, 121))
        self.txtEdit_preg.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_preg.setObjectName("txtEdit_preg")
        self.bel_pregImage = QtWidgets.QLabel(Form)
        self.bel_pregImage.setGeometry(QtCore.QRect(20, 140, 441, 341))
        self.bel_pregImage.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.bel_pregImage.setText("")
        self.bel_pregImage.setObjectName("bel_pregImage")
        self.btn_respA = QtWidgets.QPushButton(Form)
        self.btn_respA.setGeometry(QtCore.QRect(470, 40, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respA.setFont(font)
        self.btn_respA.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respA.setObjectName("btn_respA")
        self.txtEdit_respB = QtWidgets.QTextEdit(Form)
        self.txtEdit_respB.setGeometry(QtCore.QRect(520, 130, 371, 101))
        self.txtEdit_respB.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respB.setObjectName("txtEdit_respB")
        self.txtEdit_respC = QtWidgets.QTextEdit(Form)
        self.txtEdit_respC.setGeometry(QtCore.QRect(520, 250, 371, 101))
        self.txtEdit_respC.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respC.setObjectName("txtEdit_respC")
        self.txtEdit_respD = QtWidgets.QTextEdit(Form)
        self.txtEdit_respD.setGeometry(QtCore.QRect(520, 370, 371, 101))
        self.txtEdit_respD.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respD.setObjectName("txtEdit_respD")
        self.btn_respB = QtWidgets.QPushButton(Form)
        self.btn_respB.setGeometry(QtCore.QRect(470, 160, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respB.setFont(font)
        self.btn_respB.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respB.setObjectName("btn_respB")
        self.btn_respC = QtWidgets.QPushButton(Form)
        self.btn_respC.setGeometry(QtCore.QRect(470, 280, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respC.setFont(font)
        self.btn_respC.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respC.setObjectName("btn_respC")
        self.btn_respD = QtWidgets.QPushButton(Form)
        self.btn_respD.setGeometry(QtCore.QRect(470, 400, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respD.setFont(font)
        self.btn_respD.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respD.setObjectName("btn_respD")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_respA.setText(_translate("Form", "A"))
        self.btn_respB.setText(_translate("Form", "B"))
        self.btn_respC.setText(_translate("Form", "C"))
        self.btn_respD.setText(_translate("Form", "D"))

import imagenes_rc
