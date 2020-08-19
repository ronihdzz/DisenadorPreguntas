# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespMultiplesImagen75_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(897, 522)
        self.btn_pregCen = QtWidgets.QPushButton(Form)
        self.btn_pregCen.setGeometry(QtCore.QRect(160, 380, 21, 21))
        self.btn_pregCen.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_centrar.png);")
        self.btn_pregCen.setText("")
        self.btn_pregCen.setProperty("id", 0)
        self.btn_pregCen.setObjectName("btn_pregCen")
        self.btn_respIzq = QtWidgets.QPushButton(Form)
        self.btn_respIzq.setGeometry(QtCore.QRect(725, 10, 21, 21))
        self.btn_respIzq.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_izquierda.png);")
        self.btn_respIzq.setText("")
        self.btn_respIzq.setObjectName("btn_respIzq")
        self.btn_imageRespA = QtWidgets.QPushButton(Form)
        self.btn_imageRespA.setGeometry(QtCore.QRect(350, 70, 51, 41))
        self.btn_imageRespA.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_subir.png);")
        self.btn_imageRespA.setText("")
        self.btn_imageRespA.setObjectName("btn_imageRespA")
        self.btn_imageRespB = QtWidgets.QPushButton(Form)
        self.btn_imageRespB.setGeometry(QtCore.QRect(340, 320, 51, 41))
        self.btn_imageRespB.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_subir.png);")
        self.btn_imageRespB.setText("")
        self.btn_imageRespB.setObjectName("btn_imageRespB")
        self.dSpin_pregTam = QtWidgets.QDoubleSpinBox(Form)
        self.dSpin_pregTam.setGeometry(QtCore.QRect(220, 380, 69, 26))
        self.dSpin_pregTam.setObjectName("dSpin_pregTam")
        self.btn_respCen = QtWidgets.QPushButton(Form)
        self.btn_respCen.setGeometry(QtCore.QRect(760, 10, 21, 21))
        self.btn_respCen.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_centrar.png);")
        self.btn_respCen.setText("")
        self.btn_respCen.setObjectName("btn_respCen")
        self.btn_respB = QtWidgets.QPushButton(Form)
        self.btn_respB.setGeometry(QtCore.QRect(310, 370, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_respB.setFont(font)
        self.btn_respB.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 20px;\n"
"border: 1px solid #555;")
        self.btn_respB.setObjectName("btn_respB")
        self.dSpin_respTam = QtWidgets.QDoubleSpinBox(Form)
        self.dSpin_respTam.setGeometry(QtCore.QRect(820, 10, 69, 26))
        self.dSpin_respTam.setObjectName("dSpin_respTam")
        self.btn_respDer = QtWidgets.QPushButton(Form)
        self.btn_respDer.setGeometry(QtCore.QRect(790, 10, 21, 21))
        self.btn_respDer.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_derecho.png);")
        self.btn_respDer.setText("")
        self.btn_respDer.setObjectName("btn_respDer")
        self.txtEdit_preg = QtWidgets.QTextEdit(Form)
        self.txtEdit_preg.setGeometry(QtCore.QRect(10, 70, 291, 301))
        self.txtEdit_preg.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_preg.setObjectName("txtEdit_preg")
        self.btn_respA = QtWidgets.QPushButton(Form)
        self.btn_respA.setGeometry(QtCore.QRect(320, 120, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_respA.setFont(font)
        self.btn_respA.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 20px;\n"
"border: 1px solid #555;")
        self.btn_respA.setObjectName("btn_respA")
        self.btn_respD = QtWidgets.QPushButton(Form)
        self.btn_respD.setGeometry(QtCore.QRect(600, 370, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_respD.setFont(font)
        self.btn_respD.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 20px;\n"
"border: 1px solid #555;")
        self.btn_respD.setObjectName("btn_respD")
        self.btn_pregIzq = QtWidgets.QPushButton(Form)
        self.btn_pregIzq.setGeometry(QtCore.QRect(130, 380, 21, 21))
        self.btn_pregIzq.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_izquierda.png);")
        self.btn_pregIzq.setText("")
        self.btn_pregIzq.setProperty("id", 1)
        self.btn_pregIzq.setObjectName("btn_pregIzq")
        self.btn_imageRespD = QtWidgets.QPushButton(Form)
        self.btn_imageRespD.setGeometry(QtCore.QRect(630, 320, 51, 41))
        self.btn_imageRespD.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_subir.png);")
        self.btn_imageRespD.setText("")
        self.btn_imageRespD.setObjectName("btn_imageRespD")
        self.btn_imageRespC = QtWidgets.QPushButton(Form)
        self.btn_imageRespC.setGeometry(QtCore.QRect(640, 80, 51, 41))
        self.btn_imageRespC.setStyleSheet("border-image: url(:/alinear/IMAGENES/imagen_subir.png);")
        self.btn_imageRespC.setText("")
        self.btn_imageRespC.setObjectName("btn_imageRespC")
        self.bel_imageRespA = QtWidgets.QLabel(Form)
        self.bel_imageRespA.setGeometry(QtCore.QRect(410, 40, 191, 181))
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
        self.btn_pregDer = QtWidgets.QPushButton(Form)
        self.btn_pregDer.setGeometry(QtCore.QRect(190, 380, 21, 21))
        self.btn_pregDer.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_derecho.png);")
        self.btn_pregDer.setText("")
        self.btn_pregDer.setProperty("id", 2)
        self.btn_pregDer.setObjectName("btn_pregDer")
        self.bel_imageRespC = QtWidgets.QLabel(Form)
        self.bel_imageRespC.setGeometry(QtCore.QRect(700, 40, 191, 181))
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
        self.btn_respC = QtWidgets.QPushButton(Form)
        self.btn_respC.setGeometry(QtCore.QRect(610, 130, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_respC.setFont(font)
        self.btn_respC.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 20px;\n"
"border: 1px solid #555;")
        self.btn_respC.setObjectName("btn_respC")
        self.bel_imageRespD = QtWidgets.QLabel(Form)
        self.bel_imageRespD.setGeometry(QtCore.QRect(690, 280, 191, 181))
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
        self.bel_imageRespB = QtWidgets.QLabel(Form)
        self.bel_imageRespB.setGeometry(QtCore.QRect(400, 280, 191, 181))
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
        self.txtEdit_respD = QtWidgets.QTextEdit(Form)
        self.txtEdit_respD.setGeometry(QtCore.QRect(620, 470, 261, 41))
        self.txtEdit_respD.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respD.setObjectName("txtEdit_respD")
        self.txtEdit_respB = QtWidgets.QTextEdit(Form)
        self.txtEdit_respB.setGeometry(QtCore.QRect(330, 470, 261, 41))
        self.txtEdit_respB.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respB.setObjectName("txtEdit_respB")
        self.txtEdit_respC = QtWidgets.QTextEdit(Form)
        self.txtEdit_respC.setGeometry(QtCore.QRect(630, 230, 261, 41))
        self.txtEdit_respC.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respC.setObjectName("txtEdit_respC")
        self.txtEdit_respA = QtWidgets.QTextEdit(Form)
        self.txtEdit_respA.setGeometry(QtCore.QRect(330, 230, 261, 41))
        self.txtEdit_respA.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respA.setObjectName("txtEdit_respA")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_respB.setText(_translate("Form", "B"))
        self.btn_respA.setText(_translate("Form", "A"))
        self.btn_respD.setText(_translate("Form", "D"))
        self.btn_respC.setText(_translate("Form", "C"))

import imagenes_rc
