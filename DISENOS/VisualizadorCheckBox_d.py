# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizadorCheckBox_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(913, 509)
        self.listWidget_panelVersion = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelVersion.setGeometry(QtCore.QRect(10, 10, 331, 491))
        self.listWidget_panelVersion.setToolTipDuration(0)
        self.listWidget_panelVersion.setStyleSheet("")
        self.listWidget_panelVersion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelVersion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelVersion.setObjectName("listWidget_panelVersion")
        self.scroll_barra = QtWidgets.QScrollArea(Form)
        self.scroll_barra.setGeometry(QtCore.QRect(350, 10, 551, 491))
        self.scroll_barra.setStyleSheet(" border: none;")
        self.scroll_barra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setObjectName("scroll_barra")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 537, 491))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_barra.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        self.listWidget_panelVersion.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import imagenes_rc
