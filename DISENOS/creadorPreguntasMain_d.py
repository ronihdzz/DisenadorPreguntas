# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creadorPreguntasMain_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1049, 564)
        self.scroll_barra = QtWidgets.QScrollArea(Form)
        self.scroll_barra.setGeometry(QtCore.QRect(10, 110, 81, 431))
        self.scroll_barra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setObjectName("scroll_barra")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 65, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_barra.setWidget(self.scrollAreaWidgetContents)
        self.listWidget_panelPreguntas = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelPreguntas.setGeometry(QtCore.QRect(100, 100, 941, 451))
        self.listWidget_panelPreguntas.setToolTipDuration(0)
        self.listWidget_panelPreguntas.setStyleSheet("padding:0px;\n"
"border: 1px solid red;\n"
"")
        self.listWidget_panelPreguntas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelPreguntas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelPreguntas.setObjectName("listWidget_panelPreguntas")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(970, 10, 71, 61))
        self.pushButton_5.setStyleSheet("border-image: url(:/alinear/IMAGENES/pregunta_delete.png);")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.btn_mas = QtWidgets.QPushButton(Form)
        self.btn_mas.setGeometry(QtCore.QRect(820, 10, 71, 61))
        self.btn_mas.setStyleSheet("border-image: url(:/alinear/IMAGENES/pregunta_add.png);")
        self.btn_mas.setText("")
        self.btn_mas.setObjectName("btn_mas")
        self.btn__ver = QtWidgets.QPushButton(Form)
        self.btn__ver.setGeometry(QtCore.QRect(890, 10, 71, 61))
        self.btn__ver.setStyleSheet("border-image: url(:/alinear/IMAGENES/pregunta_ver.png);")
        self.btn__ver.setText("")
        self.btn__ver.setObjectName("btn__ver")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(830, 70, 51, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(900, 70, 51, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(970, 70, 61, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(750, 70, 61, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.btn_guardar = QtWidgets.QPushButton(Form)
        self.btn_guardar.setGeometry(QtCore.QRect(750, 20, 61, 51))
        self.btn_guardar.setStyleSheet("border-image: url(:/alinear/IMAGENES/pregunta_guardar.png);")
        self.btn_guardar.setText("")
        self.btn_guardar.setObjectName("btn_guardar")

        self.retranslateUi(Form)
        self.listWidget_panelPreguntas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "mas"))
        self.label_5.setText(_translate("Form", "ver"))
        self.label_6.setText(_translate("Form", "eliminar"))
        self.label_7.setText(_translate("Form", "Guardar"))

import imagenes_rc
