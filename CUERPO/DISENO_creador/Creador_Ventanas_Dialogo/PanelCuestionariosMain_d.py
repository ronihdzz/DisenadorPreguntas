# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PanelCuestionariosMain_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(467, 284)
        self.btn_descargados = QtWidgets.QPushButton(Dialog)
        self.btn_descargados.setGeometry(QtCore.QRect(90, 10, 34, 32))
        self.btn_descargados.setStyleSheet("border-image: url(:/prefijoNuevo/IMAGENES_creador/icons8-downloads-folder-40.png);")
        self.btn_descargados.setText("")
        self.btn_descargados.setObjectName("btn_descargados")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(70, 40, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.btn_proceso = QtWidgets.QPushButton(Dialog)
        self.btn_proceso.setGeometry(QtCore.QRect(20, 10, 33, 35))
        self.btn_proceso.setStyleSheet("border-image: url(:/prefijoNuevo/IMAGENES_creador/icon_folder.png);")
        self.btn_proceso.setText("")
        self.btn_proceso.setObjectName("btn_proceso")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(0, 40, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.listWidget = QtWidgets.QStackedWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 451, 221))
        self.listWidget.setToolTipDuration(0)
        self.listWidget.setStyleSheet("")
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Dialog)
        self.listWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_12.setText(_translate("Dialog", "Descargados"))
        self.label_13.setText(_translate("Dialog", "En proceso"))

import IMAG_rc
