# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizacionTodoCuestionario_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(998, 630)
        self.listWidget_panelPreguntas = QtWidgets.QStackedWidget(Dialog)
        self.listWidget_panelPreguntas.setGeometry(QtCore.QRect(0, 100, 911, 511))
        self.listWidget_panelPreguntas.setToolTipDuration(0)
        self.listWidget_panelPreguntas.setStyleSheet("")
        self.listWidget_panelPreguntas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelPreguntas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelPreguntas.setObjectName("listWidget_panelPreguntas")
        self.btn_hagamoslo = QtWidgets.QPushButton(Dialog)
        self.btn_hagamoslo.setGeometry(QtCore.QRect(270, 10, 451, 71))
        self.btn_hagamoslo.setObjectName("btn_hagamoslo")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(900, 60, 81, 21))
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
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(920, 160, 71, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 69, 369))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.btn_next = QtWidgets.QPushButton(Dialog)
        self.btn_next.setGeometry(QtCore.QRect(950, 20, 31, 31))
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
        self.btn_prev = QtWidgets.QPushButton(Dialog)
        self.btn_prev.setGeometry(QtCore.QRect(900, 20, 31, 31))
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

        self.retranslateUi(Dialog)
        self.listWidget_panelPreguntas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_hagamoslo.setText(_translate("Dialog", "CONFIRMAR QUE ES EL CUESTIONARIO QUE QUIERO "))
        self.bel_punteroPregunta.setText(_translate("Dialog", "10"))
        self.label_2.setText(_translate("Dialog", "/"))
        self.bel_noPreguntas.setText(_translate("Dialog", "105"))

import IMAG_rc
