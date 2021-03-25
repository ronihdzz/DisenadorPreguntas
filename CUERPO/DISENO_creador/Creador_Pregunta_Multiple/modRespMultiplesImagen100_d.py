# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modRespMultiplesImagen100_d.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(891, 490)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.txtEdit_preg = QtWidgets.QTextEdit(Form)
        self.txtEdit_preg.setMinimumSize(QtCore.QSize(300, 90))
        self.txtEdit_preg.setMaximumSize(QtCore.QSize(500, 230))
        self.txtEdit_preg.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_preg.setObjectName("txtEdit_preg")
        self.verticalLayout_7.addWidget(self.txtEdit_preg)
        self.bel_pregImage = QtWidgets.QLabel(Form)
        self.bel_pregImage.setMinimumSize(QtCore.QSize(300, 330))
        self.bel_pregImage.setMaximumSize(QtCore.QSize(500, 800))
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
        self.verticalLayout_7.addWidget(self.bel_pregImage)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bel_imageRespA = QtWidgets.QLabel(Form)
        self.bel_imageRespA.setMinimumSize(QtCore.QSize(241, 181))
        self.bel_imageRespA.setMaximumSize(QtCore.QSize(350, 260))
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
        self.verticalLayout_3.addWidget(self.bel_imageRespA)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_respA = QtWidgets.QPushButton(Form)
        self.btn_respA.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_respA.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respA.setFont(font)
        self.btn_respA.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respA.setObjectName("btn_respA")
        self.horizontalLayout_3.addWidget(self.btn_respA)
        self.txtEdit_respA = QtWidgets.QTextEdit(Form)
        self.txtEdit_respA.setMinimumSize(QtCore.QSize(201, 41))
        self.txtEdit_respA.setMaximumSize(QtCore.QSize(300, 60))
        self.txtEdit_respA.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respA.setObjectName("txtEdit_respA")
        self.horizontalLayout_3.addWidget(self.txtEdit_respA)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.bel_imageRespB = QtWidgets.QLabel(Form)
        self.bel_imageRespB.setMinimumSize(QtCore.QSize(241, 181))
        self.bel_imageRespB.setMaximumSize(QtCore.QSize(350, 260))
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
        self.verticalLayout.addWidget(self.bel_imageRespB)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_respB = QtWidgets.QPushButton(Form)
        self.btn_respB.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_respB.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respB.setFont(font)
        self.btn_respB.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respB.setObjectName("btn_respB")
        self.horizontalLayout.addWidget(self.btn_respB)
        self.txtEdit_respB = QtWidgets.QTextEdit(Form)
        self.txtEdit_respB.setMinimumSize(QtCore.QSize(201, 41))
        self.txtEdit_respB.setMaximumSize(QtCore.QSize(300, 60))
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
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.bel_imageRespC = QtWidgets.QLabel(Form)
        self.bel_imageRespC.setMinimumSize(QtCore.QSize(241, 181))
        self.bel_imageRespC.setMaximumSize(QtCore.QSize(350, 260))
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
        self.verticalLayout_6.addWidget(self.bel_imageRespC)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btn_respC = QtWidgets.QPushButton(Form)
        self.btn_respC.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_respC.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respC.setFont(font)
        self.btn_respC.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respC.setObjectName("btn_respC")
        self.horizontalLayout_4.addWidget(self.btn_respC)
        self.txtEdit_respC = QtWidgets.QTextEdit(Form)
        self.txtEdit_respC.setMinimumSize(QtCore.QSize(201, 41))
        self.txtEdit_respC.setMaximumSize(QtCore.QSize(300, 60))
        self.txtEdit_respC.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respC.setObjectName("txtEdit_respC")
        self.horizontalLayout_4.addWidget(self.txtEdit_respC)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout_6)
        self.bel_imageRespD = QtWidgets.QLabel(Form)
        self.bel_imageRespD.setMinimumSize(QtCore.QSize(241, 181))
        self.bel_imageRespD.setMaximumSize(QtCore.QSize(350, 260))
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
        self.verticalLayout_2.addWidget(self.bel_imageRespD)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_respD = QtWidgets.QPushButton(Form)
        self.btn_respD.setMinimumSize(QtCore.QSize(41, 41))
        self.btn_respD.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_respD.setFont(font)
        self.btn_respD.setStyleSheet("background-color:#EEF2F3;\n"
"border-radius: 7px;\n"
"border: 1px solid #555;")
        self.btn_respD.setObjectName("btn_respD")
        self.horizontalLayout_2.addWidget(self.btn_respD)
        self.txtEdit_respD = QtWidgets.QTextEdit(Form)
        self.txtEdit_respD.setMinimumSize(QtCore.QSize(201, 41))
        self.txtEdit_respD.setMaximumSize(QtCore.QSize(300, 60))
        self.txtEdit_respD.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_respD.setObjectName("txtEdit_respD")
        self.horizontalLayout_2.addWidget(self.txtEdit_respD)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_respA.setText(_translate("Form", "A"))
        self.btn_respB.setText(_translate("Form", "B"))
        self.btn_respC.setText(_translate("Form", "C"))
        self.btn_respD.setText(_translate("Form", "D"))
