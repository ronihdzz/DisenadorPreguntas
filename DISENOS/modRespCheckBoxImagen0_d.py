# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespCheckBoxImagen0_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(894, 521)
        self.txtEdit_preg = QtWidgets.QTextEdit(Form)
        self.txtEdit_preg.setGeometry(QtCore.QRect(10, 70, 301, 341))
        self.txtEdit_preg.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_preg.setObjectName("txtEdit_preg")
        self.scroll_barra = QtWidgets.QScrollArea(Form)
        self.scroll_barra.setGeometry(QtCore.QRect(330, 30, 551, 471))
        self.scroll_barra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setObjectName("scroll_barra")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 535, 469))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_barra.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import imagenes_rc
