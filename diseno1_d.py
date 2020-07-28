# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diseno1_d.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(884, 518)
        self.txtEdit_preg = QtWidgets.QTextEdit(Form)
        self.txtEdit_preg.setGeometry(QtCore.QRect(180, 110, 611, 121))
        self.txtEdit_preg.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_preg.setObjectName("txtEdit_preg")
        self.txt_b = QtWidgets.QTextEdit(Form)
        self.txt_b.setGeometry(QtCore.QRect(200, 360, 251, 81))
        self.txt_b.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txt_b.setObjectName("txt_b")
        self.txt_c = QtWidgets.QTextEdit(Form)
        self.txt_c.setGeometry(QtCore.QRect(580, 260, 251, 81))
        self.txt_c.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txt_c.setObjectName("txt_c")
        self.txtEdit_a = QtWidgets.QTextEdit(Form)
        self.txtEdit_a.setGeometry(QtCore.QRect(200, 260, 251, 81))
        self.txtEdit_a.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txtEdit_a.setObjectName("txtEdit_a")
        self.txt_d = QtWidgets.QTextEdit(Form)
        self.txt_d.setGeometry(QtCore.QRect(580, 360, 251, 81))
        self.txt_d.setStyleSheet("  background-color: #19232D;\n"
"  border: 0px solid #32414B;\n"
"  padding: 0px;\n"
"  color: #F0F0F0;\n"
"  selection-background-color: #1464A0;\n"
"  selection-color: #F0F0F0;\n"
"\n"
"    border-radius: 10;")
        self.txt_d.setObjectName("txt_d")
        self.scroll_barra = QtWidgets.QScrollArea(Form)
        self.scroll_barra.setGeometry(QtCore.QRect(10, 80, 81, 421))
        self.scroll_barra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setObjectName("scroll_barra")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 65, 419))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_barra.setWidget(self.scrollAreaWidgetContents)
        self.btn_mas_2 = QtWidgets.QPushButton(Form)
        self.btn_mas_2.setGeometry(QtCore.QRect(770, 20, 89, 25))
        self.btn_mas_2.setObjectName("btn_mas_2")
        self.btn_mas = QtWidgets.QPushButton(Form)
        self.btn_mas.setGeometry(QtCore.QRect(650, 20, 89, 25))
        self.btn_mas.setObjectName("btn_mas")
        self.btn_ver = QtWidgets.QPushButton(Form)
        self.btn_ver.setGeometry(QtCore.QRect(530, 20, 89, 25))
        self.btn_ver.setObjectName("btn_ver")
        self.btn_Datos = QtWidgets.QPushButton(Form)
        self.btn_Datos.setGeometry(QtCore.QRect(100, 260, 89, 81))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_Datos.setFont(font)
        self.btn_Datos.setStyleSheet("QPushButton {\n"
"/*color: #333;*/\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"/*background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");*/\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        self.btn_Datos.setObjectName("btn_Datos")
        self.btn_Datos_2 = QtWidgets.QPushButton(Form)
        self.btn_Datos_2.setGeometry(QtCore.QRect(100, 360, 89, 81))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_Datos_2.setFont(font)
        self.btn_Datos_2.setStyleSheet("QPushButton {\n"
"/*color: #333;*/\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"/*background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");*/\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        self.btn_Datos_2.setObjectName("btn_Datos_2")
        self.btn_Datos_3 = QtWidgets.QPushButton(Form)
        self.btn_Datos_3.setGeometry(QtCore.QRect(480, 260, 89, 81))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_Datos_3.setFont(font)
        self.btn_Datos_3.setStyleSheet("QPushButton {\n"
"/*color: #333;*/\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"/*background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");*/\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        self.btn_Datos_3.setObjectName("btn_Datos_3")
        self.btn_Datos_4 = QtWidgets.QPushButton(Form)
        self.btn_Datos_4.setGeometry(QtCore.QRect(480, 360, 89, 81))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.btn_Datos_4.setFont(font)
        self.btn_Datos_4.setStyleSheet("QPushButton {\n"
"/*color: #333;*/\n"
"border: 1px solid #555;\n"
"border-radius: 20px;\n"
"border-style: outset;\n"
"/*background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #888\n"
");*/\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: qradialgradient(\n"
"cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #bbb\n"
");\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-style: inset;\n"
"background: qradialgradient(\n"
"cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1,\n"
"radius: 1.35, stop: 0 #fff, stop: 1 #ddd\n"
");\n"
"}")
        self.btn_Datos_4.setObjectName("btn_Datos_4")
        self.lineEdit_tamano = QtWidgets.QLineEdit(Form)
        self.lineEdit_tamano.setGeometry(QtCore.QRect(120, 110, 41, 25))
        self.lineEdit_tamano.setObjectName("lineEdit_tamano")
        self.btn_aplicarTam = QtWidgets.QPushButton(Form)
        self.btn_aplicarTam.setGeometry(QtCore.QRect(110, 140, 61, 25))
        self.btn_aplicarTam.setObjectName("btn_aplicarTam")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_mas_2.setText(_translate("Form", "MAS"))
        self.btn_mas.setText(_translate("Form", "BORRAR"))
        self.btn_ver.setText(_translate("Form", "VER"))
        self.btn_Datos.setText(_translate("Form", "A"))
        self.btn_Datos_2.setText(_translate("Form", "B"))
        self.btn_Datos_3.setText(_translate("Form", "C"))
        self.btn_Datos_4.setText(_translate("Form", "D"))
        self.btn_aplicarTam.setText(_translate("Form", "APL"))

