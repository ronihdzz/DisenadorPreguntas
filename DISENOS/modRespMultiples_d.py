# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespMultiples_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(888, 442)
        self.listWidget_panelVersion = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelVersion.setGeometry(QtCore.QRect(10, 60, 871, 381))
        self.listWidget_panelVersion.setToolTipDuration(0)
        self.listWidget_panelVersion.setStyleSheet("padding:0px;\n"
"border: 1px solid red;\n"
"")
        self.listWidget_panelVersion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelVersion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelVersion.setObjectName("listWidget_panelVersion")
        self.btn_pregImag0 = QtWidgets.QPushButton(Form)
        self.btn_pregImag0.setGeometry(QtCore.QRect(690, 0, 51, 51))
        self.btn_pregImag0.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_noImagen.png);")
        self.btn_pregImag0.setText("")
        self.btn_pregImag0.setObjectName("btn_pregImag0")
        self.btn_pregImag50 = QtWidgets.QPushButton(Form)
        self.btn_pregImag50.setGeometry(QtCore.QRect(760, 0, 51, 51))
        self.btn_pregImag50.setStyleSheet("border-image: url(:/alinear/ICONOS/iconImage.png);")
        self.btn_pregImag50.setText("")
        self.btn_pregImag50.setObjectName("btn_pregImag50")
        self.btn_pregImag100 = QtWidgets.QPushButton(Form)
        self.btn_pregImag100.setGeometry(QtCore.QRect(820, 0, 51, 51))
        self.btn_pregImag100.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_galeri.png);")
        self.btn_pregImag100.setText("")
        self.btn_pregImag100.setObjectName("btn_pregImag100")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(360, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.timeEdit.setFont(font)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setCurrentSectionIndex(0)
        self.timeEdit.setObjectName("timeEdit")

        self.retranslateUi(Form)
        self.listWidget_panelVersion.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeEdit.setDisplayFormat(_translate("Form", "mm:ss"))

import imagenes_rc
