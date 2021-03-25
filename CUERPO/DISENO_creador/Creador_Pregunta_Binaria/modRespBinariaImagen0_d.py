# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespBinariaImagen0_d.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(903, 495)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.txtEdit_preg = QtWidgets.QTextEdit(Form)
        self.txtEdit_preg.setMinimumSize(QtCore.QSize(861, 231))
        self.txtEdit_preg.setMaximumSize(QtCore.QSize(1200, 300))
        self.txtEdit_preg.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_preg.setObjectName("txtEdit_preg")
        self.horizontalLayout_2.addWidget(self.txtEdit_preg)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
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
        self.txtEdit_respA.setMinimumSize(QtCore.QSize(381, 151))
        self.txtEdit_respA.setMaximumSize(QtCore.QSize(500, 200))
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
        self.horizontalLayout.addWidget(self.btn_respB)
        self.txtEdit_respB = QtWidgets.QTextEdit(Form)
        self.txtEdit_respB.setMinimumSize(QtCore.QSize(381, 151))
        self.txtEdit_respB.setMaximumSize(QtCore.QSize(500, 200))
        self.txtEdit_respB.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respB.setObjectName("txtEdit_respB")
        self.horizontalLayout.addWidget(self.txtEdit_respB)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_respA.setText(_translate("Form", "A"))
        self.btn_respB.setText(_translate("Form", "B"))
