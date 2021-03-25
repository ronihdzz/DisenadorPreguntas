from PyQt5 import QtWidgets,QtGui,Qt
import numpy as np
from PyQt5.QtCore import Qt

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Pregunta_Binaria.VisualizadorBinaria_d import Ui_Form
from CUERPO.LOGICA_creador.Creador_Pregunta_Binaria.PreguntaBinariaImagen_0 import PreguntaBinariaImagen_0
from CUERPO.LOGICA_creador.Creador_Pregunta_Binaria.PreguntaBinariaImagen_50 import PreguntaBinariaImagen_50

###############################################################
#  MIS LIBRERIAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.comportSelectBtnsRespG import comporSelecBtnsResp

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class VisualizadorPreguntaBinaria(QtWidgets.QWidget, Ui_Form):
    def __init__(self,nombreCreador="",direc_carpetaImagenes=""):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.DIREC_IMAGENES=direc_carpetaImagenes

        # creando multiples ventanas...
        self.ventanas = []
        self.ventanas.append( PreguntaBinariaImagen_0() )  # pregunta binaria
        self.ventanas.append( PreguntaBinariaImagen_50(nombreCreador,direc_carpetaImagenes) )  # preguntas multiples

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()


        self.PROPIEDADES_PREGUNTA={}
        self.PROPIEDADES_RESPUESTA={}

        datosPregunta,datosRespuesta=self.datosDefault()

        self.COLOR_OR = "#5DD1D6"
        self.COLOR_AND = "#F51E8C"
        self.respuestaUsuario=[]

####################################################################################################################################
#       C O N T R O L    D E     B O T O N E S :
####################################################################################################################################
        # En este apartado le daremo un comportamiento a las respuestas botones,de tal manera
        # que cuando hagan click en ellos,nos avisen y aparte registre dichas respuestas...
        # CREANDO UNA MATRIZ DE PUROS BOTONES...
        renglonBotones = np.array([[self.ventanas[0].btn_respA, self.ventanas[0].btn_respB]])
        self.matrizBotonesRespuesta = renglonBotones
        for i in range(1, len(self.ventanas)):
            # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
            renglonBotones = np.array([[self.ventanas[i].btn_respA, self.ventanas[i].btn_respB]])
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
            if self.respuestaUsuario> -1:#ya que el valor inciial es -1
                if self.respuestasCorrectas[self.respuestaUsuario]==1:
                    estadoRespuesta=True

        return estadoRespuesta

    def getRespuesta(self):
        if self.formaEvaluar==0: #osea debe elegir todas las correctas...
            self.respuestaUsuario = self.controlABSOLUTO_botones.dameTodoLoQueRespondio()
            return str(self.respuestaUsuario)[1:-1] # con esto quitamos corchetes...
                                                    # [0,0,0,0]  0,0,0,0
        else: #solo debe seleccionara una bien..
            self.respuestaUsuario = self.controlABSOLUTO_botones.dameLaRespuestaEscogio()
            respuesta=[0,0] #son dos porque es una pregunta binaria...
            if self.respuestaUsuario> -1:#ya que el valor inciial es -1
                respuesta[self.respuestaUsuario]=1
            return str(respuesta)[1:-1]

    def mostrarRespuestaCorrecta(self):
        respuestaCorrecta=self.PROPIEDADES_PREGUNTA["RESPUESTAS"]
        self.mostrarRespuesta(respuestaCorrecta)

    def mostrarRespuesta(self,respuesta):
        self.controlABSOLUTO_botones.setAllRespuestas([0,0])  # primero limpiamos,luego mostramos
        if respuesta!=None and respuesta!= "":
            respuestaUsuario = [int(x) for x in respuesta.split(",")]
            self.controlABSOLUTO_botones.setAllRespuestas(respuestaUsuario)

##############################################################################################################################
#  C U E N T A     R E G R E S I V A  :
##############################################################################################################################
    def abrirPregunta(self,datosPregunta,datosRespuesta,respuestaUsuario=None):
        self.PROPIEDADES_PREGUNTA=datosPregunta
        self.PROPIEDADES_RESPUESTA=datosRespuesta

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

        #RESPUESTAS...
        tamRespuesta=self.PROPIEDADES_PREGUNTA["TAMANO_RESPUESTA"]
        posRespuesta=self.PROPIEDADES_PREGUNTA["POSICION_RESPUESTA"]
        #FORMA DE EVALUAR...
        formaEvaluar=self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"]

        self.controlABSOLUTO_botones.setAllRespuestas([0,0])#todas las respuestas desmarcadas
        self.controlABSOLUTO_botones.ultimoBotonPresionado=-1
        if formaEvaluar==0: #seleccionar todos las respuestas correctas
            self.controlABSOLUTO_botones.seleccionMultiple=True
            self.controlABSOLUTO_botones.setColor(self.COLOR_AND)
        else:#solo debe seleccionar una respuesta correcta
            self.controlABSOLUTO_botones.seleccionMultiple=False
            self.controlABSOLUTO_botones.setColor(self.COLOR_OR)


        respuestasCorrectas=self.PROPIEDADES_PREGUNTA["RESPUESTAS"]
        respuestasCorrectas=[int(x) for x in respuestasCorrectas.split(",")]

        #RESPUESTAS...
        respuestas = ["A", "B"]
        listaRespuestaText = [self.PROPIEDADES_RESPUESTA["TEXTO_RESP" + letra] for letra in respuestas]
        #poniendo respuesta en cada edit text...
        listaTxtRespuestas=[self.ventanas[noWidgetAbrir].txtEdit_respA,
                            self.ventanas[noWidgetAbrir].txtEdit_respB]

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

        if respuestaUsuario!=None:
            respuestaUsuario=[int(x) for x in respuestaUsuario.split(",")]
            self.controlABSOLUTO_botones.setAllRespuestas(respuestaUsuario)



    def limpiarWidget(self):
        #Limpiaremos los datos que quedaran resagados pregunta con pregunta....
        #self.controlABSOLUTO_botones.setAllRespuestas([0,0]) #ponemos todas desmarcadas...
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





    def datosDefault(self):
        datosPregunta={
            "GRADO_IMAGENES": 1,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 60,
            "TEXTO_PREGUNTA": "¿Roni es gay?",
            "IMAGEN_PREGUNTA": "roni.png",
            "TAMANO_PREGUNTA": 30,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 70,
            "POSICION_RESPUESTA":1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR":0,  # 0=todas 1=cualquiera
            "RESPUESTAS": "1,1"
        }

        datosRespuesta={
            "TEXTO_RESPA":"CIERTO",
            "TEXTO_RESPB":"FALSO",
        }

        return datosPregunta,datosRespuesta


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = VisualizadorPreguntaBinaria()
    application.show()
    app.exec()
    #sys.exit(app.exec())




