# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreadorPreguntasMain_d.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1043, 610)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn_mas = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mas.setMinimumSize(QtCore.QSize(51, 41))
        self.btn_mas.setMaximumSize(QtCore.QSize(51, 41))
        self.btn_mas.setStyleSheet("border-image: url(:/prefijoNuevo/IMAGENES_creador/pregunta_add.png);\n"
"")
        self.btn_mas.setText("")
        self.btn_mas.setObjectName("btn_mas")
        self.verticalLayout.addWidget(self.btn_mas, 0, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setMinimumSize(QtCore.QSize(79, 26))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.scroll_barra = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_barra.setMinimumSize(QtCore.QSize(90, 150))
        self.scroll_barra.setMaximumSize(QtCore.QSize(115, 16777215))
        self.scroll_barra.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setObjectName("scroll_barra")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 71, 480))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_barra.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scroll_barra)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.listWidget_panelPreguntas = QtWidgets.QStackedWidget(self.centralwidget)
        self.listWidget_panelPreguntas.setMinimumSize(QtCore.QSize(911, 551))
        self.listWidget_panelPreguntas.setMaximumSize(QtCore.QSize(1200, 800))
        self.listWidget_panelPreguntas.setToolTipDuration(0)
        self.listWidget_panelPreguntas.setStyleSheet("")
        self.listWidget_panelPreguntas.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_panelPreguntas.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget_panelPreguntas.setObjectName("listWidget_panelPreguntas")
        self.horizontalLayout_4.addWidget(self.listWidget_panelPreguntas)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.btn_next_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_next_2.setMaximumSize(QtCore.QSize(70, 70))
        self.btn_next_2.setStyleSheet("QPushButton {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen5_nextE.png);  }\n"
"\n"
"QPushButton:hover {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen4_nextD.png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen5_nextE.png);\n"
"}\n"
"")
        self.btn_next_2.setText("")
        self.btn_next_2.setObjectName("btn_next_2")
        self.verticalLayout_3.addWidget(self.btn_next_2)
        self.btn_prev_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prev_2.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_prev_2.setMaximumSize(QtCore.QSize(70, 70))
        self.btn_prev_2.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen5_prevE.png);\n"
"  }\n"
"QPushButton:hover {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen4_prevD .png);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"border-image: url(:/prefijoNuevo/IMAGENES_creador/imagen5_prevE.png);\n"
"}\n"
"")
        self.btn_prev_2.setText("")
        self.btn_prev_2.setObjectName("btn_prev_2")
        self.verticalLayout_3.addWidget(self.btn_prev_2)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1043, 21))
        self.menubar.setObjectName("menubar")
        self.menuNueva_pregunta = QtWidgets.QMenu(self.menubar)
        self.menuNueva_pregunta.setObjectName("menuNueva_pregunta")
        self.menuCuestionario = QtWidgets.QMenu(self.menubar)
        self.menuCuestionario.setObjectName("menuCuestionario")
        self.menuCompartir = QtWidgets.QMenu(self.menubar)
        self.menuCompartir.setObjectName("menuCompartir")
        self.menuConcluyente = QtWidgets.QMenu(self.menubar)
        self.menuConcluyente.setObjectName("menuConcluyente")
        self.menuImportar = QtWidgets.QMenu(self.menubar)
        self.menuImportar.setObjectName("menuImportar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCrear_nueva_pregunta = QtWidgets.QAction(MainWindow)
        self.actionCrear_nueva_pregunta.setObjectName("actionCrear_nueva_pregunta")
        self.actionEliminar_una_pregunta = QtWidgets.QAction(MainWindow)
        self.actionEliminar_una_pregunta.setObjectName("actionEliminar_una_pregunta")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionCambiar_nombre = QtWidgets.QAction(MainWindow)
        self.actionCambiar_nombre.setObjectName("actionCambiar_nombre")
        self.actionVisualizar = QtWidgets.QAction(MainWindow)
        self.actionVisualizar.setObjectName("actionVisualizar")
        self.actionSubir_a_DelphiData = QtWidgets.QAction(MainWindow)
        self.actionSubir_a_DelphiData.setObjectName("actionSubir_a_DelphiData")
        self.actionMandar_por_correo = QtWidgets.QAction(MainWindow)
        self.actionMandar_por_correo.setObjectName("actionMandar_por_correo")
        self.actionEjecutar_cuestionario = QtWidgets.QAction(MainWindow)
        self.actionEjecutar_cuestionario.setObjectName("actionEjecutar_cuestionario")
        self.actionGuarda_en_otra_carpeta = QtWidgets.QAction(MainWindow)
        self.actionGuarda_en_otra_carpeta.setObjectName("actionGuarda_en_otra_carpeta")
        self.actionSubir_a_cuestionarios_oficiales = QtWidgets.QAction(MainWindow)
        self.actionSubir_a_cuestionarios_oficiales.setObjectName("actionSubir_a_cuestionarios_oficiales")
        self.actionEliminar_todo_el_cuestionario = QtWidgets.QAction(MainWindow)
        self.actionEliminar_todo_el_cuestionario.setObjectName("actionEliminar_todo_el_cuestionario")
        self.actionImportar_otro_cuestionario = QtWidgets.QAction(MainWindow)
        self.actionImportar_otro_cuestionario.setObjectName("actionImportar_otro_cuestionario")
        self.actionImportar_otro_cuestionario_2 = QtWidgets.QAction(MainWindow)
        self.actionImportar_otro_cuestionario_2.setObjectName("actionImportar_otro_cuestionario_2")
        self.actionSubir_como_cuestionario_oficial = QtWidgets.QAction(MainWindow)
        self.actionSubir_como_cuestionario_oficial.setObjectName("actionSubir_como_cuestionario_oficial")
        self.actionCompartir_cuestionario_al_servidor = QtWidgets.QAction(MainWindow)
        self.actionCompartir_cuestionario_al_servidor.setObjectName("actionCompartir_cuestionario_al_servidor")
        self.actionSubir_cuestionario_cuestionario_como_cuestionario_final = QtWidgets.QAction(MainWindow)
        self.actionSubir_cuestionario_cuestionario_como_cuestionario_final.setObjectName("actionSubir_cuestionario_cuestionario_como_cuestionario_final")
        self.menuNueva_pregunta.addAction(self.actionCrear_nueva_pregunta)
        self.menuNueva_pregunta.addAction(self.actionVisualizar)
        self.menuCuestionario.addAction(self.actionCambiar_nombre)
        self.menuCuestionario.addAction(self.actionEjecutar_cuestionario)
        self.menuCompartir.addSeparator()
        self.menuCompartir.addSeparator()
        self.menuCompartir.addAction(self.actionCompartir_cuestionario_al_servidor)
        self.menuCompartir.addAction(self.actionSubir_cuestionario_cuestionario_como_cuestionario_final)
        self.menuConcluyente.addAction(self.actionEliminar_todo_el_cuestionario)
        self.menuImportar.addAction(self.actionImportar_otro_cuestionario_2)
        self.menubar.addAction(self.menuCuestionario.menuAction())
        self.menubar.addAction(self.menuNueva_pregunta.menuAction())
        self.menubar.addAction(self.menuCompartir.menuAction())
        self.menubar.addAction(self.menuImportar.menuAction())
        self.menubar.addAction(self.menuConcluyente.menuAction())

        self.retranslateUi(MainWindow)
        self.listWidget_panelPreguntas.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Agregar otra\n"
"pregunta"))
        self.menuNueva_pregunta.setTitle(_translate("MainWindow", "Preguntas"))
        self.menuCuestionario.setTitle(_translate("MainWindow", "Cuestionario"))
        self.menuCompartir.setTitle(_translate("MainWindow", "Exportar"))
        self.menuConcluyente.setTitle(_translate("MainWindow", "Concluyente"))
        self.menuImportar.setTitle(_translate("MainWindow", "Importar"))
        self.actionCrear_nueva_pregunta.setText(_translate("MainWindow", "Crear"))
        self.actionEliminar_una_pregunta.setText(_translate("MainWindow", "Eliminar"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar "))
        self.actionCambiar_nombre.setText(_translate("MainWindow", "Cambiar nombre"))
        self.actionVisualizar.setText(_translate("MainWindow", "Visualizar "))
        self.actionSubir_a_DelphiData.setText(_translate("MainWindow", "Subir a mis cuestionarios Delphi"))
        self.actionMandar_por_correo.setText(_translate("MainWindow", "Mandar por correo"))
        self.actionEjecutar_cuestionario.setText(_translate("MainWindow", "Ejecutar cuestionario"))
        self.actionGuarda_en_otra_carpeta.setText(_translate("MainWindow", "Guardar en otra carpeta"))
        self.actionSubir_a_cuestionarios_oficiales.setText(_translate("MainWindow", "Subir como cuestionario oficial"))
        self.actionEliminar_todo_el_cuestionario.setText(_translate("MainWindow", "Eliminar todo el cuestionario"))
        self.actionImportar_otro_cuestionario.setText(_translate("MainWindow", "Importar otro cuestionario"))
        self.actionImportar_otro_cuestionario_2.setText(_translate("MainWindow", "Importar otro cuestionario"))
        self.actionSubir_como_cuestionario_oficial.setText(_translate("MainWindow", "Subir como cuestionario oficial"))
        self.actionCompartir_cuestionario_al_servidor.setText(_translate("MainWindow", "Compartir cuestionario al servidor"))
        self.actionSubir_cuestionario_cuestionario_como_cuestionario_final.setText(_translate("MainWindow", "Subir cuestionario como cuestionario final"))
import IMAG_rc
