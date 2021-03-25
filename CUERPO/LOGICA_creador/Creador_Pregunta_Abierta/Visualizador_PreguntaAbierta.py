from PyQt5 import QtWidgets,QtGui,Qt
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QDoubleValidator,QRegExpValidator

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Pregunta_Abierta.VisualizadorAbierto_d import Ui_Form
from CUERPO.LOGICA_creador.Creador_Pregunta_Abierta.PreguntaAbiertaImagen_0  import PreguntaAbiertaImagen_0
from CUERPO.LOGICA_creador.Creador_Pregunta_Abierta.PreguntaAbiertaImagen_50 import PreguntaAbiertaImagen_50

###############################################################
#  MIS LIBRERIAS...
##############################################################

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class VisualizadorPregunta_Abierta(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self,nombreCreador="",direc_carpetaImagenes=""):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.DIREC_IMAGENES=direc_carpetaImagenes

        self.ventanas = []
        self.ventanas.append( PreguntaAbiertaImagen_0() )  # pregunta binaria
        self.ventanas.append( PreguntaAbiertaImagen_50(nombreCreador,direc_carpetaImagenes) )  # preguntas multiples

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()

        self.LIMITE_CARACTERES=30
        self.lineEdit_respuesta.setMaxLength(self.LIMITE_CARACTERES)
        self.lineEdit_respuesta.textChanged.connect(lambda x: self.bel_noChars.setText( str(len(self.lineEdit_respuesta.text()))) )

###########################################################################################################################
#
#
#       M    E     T     O     D     O     S    :
#
#
##############################################################################################################################

##############################################################################################################################
#  M E T O D O S     VISUALIZADOR...
##############################################################################################################################

    def calificarRespuesta(self):
        estadoRespuesta=False
        if self.lineEdit_respuesta.text()==self.respuestasCorrectas:
            estadoRespuesta=True
        return estadoRespuesta

    def getRespuesta(self):
        return self.lineEdit_respuesta.text()

    def mostrarRespuestaCorrecta(self):
        respuestaCorrecta=self.PROPIEDADES_PREGUNTA["RESPUESTAS"]
        self.mostrarRespuesta(respuestaCorrecta)

    def mostrarRespuesta(self, respuesta):
        if respuesta!=None:
            self.lineEdit_respuesta.setText(respuesta)


    def limpiarWidget(self):
        if self.noWidgetAbrir>0: #1,2,3
            self.ventanas[self.noWidgetAbrir].controlABSOLUTO_labelImagen.ponerEnDafultTodasLabel()


    def abrirPregunta(self, datosPregunta, datosRespuesta,respuestaUsuario=None):
        self.PROPIEDADES_PREGUNTA = datosPregunta
        self.PROPIEDADES_RESPUESTA = datosRespuesta
        # P R E G U N T A   :
        # GRADO_IMAGENES...

        noWidgetAbrir=self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"]
        self.listWidget_panelVersion.setCurrentIndex(noWidgetAbrir)

        tiempoPregunta=self.PROPIEDADES_PREGUNTA["TIEMPO_SEGUNDOS"]

        textoPregunta=self.PROPIEDADES_PREGUNTA["TEXTO_PREGUNTA"]
        self.ventanas[noWidgetAbrir].txtEdit_preg.setText(textoPregunta)
        self.ventanas[noWidgetAbrir].txtEdit_preg.setReadOnly(True)

        imagenPregunta=self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]

        # IMAGEN_PREGUNTA...
        if noWidgetAbrir>0: #Significa que es una pregunta con respuestas imagenes...
            self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.IMAGENES_BLOQUEDAS=False
            self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.ponerEnDafultTodasLabel()
            if imagenPregunta!="" and imagenPregunta!=None and imagenPregunta!=False:
                imagenPregunta = self.DIREC_IMAGENES + imagenPregunta
                self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.escogioImagen(0,False,imagenPregunta)
            self.ventanas[noWidgetAbrir].controlABSOLUTO_labelImagen.IMAGENES_BLOQUEDAS=True


        tamPregunta=self.PROPIEDADES_PREGUNTA["TAMANO_PREGUNTA"]
        self.cambiarTam(self.ventanas[noWidgetAbrir].txtEdit_preg,tamPregunta)

        posPregunta=self.PROPIEDADES_PREGUNTA["POSICION_PREGUNTA"]
        self.cambiarPosEditsText(self.ventanas[noWidgetAbrir].txtEdit_preg,posPregunta)

        #FORMA DE EVALUAR...
        formaEvaluar=self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"]#esta siempre sera 0,(AND)....

        if formaEvaluar == 0:  # respuesta string....
            self.bel_noChars.setText("0")
            self.lineEdit_respuesta.setText("")
            validator = QRegExpValidator(QRegExp("[^\n  ]{1," + str(self.LIMITE_CARACTERES) + "}"))
            self.lineEdit_respuesta.setValidator(validator)
        else:  # respuesta double..
            self.bel_noChars.setText("0")
            self.lineEdit_respuesta.setText("")
            self.lineEdit_respuesta.setValidator(QDoubleValidator())

        # RESPUESTAS...
        respuestasCorrectas = self.PROPIEDADES_PREGUNTA["RESPUESTAS"]

        #Una ayuda para el que responde...
        noCaracteresResp=len(respuestasCorrectas)
        self.bel_maxChars.setText(str(noCaracteresResp))

        #ATRIBUTOS QUE SI UTILIZARE...
        self.noWidgetAbrir=noWidgetAbrir
        self.respuestasCorrectas=respuestasCorrectas
        self.formaEvaluar=formaEvaluar

        if respuestaUsuario!=None:
            self.lineEdit_respuesta.setText(respuestaUsuario)


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
        datosPregunta = {
            "GRADO_IMAGENES": 0,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 60,
            "TEXTO_PREGUNTA": "",
            "IMAGEN_PREGUNTA": "",
            "TAMANO_PREGUNTA": 15,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 0, #no esta definida...
            "POSICION_RESPUESTA": 1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR": 0,  # 0=preguntasString  1=preguntasNumero
            "RESPUESTAS": ""
        }
        datosRespuesta = None
        return datosPregunta, datosRespuesta

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = VisualizadorPregunta_Abierta()
    application.show()
    app.exec()
    #sys.exit(app.exec())




