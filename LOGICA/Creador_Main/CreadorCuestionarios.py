import sqlite3
from LOGICA.Creador_MisPaquetes.DataBaseCreadorPreguntas import DataBaseCreadorPreguntas

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
from DISENO.Creador_Ejecutador.EjecutadorCuestionario_d import Ui_Form


###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from LOGICA.Creador_Pregunta_Binaria.Visualizador_PreguntaBinaria import VisualizadorPreguntaBinaria
from LOGICA.Creador_Pregunta_Multiple.Visualizador_PreguntaMultiple import VisualizadorPreguntaMultiple
from LOGICA.Creador_Preguna_CheckBox.Visualizador_PreguntaCheckBox import VisualizadorPregunta_CheckBox
from LOGICA.Creador_Pregunta_Abierta.Visualizador_PreguntaAbierta import VisualizadorPregunta_Abierta

###############################################################
#  MIS LIBRERIAS...
##############################################################
from LOGICA.Creador_MisPaquetes.DataBaseCreadorPreguntas import DataBaseCreadorPreguntas
from LOGICA.Creador_Ventanas_Dialogo.ConfirmadorAccion import ConfirmadorAccion
from LOGICA.Creador_MisPaquetes.comportSelect_btnsImagen import comporSelec_btnsImagen
from LOGICA.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios



class EjecutadorCuestionario(QtWidgets.QWidget, Ui_Form):
    def __init__(self,nombreCuestionario="",nombreCreador="ANONIMO"):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

##############################################################################################################################
#  INCLUYENDO WIDGETS...
##############################################################################################################################
        #creando multiples ventanas...
        self.ventanas=[]
        self.listBotonesPreguntas=[]
        self.contadorPreguntas=0

        # creando multiples ventanas...
        self.ventanas = []
        self.ventanas.append( VisualizadorPreguntaBinaria() )  # pregunta binaria
        self.ventanas.append( VisualizadorPreguntaMultiple() ) #pregunta multiple
        self.ventanas.append( VisualizadorPregunta_CheckBox() ) #visualizador pregunta checkbox
        self.ventanas.append(  VisualizadorPregunta_Abierta() ) #visualizador de pregunta abierta...

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelPreguntas.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelPreguntas.setCurrentIndex(0)
        self.listWidget_panelPreguntas.showFullScreen()

        self.listBotonesPreguntas = []
        self.listIdPreguntas = []
        self.punteroPregunta = -1  # numero que no puede ser ningun puntero al incio

        self.btn_terminar.setVisible(False)
        self.btn_terminar.clicked.connect(self.preguntarSiQuiereTerminar)

        textoTerminador="Al termino del cuestionario, tu calificacion final sera mostrada "
        textoTerminador+="asi como las preguntas en las cuales erraste, de igual forma tu "
        textoTerminador+="calificacion final quedara registrada: ¿En realidad deseas terminar "
        textoTerminador+="el cuestionario?"
        fraseTerminadora="Estoy seguro de terminarlo"

        self.controlABSOLUTO_terminadorCuestionario=ConfirmadorAccion(textoTerminador,fraseTerminadora)
        self.controlABSOLUTO_terminadorCuestionario.accionConfirmada.connect(self.terminarCuestionario)

##############################################################################################################################
#  SCROLL DE PREGUNTAS...
##############################################################################################################################


        # Scroll Are
        # a Properties
        self.widgetHorizontal = QWidget()  # Widget that contains the collection of Vertical Box
        self.hbox = QHBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widgetHorizontal.setLayout(self.hbox)

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widgetHorizontal)




##############################################################################################################################
#  LEYENDO LAS BASES DATOS...
##############################################################################################################################

        self.nombreCuestionario=nombreCuestionario
        self.carpetaImagenes="IMAGENES_"+nombreCuestionario+"/"
        self.controlABSOLUTO_baseDatos=DataBaseCreadorPreguntas("MiCora")

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



        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_yoDijeElDijo = (self.btn_respondioYo,self.btn_respondioEl)
        self.listImagen_yoDijeElDijo= (RecursosCreadorCuestionarios.ICON_RESPONDI_YO,
                                       RecursosCreadorCuestionarios.ICON_RESPONDIO_EL,)
        self.controlABSLUTO_verRespuestas = comporSelec_btnsImagen(self.listBtnPunteros_yoDijeElDijo,
                                                self.listImagen_yoDijeElDijo)

        self.controlABSLUTO_verRespuestas.botonFuePresionado.connect(self.cambioVerRespuesta)
        self.controlABSLUTO_verRespuestas.botonPresionado(0)

        self.dejarDeOcultarElementosFinales(False)
        self.cuestionarioTerminado=False

        #Constantes de imagenes...
        self.pixmapImagen_respondioBIEN = QPixmap(RecursosCreadorCuestionarios.ICON_RESPONDIO_BIEN).scaled(65, 65, Qt.KeepAspectRatio,
                                                          Qt.SmoothTransformation)

        self.pixmapImagen_respondioMAL = QPixmap(RecursosCreadorCuestionarios.ICON_RESPONDIO_MAL).scaled(65, 65,
                                                                                                      Qt.KeepAspectRatio,
                                                                                                      Qt.SmoothTransformation)


    def cambioVerRespuesta(self,idBtnFuePresionado):
        self.controlABSLUTO_verRespuestas.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)
        if idBtnFuePresionado==1: #quiere ver la respuesta correcta...
            self.ventanas[self.punteroWidgetVisualizando].mostrarRespuestaCorrecta()
        else: #quiere ver su respuesta...
            self.ventanas[self.punteroWidgetVisualizando].mostrarRespuesta(self.listaRespuestas[self.punteroPregunta])




##############################################################################################################################
#  VISUALIZADOR DE PREGUNTA
##############################################################################################################################
    def dejarDeOcultarElementosFinales(self,estado):
        self.btn_respondioEl.setVisible(estado)
        self.bel_respondioEl.setVisible(estado)

        self.btn_respondioYo.setVisible(estado)
        self.bel_respondioYo.setVisible(estado)

        self.btn_terminar.setVisible(estado)
        self.bel_califFinal.setVisible(estado)
        self.bel_estadoPregunta.setVisible(estado)


    def desconectarBotones(self):
        for boton in self.listBotonesPreguntas:
            boton.clickBotonPregunta.disconnect()
            boton.clickBotonPregunta.connect(self.verRespuestas)

    def preguntarSiQuiereTerminar(self):
        self.controlABSOLUTO_terminadorCuestionario.show()

    def terminarCuestionario(self):
        self.listWidget_panelPreguntas.setEnabled(False)
        self.dejarDeOcultarElementosFinales(True)
        self.desconectarBotones() #desconectamos todos de la funcion...
        #Obteniendo calificaciones...
        puntosObtenidos=0
        puntosObtener=self.noPreguntas
        for x in self.listaCalificaciones:
            puntosObtenidos+=int(x)
        calificacion=int((puntosObtenidos/puntosObtener)*1000)
        calificacion=calificacion/10
        print("CALIFICACION...."+str(calificacion))

        calificacion=str(calificacion)+" %"
        self.btn_terminar.setText(calificacion)
        self.cambiarTam(self.btn_terminar, 20)
        self.btn_terminar.setEnabled(False)

        QMessageBox.question(self, 'Calificacion final',
                             "Obtuviste una calificacion:\n"
                             f"del {calificacion},respodiste bien \n"
                             f"{puntosObtenidos}/{puntosObtener} preguntas",
                            QMessageBox.Ok)

        self.verRespuestas(0) #viendo las respuestas apartir de la pregunta cero...
        self.cuestionarioTerminado=True


    def verRespuestas(self,noPregunta):
        self.controlABSLUTO_verRespuestas.botonPresionado(0) #siempre querra ver lo que el respondio...
        if self.punteroPregunta != noPregunta:
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
            self.scrollArea.ensureWidgetVisible(self.listBotonesPreguntas[self.punteroPregunta].botonPregunta)
            if self.listaCalificaciones[self.punteroPregunta]==True: #respondio bien..
                self.bel_estadoPregunta.setStyleSheet(f"border-image: url({RecursosCreadorCuestionarios.ICON_RESPONDIO_BIEN});")
            else: #respondio mal...
                self.bel_estadoPregunta.setStyleSheet(f"border-image: url({RecursosCreadorCuestionarios.ICON_RESPONDIO_MAL});")

            self.controlABSLUTO_verRespuestas.botonPresionado(0) #diremos que quisieron presionar el boton de ver
                                                                 #su respuesta...



    def verContenidoPregunta(self,noPregunta,verloNuevamente=False):
        self.controlABSLUTO_verRespuestas.botonPresionado(0) #siempre querra ver lo que el respondio...
        if self.punteroPregunta != noPregunta or verloNuevamente:
            if self.punteroWidgetVisualizando>-1:
                self.listaRespuestas[self.punteroPregunta]=self.ventanas[self.punteroWidgetVisualizando].getRespuesta()
                self.listaCalificaciones[self.punteroPregunta]=self.ventanas[self.punteroWidgetVisualizando].calificarRespuesta()

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
            self.scrollArea.ensureWidgetVisible(self.listBotonesPreguntas[self.punteroPregunta].botonPregunta)
            if self.punteroPregunta==(self.noPreguntas-1) or self.cuestionarioTerminado: #si ya van en la ultima pregunta
                self.btn_terminar.setVisible(True)
            else:
                self.btn_terminar.setVisible(False)

    def verNextPregunta(self):
        if self.punteroPregunta < (self.noPreguntas - 1):
            if not(self.cuestionarioTerminado):
                self.verContenidoPregunta(self.punteroPregunta+1)
            else:
                self.verRespuestas(self.punteroPregunta + 1)


    def verPrevPregunta(self):
        if self.punteroPregunta>=1:
            if not(self.cuestionarioTerminado):
                self.verContenidoPregunta(self.punteroPregunta-1)
            else:
                self.verRespuestas(self.punteroPregunta-1)







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
        self.hbox.addWidget(botonPregunta,alignment=QtCore.Qt.AlignVCenter)


    def cambiarTam(self,editText,newValor):
        # Cambiando el tamaño
        font = QtGui.QFont()
        font.setPointSize(int(newValor))
        editText.setFont(font)



    def closeEvent(self, event):
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
    application = EjecutadorCuestionario()
    application.show()
    app.exec()
    #sys.exit(app.exec())


#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke















































'''
#Abriendo o crenado conexion
miConexion=sqlite3.connect("MiCora.db")

#Puntero de la base...
miCursor=miConexion.cursor()
#SELECT * ==>NOS DEVUELVE TODOS LOS PRODUCTOS...
miCursor.execute("SELECT  ID  FROM  TABLA_PREGUNTAS")

variosProductos=miCursor.fetchall()#devuelve una lista con
                                   #todos los registros que devuelve
                                   #la instruccion sql

controlABSOLUTO_baseDatos=DataBaseCreadorPreguntas("MiCora")

#controlABSOLUTO_baseDatos.getData(1)
listaIDs=[]
#obteniendo todos los id de las preguntas...
for x in variosProductos:
    id=int(x[0])
    listaIDs.append(id)
    print(controlABSOLUTO_baseDatos.getData(id))

print(listaIDs)
#print(variosProductos)
#Confirmamos los cambios...
miConexion.commit()
miConexion.close()








    def agregarPregunta(self):
        widget = QWidget()
        widget.setMinimumSize(60,75)
        widget.setMaximumSize(60,75)
        gridLayout = QGridLayout(widget)  # Set the checkbox in the layer
        botonCerrar = QPushButton()
        a = "QPushButton{border-image:url(" + self.IMAGEN_ELIMINAR + ");}"
        b = "QPushButton:hover{border-image:url(" + self.IMAGEN_ELIMINAR_2 + ");}"
        c = "QPushButton:pressed{border-image:url(" + self.IMAGEN_ELIMINAR + ");}"
        botonCerrar.setStyleSheet(a + b + c)
        botonCerrar.setMaximumSize(15,15)
        botonCerrar.setMinimumSize(15,15)
        botonPregunta=QPushButton()
        botonPregunta.setMaximumSize(50,50)
        botonPregunta.setMinimumSize(50,50)
        nuevoBotonPregunta=BotonPregunta(self.contadorPreguntas,botonPregunta,botonCerrar)
        self.listBotonesPreguntas.append(nuevoBotonPregunta)
        nuevoBotonPregunta.clickBotonPregunta.connect(self.verContenidoPregunta)
        nuevoBotonPregunta.suHoraMorir.connect(self.eliminarPregunta)
        nuevoBotonPregunta.darIdBotonPregunta()  # hacer como que lo selecciona...


        # addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
        gridLayout.addWidget(botonCerrar, 0, 0, 1, -1, alignment=QtCore.Qt.AlignRight)
        gridLayout.addWidget(botonPregunta,1, 0, -1, -1,alignment=QtCore.Qt.AlignHCenter)
        gridLayout.setContentsMargins(0, 0, 0, 0)  # Set the zero padding
        self.vbox.addWidget(widget,alignment=QtCore.Qt.AlignHCenter)
        self.contadorPreguntas += 1

'''

