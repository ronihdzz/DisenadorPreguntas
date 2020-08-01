# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menuTipoPreguntas_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(304, 192)
        self.scroll_visorTipoPreguntas = QtWidgets.QScrollArea(Dialog)
        self.scroll_visorTipoPreguntas.setGeometry(QtCore.QRect(10, 80, 281, 101))
        self.scroll_visorTipoPreguntas.setWidgetResizable(True)
        self.scroll_visorTipoPreguntas.setObjectName("scroll_visorTipoPreguntas")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 279, 99))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_visorTipoPreguntas.setWidget(self.scrollAreaWidgetContents)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Tipo preguntas:"))

