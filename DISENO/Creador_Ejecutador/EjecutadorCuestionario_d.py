# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EjecutadorCuestionario_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1036, 584)
        self.scroll_barra = QtWidgets.QScrollArea(Form)
        self.scroll_barra.setGeometry(QtCore.QRect(10, 100, 91, 431))
        self.scroll_barra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setObjectName("scroll_barra")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 75, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_barra.setWidget(self.scrollAreaWidgetContents)
        self.listWidget_panelPreguntas = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelPreguntas.setGeometry(QtCore.QRect(110, 80, 911, 501))
        self.listWidget_panelPreguntas.setToolTipDuration(0)
        self.listWidget_panelPreguntas.setStyleSheet("")
        self.listWidget_panelPreguntas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelPreguntas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelPreguntas.setObjectName("listWidget_panelPreguntas")
        self.lcdNum_timePregunta = QtWidgets.QLCDNumber(Form)
        self.lcdNum_timePregunta.setGeometry(QtCore.QRect(460, 10, 121, 31))
        self.lcdNum_timePregunta.setObjectName("lcdNum_timePregunta")
        self.btn_next = QtWidgets.QPushButton(Form)
        self.btn_next.setGeometry(QtCore.QRect(960, 10, 31, 31))
        self.btn_next.setStyleSheet("QPushButton {\n"
"border-image: url(:/CreadorPreguntas/IMAGENES/imagen5_nextE.png);\n"
"  }\n"
"QPushButton:hover {\n"
"border-image: url(:/CreadorPreguntas/IMAGENES/imagen4_nextD.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/CreadorPreguntas/IMAGENES/imagen5_nextE.png);\n"
"}\n"
"")
        self.btn_next.setText("")
        self.btn_next.setObjectName("btn_next")
        self.bel_estadoRespuesta = QtWidgets.QLabel(Form)
        self.bel_estadoRespuesta.setGeometry(QtCore.QRect(20, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bel_estadoRespuesta.setFont(font)
        self.bel_estadoRespuesta.setText("")
        self.bel_estadoRespuesta.setObjectName("bel_estadoRespuesta")
        self.btn_prev = QtWidgets.QPushButton(Form)
        self.btn_prev.setGeometry(QtCore.QRect(910, 10, 31, 31))
        self.btn_prev.setStyleSheet("QPushButton {\n"
"border-image: url(:/CreadorPreguntas/IMAGENES/imagen5_prevE.png);\n"
"  }\n"
"QPushButton:hover {\n"
"border-image: url(:/CreadorPreguntas/IMAGENES/imagen4_prevD .png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/CreadorPreguntas/IMAGENES/imagen5_prevE.png);\n"
"}\n"
"")
        self.btn_prev.setText("")
        self.btn_prev.setObjectName("btn_prev")
        self.proBar_avance = QtWidgets.QProgressBar(Form)
        self.proBar_avance.setGeometry(QtCore.QRect(870, 50, 141, 31))
        self.proBar_avance.setStyleSheet("QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    padding:2px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 20px;\n"
"    padding:2px;\n"
"\n"
"}")
        self.proBar_avance.setProperty("value", 0)
        self.proBar_avance.setAlignment(QtCore.Qt.AlignCenter)
        self.proBar_avance.setObjectName("proBar_avance")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(480, 40, 81, 21))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bel_punteroPregunta = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bel_punteroPregunta.setFont(font)
        self.bel_punteroPregunta.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_punteroPregunta.setObjectName("bel_punteroPregunta")
        self.horizontalLayout.addWidget(self.bel_punteroPregunta)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(15, 16777215))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bel_noPreguntas = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bel_noPreguntas.setFont(font)
        self.bel_noPreguntas.setStyleSheet("")
        self.bel_noPreguntas.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_noPreguntas.setObjectName("bel_noPreguntas")
        self.horizontalLayout.addWidget(self.bel_noPreguntas)

        self.retranslateUi(Form)
        self.listWidget_panelPreguntas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bel_punteroPregunta.setText(_translate("Form", "10"))
        self.label_2.setText(_translate("Form", "/"))
        self.bel_noPreguntas.setText(_translate("Form", "105"))

import IMAG_rc
