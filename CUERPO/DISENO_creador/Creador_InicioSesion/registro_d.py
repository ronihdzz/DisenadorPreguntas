# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registro_d.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(639, 479)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_17 = QtWidgets.QLabel(Dialog)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setMinimumSize(QtCore.QSize(320, 70))
        self.label_12.setMaximumSize(QtCore.QSize(310, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(85, 0, 127);\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_infoDudas = QtWidgets.QPushButton(Dialog)
        self.btn_infoDudas.setMinimumSize(QtCore.QSize(20, 20))
        self.btn_infoDudas.setMaximumSize(QtCore.QSize(20, 20))
        self.btn_infoDudas.setStyleSheet("QPushButton {\n"
"    border-image: url(:/prefijoNuevo/IMAGENES_creador/tache_2.png);\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/info_off.png);\n"
" }\n"
"QPushButton:hover {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/info_on.png);\n"
"}\n"
"QPushButton:pressed {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/info_off.png);\n"
"}")
        self.btn_infoDudas.setText("")
        self.btn_infoDudas.setObjectName("btn_infoDudas")
        self.verticalLayout.addWidget(self.btn_infoDudas)
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setMinimumSize(QtCore.QSize(25, 25))
        self.label_11.setMaximumSize(QtCore.QSize(25, 25))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label_18 = QtWidgets.QLabel(Dialog)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_2.addWidget(self.label_18)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setMinimumSize(QtCore.QSize(150, 50))
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.le_nameUser = QtWidgets.QLineEdit(Dialog)
        self.le_nameUser.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.le_nameUser.setFont(font)
        self.le_nameUser.setMaxLength(20)
        self.le_nameUser.setObjectName("le_nameUser")
        self.horizontalLayout.addWidget(self.le_nameUser)
        self.btn_nameUser = QtWidgets.QPushButton(Dialog)
        self.btn_nameUser.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_nameUser.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_nameUser.setStyleSheet("QPushButton{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_0.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"     border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_1.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_2.png);\n"
"}")
        self.btn_nameUser.setText("")
        self.btn_nameUser.setObjectName("btn_nameUser")
        self.horizontalLayout.addWidget(self.btn_nameUser)
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setMinimumSize(QtCore.QSize(70, 50))
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.sB_edad = QtWidgets.QSpinBox(Dialog)
        self.sB_edad.setMinimumSize(QtCore.QSize(70, 40))
        self.sB_edad.setMaximumSize(QtCore.QSize(70, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.sB_edad.setFont(font)
        self.sB_edad.setAlignment(QtCore.Qt.AlignCenter)
        self.sB_edad.setMinimum(4)
        self.sB_edad.setObjectName("sB_edad")
        self.horizontalLayout.addWidget(self.sB_edad)
        self.btn_edad = QtWidgets.QPushButton(Dialog)
        self.btn_edad.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_edad.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_edad.setStyleSheet("QPushButton{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/paloma_0.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"     border-image:url(:/prefijoNuevo/IMAGENES_creador/paloma_1.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/paloma_2.png);\n"
"}")
        self.btn_edad.setText("")
        self.btn_edad.setObjectName("btn_edad")
        self.horizontalLayout.addWidget(self.btn_edad)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMinimumSize(QtCore.QSize(20, 0))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setMinimumSize(QtCore.QSize(150, 0))
        self.label_10.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.le_password_1 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.le_password_1.setFont(font)
        self.le_password_1.setMaxLength(20)
        self.le_password_1.setObjectName("le_password_1")
        self.horizontalLayout_4.addWidget(self.le_password_1)
        self.btn_mostrarPassword_1 = QtWidgets.QPushButton(Dialog)
        self.btn_mostrarPassword_1.setMinimumSize(QtCore.QSize(41, 31))
        self.btn_mostrarPassword_1.setMaximumSize(QtCore.QSize(41, 31))
        self.btn_mostrarPassword_1.setStyleSheet("")
        self.btn_mostrarPassword_1.setText("")
        self.btn_mostrarPassword_1.setObjectName("btn_mostrarPassword_1")
        self.horizontalLayout_4.addWidget(self.btn_mostrarPassword_1)
        self.btn_password_1 = QtWidgets.QPushButton(Dialog)
        self.btn_password_1.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_password_1.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_password_1.setStyleSheet("QPushButton{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_0.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"     border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_1.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_2.png);\n"
"}")
        self.btn_password_1.setText("")
        self.btn_password_1.setObjectName("btn_password_1")
        self.horizontalLayout_4.addWidget(self.btn_password_1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.verticalLayout_2.addWidget(self.label_16)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setMinimumSize(QtCore.QSize(150, 50))
        self.label_20.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setWordWrap(True)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_7.addWidget(self.label_20)
        self.le_password_2 = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.le_password_2.setFont(font)
        self.le_password_2.setMaxLength(20)
        self.le_password_2.setObjectName("le_password_2")
        self.horizontalLayout_7.addWidget(self.le_password_2)
        self.btn_mostrarPassword_2 = QtWidgets.QPushButton(Dialog)
        self.btn_mostrarPassword_2.setMinimumSize(QtCore.QSize(41, 31))
        self.btn_mostrarPassword_2.setMaximumSize(QtCore.QSize(41, 31))
        self.btn_mostrarPassword_2.setStyleSheet("")
        self.btn_mostrarPassword_2.setText("")
        self.btn_mostrarPassword_2.setObjectName("btn_mostrarPassword_2")
        self.horizontalLayout_7.addWidget(self.btn_mostrarPassword_2)
        self.btn_password_2 = QtWidgets.QPushButton(Dialog)
        self.btn_password_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_password_2.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_password_2.setStyleSheet("QPushButton{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_0.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"     border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_1.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_2.png);\n"
"}")
        self.btn_password_2.setText("")
        self.btn_password_2.setObjectName("btn_password_2")
        self.horizontalLayout_7.addWidget(self.btn_password_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setMinimumSize(QtCore.QSize(150, 0))
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.le_nameFriend = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.le_nameFriend.setFont(font)
        self.le_nameFriend.setMaxLength(20)
        self.le_nameFriend.setObjectName("le_nameFriend")
        self.horizontalLayout_3.addWidget(self.le_nameFriend)
        self.btn_mostrarMejorAmigo = QtWidgets.QPushButton(Dialog)
        self.btn_mostrarMejorAmigo.setMinimumSize(QtCore.QSize(41, 31))
        self.btn_mostrarMejorAmigo.setMaximumSize(QtCore.QSize(41, 31))
        self.btn_mostrarMejorAmigo.setStyleSheet("")
        self.btn_mostrarMejorAmigo.setText("")
        self.btn_mostrarMejorAmigo.setObjectName("btn_mostrarMejorAmigo")
        self.horizontalLayout_3.addWidget(self.btn_mostrarMejorAmigo)
        self.btn_mejorAmigo = QtWidgets.QPushButton(Dialog)
        self.btn_mejorAmigo.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_mejorAmigo.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_mejorAmigo.setStyleSheet("QPushButton{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_0.png);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"     border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_1.png);\n"
"}\n"
"QPushButton:pressed{\n"
"    border-image:url(:/prefijoNuevo/IMAGENES_creador/tache_2.png);\n"
"}")
        self.btn_mejorAmigo.setText("")
        self.btn_mejorAmigo.setObjectName("btn_mejorAmigo")
        self.horizontalLayout_3.addWidget(self.btn_mejorAmigo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.verticalLayout_2.addWidget(self.label_21)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.btn_terminarRegistro = QtWidgets.QCommandLinkButton(Dialog)
        self.btn_terminarRegistro.setMinimumSize(QtCore.QSize(120, 0))
        self.btn_terminarRegistro.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.btn_terminarRegistro.setFont(font)
        self.btn_terminarRegistro.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon.fromTheme("?")
        self.btn_terminarRegistro.setIcon(icon)
        self.btn_terminarRegistro.setObjectName("btn_terminarRegistro")
        self.horizontalLayout_6.addWidget(self.btn_terminarRegistro)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_12.setText(_translate("Dialog", "Registro de usuario:"))
        self.label_3.setText(_translate("Dialog", "Nombre de usuario:"))
        self.label_8.setText(_translate("Dialog", "Edad:"))
        self.label_10.setText(_translate("Dialog", "Contraseña:"))
        self.label_20.setText(_translate("Dialog", "Repetir contraseña:"))
        self.label_9.setText(_translate("Dialog", "Nombrede mi mejor amigo:"))
        self.label_4.setText(_translate("Dialog", "l"))
        self.btn_terminarRegistro.setText(_translate("Dialog", "terminar"))
import IMAGENES_rc
