from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...


from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.VisualizadorContenedor_d import Ui_Form
from PyQt5.QtCore import QTimer,QTime


from menuTipoPreguntas import menuTipoPreguntas
from comportSelectBtnsRespG import comporSelecBtnsResp
import datetime

#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from PreguntaBinariaImagen_0 import PreguntaBinariaImagen_0
from PreguntaBinariaImagen_50 import PreguntaBinariaImagen_50


from comporSelect_btnsImagen import comporSelec_btnsImagen
from comportEditTextEdit import comportEditTextEdit
from comportAutoguardado_textEdit import comportAutoguardado_textEdit
from PyQt5.QtWidgets import  QMessageBox
import numpy as np
from PropiedadesPregunta import PropiedadesPregunta
import os
from PyQt5.QtCore import Qt, pyqtSignal, QFile
from PyQt5.QtGui import QIcon, QPixmap

from comportSelectBtnsRespG import comporSelecBtnsResp
from PreguntasMultiplesImagen_0 import PreguntasMultiplesImagen_0
from PreguntasMultiplesImagen_50 import PreguntasMultiplesImagen50
from PreguntasMultiplesImagen_75 import PreguntasMultiplesImagen75
from PreguntasMultiplesImagen_100 import PreguntasMultiplesImagen100


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class VisualizadorPreguntaMultiple(QtWidgets.QWidget, Ui_Form,PropiedadesPregunta):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        PropiedadesPregunta.__init__(self)
        self.setupUi(self)
        # creando multiples ventanas...
        self.ventanas = []
        self.ventanas.append(PreguntasMultiplesImagen_0())  # pregunta binaria
        self.ventanas.append(PreguntasMultiplesImagen50())  # preguntas multiples
        self.ventanas.append(PreguntasMultiplesImagen75())
        self.ventanas.append(PreguntasMultiplesImagen100())  # preguntas especificas
        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()


        self.PROPIEDADES_PREGUNTA={}
        self.PROPIEDADES_RESPUESTA={}

        self.DIREC_IMAGENES="HOLA/"

        self.COLOR_OR = "#5DD1D6"
        self.COLOR_AND = "#F51E8C"
        self.respuestaUsuario=[]

####################################################################################################################################
#       C O N T R O L    D E     B O T O N E S :
####################################################################################################################################

        # CREANDO UNA MATRIZ DE PUROS BOTONES...
        renglonBotones = np.array([[self.ventanas[0].btn_respA, self.ventanas[0].btn_respB,
                                    self.ventanas[0].btn_respC, self.ventanas[0].btn_respD]])
        self.matrizBotonesRespuesta = renglonBotones
        for i in range(1, len(self.ventanas)):
            # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
            renglonBotones = np.array([[self.ventanas[i].btn_respA, self.ventanas[i].btn_respB,
                                        self.ventanas[i].btn_respC, self.ventanas[i].btn_respD]])
            self.matrizBotonesRespuesta = np.append(self.matrizBotonesRespuesta, renglonBotones, axis=0)
        self.controlABSOLUTO_botones = comporSelecBtnsResp(self.matrizBotonesRespuesta, BORDER_RADIUS="5")




    def calificarRespuesta(self):
        estadoRespuesta=False

        if self.formaEvaluar==0: #osea debe elegir todas las correctas...
            self.respuestaUsuario = self.controlABSOLUTO_botones.dameTodoLoQueRespondio()
            if self.respuestaUsuario==self.respuestasCorrectas:
                estadoRespuesta=True
        else: #solo debe seleccionara una bien..
            self.respuestaUsuario = self.controlABSOLUTO_botones.dameLaRespuestaEscogio()
            if self.respuestaUsuario>=0:#ya que el valor inciial es -1
                if self.respuestasCorrectas[self.respuestaUsuario]==1:
                    estadoRespuesta=True
        return estadoRespuesta


    def abrirPregunta(self,datosPregunta,datosRespuesta):
        self.PROPIEDADES_PREGUNTA=datosPregunta
        self.PROPIEDADES_RESPUESTA=datosRespuesta

        noWidgetAbrir=self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"]
        self.listWidget_panelVersion.setCurrentIndex(noWidgetAbrir)

        tiempoPregunta=self.PROPIEDADES_PREGUNTA["TIEMPO_SEGUNDOS"]
        #PONIENDO TIEMPOS:

        textoPregunta=self.PROPIEDADES_PREGUNTA["TEXTO_PREGUNTA"]
        self.ventanas[noWidgetAbrir].txtEdit_preg.setText(textoPregunta)
        self.ventanas[noWidgetAbrir].txtEdit_preg.setReadOnly(True)


        # IMAGEN_PREGUNTA...
        if noWidgetAbrir>0: #Significa que es una pregunta con respuestas imagenes...
            self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.IMAGENES_BLOQUEDAS = False
            self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.ponerEnDafultTodasLabel()
            if noWidgetAbrir==1 or noWidgetAbrir==3: #preguntaImagen 50% or preguntaImagen 100%
                # IMAGEN_PREGUNTA...
                imagenPregunta=self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]
                #Cagaremos la imagen pero no la respuesta...
                i=imagenPregunta
                if not(i==None or i==False or i=="" or i=="NULL"):
                    imagenPregunta = self.DIREC_IMAGENES + imagenPregunta
                self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.escogioImagen(0, False, imagenPregunta)
            if noWidgetAbrir>1:#preguntaImagen 50% or preguntaImagen 75%
                respuestas = ["A", "B", "C", "D"]
                listaRespuestaImagen = [self.PROPIEDADES_RESPUESTA["IMAGEN_RESP" + letra] for letra in respuestas ]
                listaRespuestaImagen=[ self.DIREC_IMAGENES+x if not(x==None or x==False or x=="" or x=="NULL") else x for x in listaRespuestaImagen]
                contador=0
                if noWidgetAbrir==3: #si la widget que fue presionada fue la de...
                                          #100% preguntas...
                    contador=1
                print(listaRespuestaImagen)
                for i in range(len(respuestas)):
                    self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.escogioImagen(contador+i, False,listaRespuestaImagen[i])
            self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.IMAGENES_BLOQUEDAS=True

        tamPregunta=self.PROPIEDADES_PREGUNTA["TAMANO_PREGUNTA"]
        self.cambiarTam(self.ventanas[noWidgetAbrir].txtEdit_preg,tamPregunta)

        posPregunta=self.PROPIEDADES_PREGUNTA["POSICION_PREGUNTA"]
        self.cambiarPosEditsText(self.ventanas[noWidgetAbrir].txtEdit_preg,posPregunta)

        #RESPUESTAS...
        tamRespuesta=self.PROPIEDADES_PREGUNTA["TAMANO_RESPUESTA"]
        posRespuesta=self.PROPIEDADES_PREGUNTA["POSICION_RESPUESTA"]
        #FORMA DE EVALUAR...
        formaEvaluar=self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"]

        self.controlABSOLUTO_botones.setAllRespuestas([0, 0,0,0])#todas las respuestas desmarcadas
        if formaEvaluar==0: #seleccionar todos las respuestas correctas
            self.controlABSOLUTO_botones.seleccionMultiple=True
            self.controlABSOLUTO_botones.setColor(self.COLOR_AND)
        else:#solo debe seleccionar una respuesta correcta
            self.controlABSOLUTO_botones.seleccionMultiple=False
            self.controlABSOLUTO_botones.setColor(self.COLOR_OR)

        respuestasCorrectas=self.PROPIEDADES_PREGUNTA["RESPUESTAS"]
        respuestasCorrectas=[int(x) for x in respuestasCorrectas.split(",")]

        #RESPUESTAS...
        respuestas = ["A", "B","C","D"]
        listaRespuestaText = [self.PROPIEDADES_RESPUESTA["TEXTO_RESP" + letra] for letra in respuestas]
        #poniendo respuesta en cada edit text...
        listaTxtRespuestas=[self.ventanas[noWidgetAbrir].txtEdit_respA,
                            self.ventanas[noWidgetAbrir].txtEdit_respB,
                            self.ventanas[noWidgetAbrir].txtEdit_respC,
                            self.ventanas[noWidgetAbrir].txtEdit_respD]

        for i in range(len(listaTxtRespuestas)):
            #Poniendo el texto respectivo a cada uno
            txtEditar=listaTxtRespuestas[i]
            txtEditar.setText(listaRespuestaText[i])
            self.cambiarTam(txtEditar,tamRespuesta)
            self.cambiarPosEditsText(txtEditar,posRespuesta)
            txtEditar.setReadOnly(True)

        #ATRIBUTOS QUE SI UTILIZARE...
        self.noWidgetAbrir=noWidgetAbrir
        self.respuestasCorrectas=respuestasCorrectas
        self.formaEvaluar=formaEvaluar


    def limpiarWidget(self):
        #Limpiaremos los datos que quedaran resagados pregunta con pregunta....
        self.controlABSOLUTO_botones.setAllRespuestas([0,0,0,0]) #ponemos todas desmarcadas...
        if self.noWidgetAbrir>0: #1,2,3
            self.ventanas[self.noWidgetAbrir].controlABSOLUTO_labelImagen.ponerEnDafultTodasLabel()

    def cambiarTam(self,editText,newValor):
        # Cambiando el tamaño
        font = QtGui.QFont()
        font.setPointSize(int(newValor))
        editText.setFont(font)

    def cambiarPosEditsText(self,editText,newPosicion):
        if newPosicion == 0:
            editText.setAlignment(Qt.AlignLeft)
        elif newPosicion == 1:
            editText.setAlignment(Qt.AlignHCenter)
        elif newPosicion == 2:
            editText.setAlignment(Qt.AlignRight)

##############################################################################################################################
#  DATOS DEFAULT...
##############################################################################################################################

    def datosDefault(self):
        datosPregunta={
            "GRADO_IMAGENES": 3,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 60,
            "TEXTO_PREGUNTA": "¿Actitudes de Roni?",
            "IMAGEN_PREGUNTA": "roni.png",
            "TAMANO_PREGUNTA": 30,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 20,
            "POSICION_RESPUESTA":1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR":1,  # 0=todas 1=cualquiera
            "RESPUESTAS": "0,1,1,1"
        }

        datosRespuesta={
            "TEXTO_RESPA": "Lealtad",
            "IMAGEN_RESPA":"",
            "TEXTO_RESPB": "Respto",
            "IMAGEN_RESPB": "",
            "TEXTO_RESPC": "Pasion",
            "IMAGEN_RESPC": "",
            "TEXTO_RESPD": "Perserverancia",
            "IMAGEN_RESPD": ""
        }
        return datosPregunta,datosRespuesta


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = VisualizadorPreguntaMultiple()
    application.show()
    app.exec()
    #sys.exit(app.exec())




