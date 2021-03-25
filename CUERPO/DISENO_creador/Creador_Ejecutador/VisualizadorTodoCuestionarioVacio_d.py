# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizadorTodoCuestionarioVacio_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(912, 520)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(200, 30, 631, 101))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.bel_mensajeBienvenida = QtWidgets.QLabel(Form)
        self.bel_mensajeBienvenida.setGeometry(QtCore.QRect(210, 160, 581, 311))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.bel_mensajeBienvenida.setFont(font)
        self.bel_mensajeBienvenida.setStyleSheet("border: 2px solid black;\n"
"border-radius:14px;\n"
"")
        self.bel_mensajeBienvenida.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_mensajeBienvenida.setWordWrap(True)
        self.bel_mensajeBienvenida.setObjectName("bel_mensajeBienvenida")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Hola bienvenid@ "))
        self.bel_mensajeBienvenida.setText(_translate("Form", "Por favor, navega por el cuestionario para que corrobores acerca de si es el cuestionario que deseas"))

