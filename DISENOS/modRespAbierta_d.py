# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespAbierta_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 558)
        self.listWidget_panelVersion = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelVersion.setGeometry(QtCore.QRect(10, 60, 451, 491))
        self.listWidget_panelVersion.setToolTipDuration(0)
        self.listWidget_panelVersion.setStyleSheet("")
        self.listWidget_panelVersion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelVersion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelVersion.setObjectName("listWidget_panelVersion")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(760, 0, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.btn_pregImag50 = QtWidgets.QPushButton(Form)
        self.btn_pregImag50.setGeometry(QtCore.QRect(180, 20, 31, 31))
        self.btn_pregImag50.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_preg50.png);")
        self.btn_pregImag50.setText("")
        self.btn_pregImag50.setObjectName("btn_pregImag50")
        self.timeEdit = QtWidgets.QTimeEdit(Form)
        self.timeEdit.setGeometry(QtCore.QRect(760, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.timeEdit.setFont(font)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.MinuteSection)
        self.timeEdit.setCurrentSectionIndex(0)
        self.timeEdit.setObjectName("timeEdit")
        self.btn_pregImag0 = QtWidgets.QPushButton(Form)
        self.btn_pregImag0.setGeometry(QtCore.QRect(120, 20, 31, 31))
        self.btn_pregImag0.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_preg0.png);")
        self.btn_pregImag0.setText("")
        self.btn_pregImag0.setObjectName("btn_pregImag0")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(550, 0, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.dSpin_pregTam = QtWidgets.QDoubleSpinBox(Form)
        self.dSpin_pregTam.setGeometry(QtCore.QRect(620, 20, 69, 26))
        self.dSpin_pregTam.setObjectName("dSpin_pregTam")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(120, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.btn_pregIzq = QtWidgets.QPushButton(Form)
        self.btn_pregIzq.setGeometry(QtCore.QRect(530, 20, 21, 21))
        self.btn_pregIzq.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_izquierda.png);")
        self.btn_pregIzq.setText("")
        self.btn_pregIzq.setProperty("id", 1)
        self.btn_pregIzq.setObjectName("btn_pregIzq")
        self.btn_pregCen = QtWidgets.QPushButton(Form)
        self.btn_pregCen.setGeometry(QtCore.QRect(560, 20, 21, 21))
        self.btn_pregCen.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_centrar.png);")
        self.btn_pregCen.setText("")
        self.btn_pregCen.setProperty("id", 0)
        self.btn_pregCen.setObjectName("btn_pregCen")
        self.btn_pregDer = QtWidgets.QPushButton(Form)
        self.btn_pregDer.setGeometry(QtCore.QRect(590, 20, 21, 21))
        self.btn_pregDer.setStyleSheet("border-image: url(:/alinear/IMAGENES/alinear_derecho.png);")
        self.btn_pregDer.setText("")
        self.btn_pregDer.setProperty("id", 2)
        self.btn_pregDer.setObjectName("btn_pregDer")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(40, 50, 841, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.btn_respString = QtWidgets.QPushButton(Form)
        self.btn_respString.setGeometry(QtCore.QRect(320, 20, 41, 31))
        self.btn_respString.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_respPalabra.png);")
        self.btn_respString.setText("")
        self.btn_respString.setObjectName("btn_respString")
        self.btn_respNumero = QtWidgets.QPushButton(Form)
        self.btn_respNumero.setGeometry(QtCore.QRect(380, 20, 41, 31))
        self.btn_respNumero.setStyleSheet("border-image: url(:/alinear/ICONOS/icon_respNumber.png);\n"
"")
        self.btn_respNumero.setText("")
        self.btn_respNumero.setObjectName("btn_respNumero")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(330, 0, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.lineEdit_respuesta = QtWidgets.QLineEdit(Form)
        self.lineEdit_respuesta.setGeometry(QtCore.QRect(470, 240, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_respuesta.setFont(font)
        self.lineEdit_respuesta.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_respuesta.setObjectName("lineEdit_respuesta")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(560, 160, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(580, 320, 261, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bel_noChars = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bel_noChars.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_noChars.setObjectName("bel_noChars")
        self.horizontalLayout.addWidget(self.bel_noChars)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bel_maxChars = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.bel_maxChars.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_maxChars.setObjectName("bel_maxChars")
        self.horizontalLayout.addWidget(self.bel_maxChars)

        self.retranslateUi(Form)
        self.listWidget_panelVersion.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_11.setText(_translate("Form", "Tiempo de pregunta"))
        self.timeEdit.setDisplayFormat(_translate("Form", "mm:ss"))
        self.label_10.setText(_translate("Form", "Posicion pregunta"))
        self.label_9.setText(_translate("Form", "Incluir imagenes"))
        self.label_12.setText(_translate("Form", "Tipo respuesta"))
        self.label.setText(_translate("Form", "Respuesta:"))
        self.label_2.setText(_translate("Form", "Caracteres/Digitos:"))
        self.bel_noChars.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "/"))
        self.bel_maxChars.setText(_translate("Form", "0"))

import imagenes_rc
