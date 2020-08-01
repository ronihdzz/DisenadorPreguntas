# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creadorPreguntasMain_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(974, 451)
        self.scroll_barra = QtWidgets.QScrollArea(Form)
        self.scroll_barra.setGeometry(QtCore.QRect(10, 10, 81, 431))
        self.scroll_barra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setObjectName("scroll_barra")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 65, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_barra.setWidget(self.scrollAreaWidgetContents)
        self.btn_mas = QtWidgets.QPushButton(Form)
        self.btn_mas.setGeometry(QtCore.QRect(680, 10, 89, 41))
        self.btn_mas.setObjectName("btn_mas")
        self.btn_borrar = QtWidgets.QPushButton(Form)
        self.btn_borrar.setGeometry(QtCore.QRect(880, 10, 89, 41))
        self.btn_borrar.setObjectName("btn_borrar")
        self.btn_ver = QtWidgets.QPushButton(Form)
        self.btn_ver.setGeometry(QtCore.QRect(780, 10, 89, 41))
        self.btn_ver.setObjectName("btn_ver")
        self.listWidget_panelPreguntas = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelPreguntas.setGeometry(QtCore.QRect(100, 60, 861, 381))
        self.listWidget_panelPreguntas.setToolTipDuration(0)
        self.listWidget_panelPreguntas.setStyleSheet("padding:0px;\n"
"\n"
"\n"
"")
        self.listWidget_panelPreguntas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelPreguntas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelPreguntas.setObjectName("listWidget_panelPreguntas")

        self.retranslateUi(Form)
        self.listWidget_panelPreguntas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_mas.setText(_translate("Form", "MAS"))
        self.btn_borrar.setText(_translate("Form", "BORRAR"))
        self.btn_ver.setText(_translate("Form", "VER"))

