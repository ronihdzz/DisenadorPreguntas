# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizadorPreguntas_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 559)
        self.listWidget_panelVersion = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelVersion.setGeometry(QtCore.QRect(0, 60, 901, 491))
        self.listWidget_panelVersion.setToolTipDuration(0)
        self.listWidget_panelVersion.setStyleSheet("")
        self.listWidget_panelVersion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelVersion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelVersion.setObjectName("listWidget_panelVersion")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(40, 50, 841, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lcdNum_timePregunta = QtWidgets.QLCDNumber(Form)
        self.lcdNum_timePregunta.setGeometry(QtCore.QRect(370, 10, 151, 41))
        self.lcdNum_timePregunta.setObjectName("lcdNum_timePregunta")
        self.bel_estadoRespuesta = QtWidgets.QLabel(Form)
        self.bel_estadoRespuesta.setGeometry(QtCore.QRect(50, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bel_estadoRespuesta.setFont(font)
        self.bel_estadoRespuesta.setText("")
        self.bel_estadoRespuesta.setObjectName("bel_estadoRespuesta")
        self.btn_next = QtWidgets.QPushButton(Form)
        self.btn_next.setGeometry(QtCore.QRect(860, 10, 31, 31))
        self.btn_next.setStyleSheet("QPushButton {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen5_nextE.png);  }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen4_nextD.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen5_nextE.png);\n"
"}\n"
"")
        self.btn_next.setText("")
        self.btn_next.setObjectName("btn_next")
        self.btn_prev = QtWidgets.QPushButton(Form)
        self.btn_prev.setGeometry(QtCore.QRect(810, 10, 31, 31))
        self.btn_prev.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen5_prevE.png);\n"
"  }\n"
"QPushButton:hover {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen4_prevD .png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen5_prevE.png);\n"
"}\n"
"")
        self.btn_prev.setText("")
        self.btn_prev.setObjectName("btn_prev")

        self.retranslateUi(Form)
        self.listWidget_panelVersion.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

import IMAG_rc
