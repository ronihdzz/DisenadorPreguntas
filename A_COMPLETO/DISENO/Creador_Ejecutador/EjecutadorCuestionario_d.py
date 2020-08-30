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
        Form.resize(998, 638)
        self.listWidget_panelPreguntas = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelPreguntas.setGeometry(QtCore.QRect(50, 90, 911, 511))
        self.listWidget_panelPreguntas.setToolTipDuration(0)
        self.listWidget_panelPreguntas.setStyleSheet("")
        self.listWidget_panelPreguntas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelPreguntas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelPreguntas.setObjectName("listWidget_panelPreguntas")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(270, 10, 451, 71))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 449, 69))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.btn_next = QtWidgets.QPushButton(Form)
        self.btn_next.setGeometry(QtCore.QRect(880, 600, 31, 31))
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
        self.btn_prev = QtWidgets.QPushButton(Form)
        self.btn_prev.setGeometry(QtCore.QRect(830, 600, 31, 31))
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(740, 600, 81, 21))
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
        self.btn_terminar = QtWidgets.QPushButton(Form)
        self.btn_terminar.setGeometry(QtCore.QRect(820, 30, 101, 41))
        self.btn_terminar.setObjectName("btn_terminar")
        self.btn_respondioEl = QtWidgets.QPushButton(Form)
        self.btn_respondioEl.setGeometry(QtCore.QRect(190, 30, 41, 41))
        self.btn_respondioEl.setStyleSheet("border-image: url(:/CreadorPreguntas/IMAGENES/icon_yoNoDije.png);")
        self.btn_respondioEl.setText("")
        self.btn_respondioEl.setObjectName("btn_respondioEl")
        self.bel_respondioYo = QtWidgets.QLabel(Form)
        self.bel_respondioYo.setGeometry(QtCore.QRect(110, 10, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bel_respondioYo.setFont(font)
        self.bel_respondioYo.setObjectName("bel_respondioYo")
        self.btn_respondioYo = QtWidgets.QPushButton(Form)
        self.btn_respondioYo.setGeometry(QtCore.QRect(120, 30, 41, 41))
        self.btn_respondioYo.setStyleSheet("border-image: url(:/CreadorPreguntas/IMAGENES/icon_yoDije.png);")
        self.btn_respondioYo.setText("")
        self.btn_respondioYo.setObjectName("btn_respondioYo")
        self.bel_califFinal = QtWidgets.QLabel(Form)
        self.bel_califFinal.setGeometry(QtCore.QRect(780, 0, 181, 31))
        self.bel_califFinal.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_califFinal.setObjectName("bel_califFinal")
        self.bel_respondioEl = QtWidgets.QLabel(Form)
        self.bel_respondioEl.setGeometry(QtCore.QRect(180, 10, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.bel_respondioEl.setFont(font)
        self.bel_respondioEl.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_respondioEl.setObjectName("bel_respondioEl")
        self.bel_estadoPregunta = QtWidgets.QLabel(Form)
        self.bel_estadoPregunta.setGeometry(QtCore.QRect(870, 70, 121, 91))
        self.bel_estadoPregunta.setStyleSheet("")
        self.bel_estadoPregunta.setText("")
        self.bel_estadoPregunta.setObjectName("bel_estadoPregunta")

        self.retranslateUi(Form)
        self.listWidget_panelPreguntas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bel_punteroPregunta.setText(_translate("Form", "10"))
        self.label_2.setText(_translate("Form", "/"))
        self.bel_noPreguntas.setText(_translate("Form", "105"))
        self.btn_terminar.setText(_translate("Form", "Terminar"))
        self.bel_respondioYo.setText(_translate("Form", "Yo respondi"))
        self.bel_califFinal.setText(_translate("Form", "Calificacion final"))
        self.bel_respondioEl.setText(_translate("Form", "Lo que es"))

import IMAG_rc
