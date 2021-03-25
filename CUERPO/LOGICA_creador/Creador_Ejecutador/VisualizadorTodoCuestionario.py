import sqlite3
from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QGridLayout,QHBoxLayout
from PyQt5.QtCore import Qt, pyqtSignal,QObject
from PyQt5.QtWidgets import  QMessageBox
import datetime
from PyQt5 import QtWidgets,QtGui,Qt
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import  QPixmap
###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Ejecutador.VisualizacionTodoCuestionario_d import Ui_Dialog


###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.LOGICA_creador.Creador_Pregunta_Binaria.Visualizador_PreguntaBinaria import VisualizadorPreguntaBinaria
from CUERPO.LOGICA_creador.Creador_Pregunta_Multiple.Visualizador_PreguntaMultiple import VisualizadorPreguntaMultiple
from CUERPO.LOGICA_creador.Creador_Preguna_CheckBox.Visualizador_PreguntaCheckBox import VisualizadorPregunta_CheckBox
from CUERPO.LOGICA_creador.Creador_Pregunta_Abierta.Visualizador_PreguntaAbierta import VisualizadorPregunta_Abierta
from CUERPO.LOGICA_creador.Creador_Ejecutador.VisualizadorTodoCuestionarioVacio import VisualizadorTodoCuestionarioVacio

###############################################################
#  MIS LIBRERIAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.DataBaseCreadorPreguntas import DataBaseCreadorPreguntas
from CUERPO.LOGICA_creador.Creador_Ventanas_Dialogo.ConfirmadorAccion import ConfirmadorAccion
from CUERPO.LOGICA_creador.Creador_MisPaquetes.comportSelect_btnsImagen import comporSelec_btnsImagen
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios



class VisualizadorTodoCuestionario(QtWidgets.QDialog, Ui_Dialog):

    # Metodo constructor:
    senalCuestionarioConfirmado = pyqtSignal(str) #dira si la accion se confirmo bien...
    senalTermino = pyqtSignal(bool)  # comunicacion con la aplicacion
    def __init__(self,nombreCuestionario="",descargados=False,mios=False,oficiales=False,compartidos=False,dictDatos={}):
        Ui_Dialog.__init__(self)
        QtWidgets.QDialog.__init__(self)
        self.setupUi(self)
        self.dictDatos=dictDatos #"ConfirmacionMensaje","ConfirmacionClave","Accion","Explicacion"
        self.nombreCuestionario=nombreCuestionario
        self.setWindowTitle(f"Nombre de cuestionario: {self.nombreCuestionario}")

        #Obteniendo los nombres completos con sus respectivas rutas...
        self.nombreCuestionarioCompleto,self.nombreCarpetaImagenes=self.getNombresCompletos(descargados=descargados,
                                                                                            mios=mios,
                                                                                            oficiales=oficiales,
                                                                                            compartidos=compartidos)

##############################################################################################################################
#  INCLUYENDO WIDGETS...
##############################################################################################################################
        #creando multiples ventanas...
        self.ventanas=[]
        self.listBotonesPreguntas=[]
        self.contadorPreguntas=0

        # creando multiples ventanas...
        self.ventanas = []
        self.ventanas.append( VisualizadorPreguntaBinaria(direc_carpetaImagenes=self.nombreCarpetaImagenes) )  # pregunta binaria
        self.ventanas.append( VisualizadorPreguntaMultiple(direc_carpetaImagenes=self.nombreCarpetaImagenes) ) #pregunta multiple
        self.ventanas.append( VisualizadorPregunta_CheckBox(direc_carpetaImagenes=self.nombreCarpetaImagenes) ) #visualizador pregunta checkbox
        self.ventanas.append(  VisualizadorPregunta_Abierta(direc_carpetaImagenes=self.nombreCarpetaImagenes) ) #visualizador de pregunta abierta...
        self.ventanas.append(  VisualizadorTodoCuestionarioVacio() )

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelPreguntas.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelPreguntas.setCurrentIndex(4)

        self.listWidget_panelPreguntas.showFullScreen()

        self.listBotonesPreguntas = []
        self.listIdPreguntas = []
        self.punteroPregunta = -1  # numero que no puede ser ningun puntero al incio


        # EXPLICACION DE LA VISUALIZACION....
        #self.dictDatos = dictDatos  # "ConfirmacionMensaje","ConfirmacionClave","Accion","Explicacion"
        self.btn_hagamoslo.setText(self.dictDatos["Accion"])
        self.btn_hagamoslo.clicked.connect(self.cuestionarioCasiConfirmado)
        self.ventanas[4].bel_mensajeBienvenida.setText(self.dictDatos["Explicacion"])
        self.confirmacionAccionCuestionarioVisualizado = ConfirmadorAccion(self.dictDatos["ConfirmacionMensaje"],self.dictDatos["ConfirmacionClave"])
        self.confirmacionAccionCuestionarioVisualizado.accionConfirmada.connect(self.cuestionarioConfirmado)

##############################################################################################################################
#  SCROLL DE PREGUNTAS...
##############################################################################################################################


        # Scroll Are
        # a Properties
        self.widgetVertical = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widgetVertical.setLayout(self.vbox)

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widgetVertical)




##############################################################################################################################
#  LEYENDO LAS BASES DATOS...
##############################################################################################################################


        self.controlABSOLUTO_baseDatos=DataBaseCreadorPreguntas(self.nombreCuestionarioCompleto)

        self.listaID_preguntas=self.controlABSOLUTO_baseDatos.getAllIds_preguntas()
        self.noPreguntas=len(self.listaID_preguntas)
        self.punteroPregunta = -1

        self.bel_noPreguntas.setText(str(self.noPreguntas))
        self.bel_punteroPregunta.setText(str(self.punteroPregunta+1))

        self.listaRespuestas=[]
        self.listaCalificaciones=[]
        for _ in range(self.noPreguntas):
            self.listaRespuestas.append(None)
            self.listaCalificaciones.append(False)

        self.btn_next.clicked.connect(self.verNextPregunta)
        self.btn_prev.clicked.connect(self.verPrevPregunta)

        self.crearBotonesPreguntas()
        self.punteroWidgetVisualizando=-1

        self.listWidget_panelPreguntas.setEnabled(False)#lo bloqueamos para que no puedan responder...



    def cuestionarioCasiConfirmado(self):
        self.confirmacionAccionCuestionarioVisualizado.show()

    def cuestionarioConfirmado(self):
        self.senalCuestionarioConfirmado.emit(self.nombreCuestionario)
        self.close()







    def getNombresCompletos(self,descargados=False,mios=False,oficiales=False,compartidos=False):
        if descargados+mios+oficiales+compartidos==1:
            if descargados:
                nombreCarpeta = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS+self.nombreCuestionario+"/"
            elif mios:
                nombreCarpeta= RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_EDICION+self.nombreCuestionario+"/"
            elif oficiales:
                nombreCarpeta= RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES+self.nombreCuestionario+"/"
            elif compartidos:
                nombreCarpeta = RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_COMPARTIDOS + self.nombreCuestionario + "/"

            nombreCompletoCuestionario=nombreCarpeta+self.nombreCuestionario
            nombreCarpetaImagenes=nombreCarpeta+RecursosCreadorCuestionarios.ID_CARPETA_IMAGENES+self.nombreCuestionario+"/"

            return nombreCompletoCuestionario,nombreCarpetaImagenes
        return None


##############################################################################################################################
#  VISUALIZADOR DE PREGUNTA
##############################################################################################################################

    def verContenidoPregunta(self,noPregunta,verloNuevamente=False):
        if self.punteroPregunta != noPregunta or verloNuevamente:
            self.listBotonesPreguntas[self.punteroPregunta].botonSeleccionado(False)
            self.punteroPregunta = noPregunta
            self.bel_punteroPregunta.setText(str(self.punteroPregunta+1))
            self.listBotonesPreguntas[self.punteroPregunta].botonSeleccionado(True)
            dataPregunta,dataRespuesta=self.controlABSOLUTO_baseDatos.getData(self.listaID_preguntas[self.punteroPregunta])
            # widgetPregunta = self.listWidget_panelPreguntas.currentIndex()  # nos dira en que pregunta nos econtramos...
            tipoRespuesta = dataPregunta["TIPO_RESPUESTA"]  # AHI SE ENCUENTRA EL TIPO DE RESPUESTA...
            # Eliminamos datos que no necesita...
            del dataPregunta["TIPO_RESPUESTA"]
            del dataPregunta["ID"]
            if tipoRespuesta != 3:  # pues las preguntas imagenes no tienen dataRespuesta
                del dataRespuesta["ID"]
            self.punteroWidgetVisualizando=tipoRespuesta
            self.listWidget_panelPreguntas.setCurrentIndex(tipoRespuesta)
            self.ventanas[tipoRespuesta].abrirPregunta(dataPregunta,dataRespuesta,self.listaRespuestas[self.punteroPregunta])
            self.ventanas[tipoRespuesta].mostrarRespuestaCorrecta()
            self.scrollArea.ensureWidgetVisible(self.listBotonesPreguntas[self.punteroPregunta].botonPregunta)

    def verNextPregunta(self):
        if self.punteroPregunta < (self.noPreguntas - 1):
                self.verContenidoPregunta(self.punteroPregunta+1)



    def verPrevPregunta(self):
        if self.punteroPregunta>=1:
            self.verContenidoPregunta(self.punteroPregunta-1)

    def crearBotonesPreguntas(self):
        for x in range(self.noPreguntas):
            self.agregarPregunta(x)

    def agregarPregunta(self,noBoton):
        botonPregunta=QPushButton()
        botonPregunta.setMaximumSize(40,40)
        botonPregunta.setMinimumSize(40,40)
        nuevoBotonPregunta=BotonPregunta(noBoton,botonPregunta)
        self.listBotonesPreguntas.append(nuevoBotonPregunta)
        nuevoBotonPregunta.clickBotonPregunta.connect(self.verContenidoPregunta)
        self.vbox.addWidget(botonPregunta,alignment=QtCore.Qt.AlignHCenter)


    def cambiarTam(self,editText,newValor):
        # Cambiando el tamaño
        font = QtGui.QFont()
        font.setPointSize(int(newValor))
        editText.setFont(font)



    def closeEvent(self, event):
        self.senalTermino.emit(True)
        event.accept()





class BotonPregunta(QObject):
    clickBotonPregunta=pyqtSignal(int)#indicara el id del boton
    def __init__(self,id,botonPregunta):
        QObject.__init__(self)
        self.id=id #(numeroPregunta,boton)
        self.botonPregunta=botonPregunta
        self.botonPregunta.setText(str(self.id+1))
        self.botonPregunta.clicked.connect(self.darIdBotonPregunta)

        self.COLOR_NORMAL = "#EAE5E5"
        self.COLOR_SELECCION = "#58C3D0"
        self.BORDER_RADIUS = "7"
        self.botonSeleccionado(False)

    def botonSeleccionado(self,botonPresionado):
        if botonPresionado:
            self.botonPregunta.setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                            f"border-radius:{self.BORDER_RADIUS}px;"
                                                            "border: 0.5px solid #555;")
        else:
            self.botonPregunta.setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                            f"border-radius:{self.BORDER_RADIUS}px;"
                                                            "border: 0.5px solid #555;")

    def darIdBotonPregunta(self):
        self.clickBotonPregunta.emit(self.id)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    # self.dictDatos = dictDatos  # "ConfirmacionMensaje","ConfirmacionClave","Accion","Explicacion"
    indicaciones = "En delphiApp nos preocupa que NO hagas cosas accidentalmente,"
    indicaciones += "y mas en acciones  trascedentales,por "
    indicaciones += "tal motivo empleamos este metodo de confirmacion, ¿en verdad "
    indicaciones += "estas seguro de que este cuestionario es el correcto?"

    claveConfirmacion = "estoy seguro"
    accion="CONFIRMAR QUE ES EL CUESTIONARIO QUE QUIERO"
    explicacion="Por favor, navega por el cuestionario para que corrobores acerca "
    explicacion+="de si es el cuestionario que deseas"

    dicDatos={
            "ConfirmacionMensaje":indicaciones,
            "ConfirmacionClave":claveConfirmacion,
            "Accion":accion,
            "Explicacion":explicacion
            }

    application = VisualizadorTodoCuestionario(nombreCuestionario="RoniHernandez",dictDatos=dicDatos,descargados=True)
    application.show()
    app.exec()
    #sys.exit(app.exec())