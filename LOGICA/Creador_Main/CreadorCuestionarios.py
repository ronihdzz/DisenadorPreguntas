import sqlite3
from LOGICA.Creador_MisPaquetes.DataBaseCreadorPreguntas import DataBaseCreadorPreguntas

from PyQt5.QtCore import QTimer
from PyQt5 import QtWidgets,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QGridLayout
from PyQt5.QtCore import Qt, pyqtSignal,QObject
from PyQt5.QtWidgets import  QMessageBox
import datetime


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

##############################################################################################################################
#  SCROLL DE PREGUNTAS...
##############################################################################################################################

        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll_barra.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setWidget(self.widget)

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
        for _ in range(self.noPreguntas):
            self.listaRespuestas.append(None)

        self.btn_next.clicked.connect(self.verNextPregunta)
        self.btn_prev.clicked.connect(self.verPrevPregunta)

        self.crearBotonesPreguntas()
        self.punteroWidgetVisualizando=-1



##############################################################################################################################
#  VISUALIZADOR DE PREGUNTA
##############################################################################################################################
    def crearBotonesPreguntas(self):
        for x in range(self.noPreguntas):
            self.agregarPregunta(x)

    def agregarPregunta(self,noBoton):
        botonCerrar = QPushButton()
        botonCerrar.setMaximumSize(15,15)
        botonCerrar.setMinimumSize(15,15)
        botonPregunta=QPushButton()
        botonPregunta.setMaximumSize(50,50)
        botonPregunta.setMinimumSize(50,50)
        nuevoBotonPregunta=BotonPregunta(noBoton,botonPregunta)
        self.listBotonesPreguntas.append(nuevoBotonPregunta)
        nuevoBotonPregunta.clickBotonPregunta.connect(self.verContenidoPregunta)
        self.vbox.addWidget(botonPregunta,alignment=QtCore.Qt.AlignHCenter)


    def verContenidoPregunta(self,noPregunta):
        if self.punteroPregunta != noPregunta:
            if self.punteroWidgetVisualizando>-1:
                self.listaRespuestas[self.punteroPregunta]=self.ventanas[self.punteroWidgetVisualizando].getRespuesta()

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
            self.scroll_barra.ensureWidgetVisible(self.listBotonesPreguntas[self.punteroPregunta].botonPregunta)

    def verNextPregunta(self):
        if self.punteroPregunta< (self.noPreguntas-1):
            self.verContenidoPregunta(self.punteroPregunta+1)

    def verPrevPregunta(self):
        if self.punteroPregunta>=1:
            self.verContenidoPregunta(self.punteroPregunta-1)




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

