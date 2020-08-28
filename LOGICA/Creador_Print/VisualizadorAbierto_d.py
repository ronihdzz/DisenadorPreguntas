# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizadorAbierto_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 510)
        self.listWidget_panelVersion = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelVersion.setGeometry(QtCore.QRect(10, 10, 451, 491))
        self.listWidget_panelVersion.setToolTipDuration(0)
        self.listWidget_panelVersion.setStyleSheet("")
        self.listWidget_panelVersion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelVersion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelVersion.setObjectName("listWidget_panelVersion")
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
        self.label.setText(_translate("Form", "Respuesta:"))
        self.label_2.setText(_translate("Form", "Caracteres/Digitos:"))
        self.bel_noChars.setText(_translate("Form", "0"))
        self.label_3.setText(_translate("Form", "/"))
        self.bel_maxChars.setText(_translate("Form", "0"))

import imagenes_rc
