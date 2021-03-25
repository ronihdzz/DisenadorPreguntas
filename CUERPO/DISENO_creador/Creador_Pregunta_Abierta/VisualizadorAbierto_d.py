# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VisualizadorAbierto_d.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(915, 513)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.listWidget_panelVersion = QtWidgets.QStackedWidget(Form)
        self.listWidget_panelVersion.setMinimumSize(QtCore.QSize(451, 411))
        self.listWidget_panelVersion.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget_panelVersion.setToolTipDuration(0)
        self.listWidget_panelVersion.setStyleSheet("")
        self.listWidget_panelVersion.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelVersion.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelVersion.setObjectName("listWidget_panelVersion")
        self.horizontalLayout_6.addWidget(self.listWidget_panelVersion)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(241, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.lineEdit_respuesta = QtWidgets.QLineEdit(Form)
        self.lineEdit_respuesta.setMaximumSize(QtCore.QSize(16777215, 71))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_respuesta.setFont(font)
        self.lineEdit_respuesta.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_respuesta.setObjectName("lineEdit_respuesta")
        self.verticalLayout_5.addWidget(self.lineEdit_respuesta)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMaximumSize(QtCore.QSize(93, 69))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.bel_noChars = QtWidgets.QLabel(Form)
        self.bel_noChars.setMaximumSize(QtCore.QSize(10000000, 69))
        self.bel_noChars.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_noChars.setObjectName("bel_noChars")
        self.horizontalLayout.addWidget(self.bel_noChars)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMaximumSize(QtCore.QSize(1000000, 69))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.bel_maxChars = QtWidgets.QLabel(Form)
        self.bel_maxChars.setMaximumSize(QtCore.QSize(16777215, 69))
        self.bel_maxChars.setAlignment(QtCore.Qt.AlignCenter)
        self.bel_maxChars.setObjectName("bel_maxChars")
        self.horizontalLayout.addWidget(self.bel_maxChars)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_5.addWidget(self.label_10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout_6)

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
