# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespMultiplesImagen100_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(848, 374)
        self.btn_respA = QtWidgets.QPushButton(Form)
        self.btn_respA.setGeometry(QtCore.QRect(270, 70, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_respA.setFont(font)
        self.btn_respA.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 20px;\n"
"border: 1px solid #555;")
        self.btn_respA.setObjectName("btn_respA")
        self.btn_respB = QtWidgets.QPushButton(Form)
        self.btn_respB.setGeometry(QtCore.QRect(560, 70, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_respB.setFont(font)
        self.btn_respB.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 20px;\n"
"border: 1px solid #555;")
        self.btn_respB.setObjectName("btn_respB")
        self.txtEdit_preg = QtWidgets.QTextEdit(Form)
        self.txtEdit_preg.setGeometry(QtCore.QRect(10, 280, 251, 81))
        self.txtEdit_preg.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_preg.setObjectName("txtEdit_preg")
        self.btn_respD = QtWidgets.QPushButton(Form)
        self.btn_respD.setGeometry(QtCore.QRect(560, 250, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_respD.setFont(font)
        self.btn_respD.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 20px;\n"
"border: 1px solid #555;")
        self.btn_respD.setObjectName("btn_respD")
        self.btn_respC = QtWidgets.QPushButton(Form)
        self.btn_respC.setGeometry(QtCore.QRect(270, 250, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_respC.setFont(font)
        self.btn_respC.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 20px;\n"
"border: 1px solid #555;")
        self.btn_respC.setObjectName("btn_respC")
        self.bel_pregImage = QtWidgets.QLabel(Form)
        self.bel_pregImage.setGeometry(QtCore.QRect(10, 10, 251, 211))
        self.bel_pregImage.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.bel_pregImage.setText("")
        self.bel_pregImage.setObjectName("bel_pregImage")
        self.btn_imageRespA = QtWidgets.QPushButton(Form)
        self.btn_imageRespA.setGeometry(QtCore.QRect(300, 20, 51, 41))
        self.btn_imageRespA.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_subir.png);")
        self.btn_imageRespA.setText("")
        self.btn_imageRespA.setObjectName("btn_imageRespA")
        self.btn_imageRespC = QtWidgets.QPushButton(Form)
        self.btn_imageRespC.setGeometry(QtCore.QRect(300, 200, 51, 41))
        self.btn_imageRespC.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_subir.png);")
        self.btn_imageRespC.setText("")
        self.btn_imageRespC.setObjectName("btn_imageRespC")
        self.btn_imageRespB = QtWidgets.QPushButton(Form)
        self.btn_imageRespB.setGeometry(QtCore.QRect(590, 20, 51, 41))
        self.btn_imageRespB.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_subir.png);")
        self.btn_imageRespB.setText("")
        self.btn_imageRespB.setObjectName("btn_imageRespB")
        self.btn_imageRespD = QtWidgets.QPushButton(Form)
        self.btn_imageRespD.setGeometry(QtCore.QRect(590, 200, 51, 41))
        self.btn_imageRespD.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_subir.png);")
        self.btn_imageRespD.setText("")
        self.btn_imageRespD.setObjectName("btn_imageRespD")
        self.bel_imageRespA = QtWidgets.QLabel(Form)
        self.bel_imageRespA.setGeometry(QtCore.QRect(360, 20, 191, 151))
        self.bel_imageRespA.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.bel_imageRespA.setText("")
        self.bel_imageRespA.setObjectName("bel_imageRespA")
        self.bel_imageRespC = QtWidgets.QLabel(Form)
        self.bel_imageRespC.setGeometry(QtCore.QRect(360, 190, 191, 151))
        self.bel_imageRespC.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.bel_imageRespC.setText("")
        self.bel_imageRespC.setObjectName("bel_imageRespC")
        self.bel_imageRespB = QtWidgets.QLabel(Form)
        self.bel_imageRespB.setGeometry(QtCore.QRect(650, 20, 191, 151))
        self.bel_imageRespB.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.bel_imageRespB.setText("")
        self.bel_imageRespB.setObjectName("bel_imageRespB")
        self.bel_imageRespD = QtWidgets.QLabel(Form)
        self.bel_imageRespD.setGeometry(QtCore.QRect(650, 190, 191, 151))
        self.bel_imageRespD.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.bel_imageRespD.setText("")
        self.bel_imageRespD.setObjectName("bel_imageRespD")
        self.btn_pregImage = QtWidgets.QPushButton(Form)
        self.btn_pregImage.setGeometry(QtCore.QRect(30, 220, 51, 51))
        self.btn_pregImage.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_carga.png);")
        self.btn_pregImage.setText("")
        self.btn_pregImage.setObjectName("btn_pregImage")
        self.btn_pregIzq = QtWidgets.QPushButton(Form)
        self.btn_pregIzq.setGeometry(QtCore.QRect(100, 240, 21, 21))
        self.btn_pregIzq.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_izquierda.png);")
        self.btn_pregIzq.setText("")
        self.btn_pregIzq.setProperty("id", 1)
        self.btn_pregIzq.setObjectName("btn_pregIzq")
        self.btn_pregCen = QtWidgets.QPushButton(Form)
        self.btn_pregCen.setGeometry(QtCore.QRect(130, 240, 21, 21))
        self.btn_pregCen.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_centrar.png);")
        self.btn_pregCen.setText("")
        self.btn_pregCen.setProperty("id", 0)
        self.btn_pregCen.setObjectName("btn_pregCen")
        self.dSpin_pregTam = QtWidgets.QDoubleSpinBox(Form)
        self.dSpin_pregTam.setGeometry(QtCore.QRect(190, 240, 69, 26))
        self.dSpin_pregTam.setObjectName("dSpin_pregTam")
        self.btn_pregDer = QtWidgets.QPushButton(Form)
        self.btn_pregDer.setGeometry(QtCore.QRect(160, 240, 21, 21))
        self.btn_pregDer.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_derecho.png);")
        self.btn_pregDer.setText("")
        self.btn_pregDer.setProperty("id", 2)
        self.btn_pregDer.setObjectName("btn_pregDer")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_respA.setText(_translate("Form", "A"))
        self.btn_respB.setText(_translate("Form", "B"))
        self.btn_respD.setText(_translate("Form", "D"))
        self.btn_respC.setText(_translate("Form", "C"))

import imagenes_rc
