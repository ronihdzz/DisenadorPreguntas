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
        Form.resize(915, 623)
        self.listWidget_panelVersion = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelVersion.setGeometry(QtCore.QRect(10, 60, 901, 541))
        self.listWidget_panelVersion.setToolTipDuration(0)
        self.listWidget_panelVersion.setStyleSheet("padding:0px;\n"
"border: 1px solid red;\n"
"")
        self.listWidget_panelVersion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelVersion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelVersion.setObjectName("listWidget_panelVersion")
        self.btn_pregImag0 = QtWidgets.QPushButton(Form)
        self.btn_pregImag0.setGeometry(QtCore.QRect(630, 0, 51, 51))
        self.btn_pregImag0.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_preg0.png);")
        self.btn_pregImag0.setText("")
        self.btn_pregImag0.setObjectName("btn_pregImag0")
        self.btn_pregImag50 = QtWidgets.QPushButton(Form)
        self.btn_pregImag50.setGeometry(QtCore.QRect(700, 0, 51, 51))
        self.btn_pregImag50.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_preg50.png);")
        self.btn_pregImag50.setText("")
        self.btn_pregImag50.setObjectName("btn_pregImag50")
        self.btn_pregImag75 = QtWidgets.QPushButton(Form)
        self.btn_pregImag75.setGeometry(QtCore.QRect(760, 0, 51, 51))
        self.btn_pregImag75.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_preg75.png);")
        self.btn_pregImag75.setText("")
        self.btn_pregImag75.setObjectName("btn_pregImag75")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(300, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.timeEdit.setFont(font)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setCurrentSectionIndex(0)
        self.timeEdit.setObjectName("timeEdit")
        self.btn_pregImag100 = QtWidgets.QPushButton(Form)
        self.btn_pregImag100.setGeometry(QtCore.QRect(830, 0, 51, 51))
        self.btn_pregImag100.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_preg100.png);")
        self.btn_pregImag100.setText("")
        self.btn_pregImag100.setObjectName("btn_pregImag100")
        self.btn_pregOR = QtWidgets.QPushButton(Form)
        self.btn_pregOR.setGeometry(QtCore.QRect(540, 0, 61, 51))
        self.btn_pregOR.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_or.png);")
        self.btn_pregOR.setText("")
        self.btn_pregOR.setObjectName("btn_pregOR")
        self.btn_pregAND = QtWidgets.QPushButton(Form)
        self.btn_pregAND.setGeometry(QtCore.QRect(440, 0, 91, 51))
        self.btn_pregAND.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_and.png);")
        self.btn_pregAND.setText("")
        self.btn_pregAND.setObjectName("btn_pregAND")

        self.retranslateUi(Form)
        self.listWidget_panelVersion.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.timeEdit.setDisplayFormat(_translate("Form", "mm:ss"))

import imagenes_rc
