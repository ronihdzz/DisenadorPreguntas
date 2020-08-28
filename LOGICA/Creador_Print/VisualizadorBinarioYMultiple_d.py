# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizadorContenedor_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 511)
        self.listWidget_panelVersion = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelVersion.setGeometry(QtCore.QRect(0, 10, 901, 491))
        self.listWidget_panelVersion.setToolTipDuration(0)
        self.listWidget_panelVersion.setStyleSheet("")
        self.listWidget_panelVersion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelVersion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelVersion.setObjectName("listWidget_panelVersion")

        self.retranslateUi(Form)
        self.listWidget_panelVersion.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import imagenes_rc
