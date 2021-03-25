# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespBinariaImagen50_d.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(899, 488)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txtEdit_preg = QtWidgets.QTextEdit(Form)
        self.txtEdit_preg.setMinimumSize(QtCore.QSize(350, 121))
        self.txtEdit_preg.setMaximumSize(QtCore.QSize(480, 180))
        self.txtEdit_preg.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_preg.setObjectName("txtEdit_preg")
        self.verticalLayout_2.addWidget(self.txtEdit_preg)
        self.bel_pregImage = QtWidgets.QLabel(Form)
        self.bel_pregImage.setMinimumSize(QtCore.QSize(350, 320))
        self.bel_pregImage.setMaximumSize(QtCore.QSize(480, 800))
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
        self.verticalLayout_2.addWidget(self.bel_pregImage)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_respA = QtWidgets.QPushButton(Form)
        self.btn_respA.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_respA.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respA.setFont(font)
        self.btn_respA.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respA.setObjectName("btn_respA")
        self.horizontalLayout.addWidget(self.btn_respA)
        self.txtEdit_respA = QtWidgets.QTextEdit(Form)
        self.txtEdit_respA.setMinimumSize(QtCore.QSize(380, 180))
        self.txtEdit_respA.setMaximumSize(QtCore.QSize(600, 200))
        self.txtEdit_respA.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respA.setObjectName("txtEdit_respA")
        self.horizontalLayout.addWidget(self.txtEdit_respA)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_respB = QtWidgets.QPushButton(Form)
        self.btn_respB.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_respB.setMaximumSize(QtCore.QSize(70, 70))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respB.setFont(font)
        self.btn_respB.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respB.setObjectName("btn_respB")
        self.horizontalLayout_2.addWidget(self.btn_respB)
        self.txtEdit_respB = QtWidgets.QTextEdit(Form)
        self.txtEdit_respB.setMinimumSize(QtCore.QSize(380, 180))
        self.txtEdit_respB.setMaximumSize(QtCore.QSize(600, 200))
        self.txtEdit_respB.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respB.setObjectName("txtEdit_respB")
        self.horizontalLayout_2.addWidget(self.txtEdit_respB)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_respA.setText(_translate("Form", "A"))
        self.btn_respB.setText(_translate("Form", "B"))
