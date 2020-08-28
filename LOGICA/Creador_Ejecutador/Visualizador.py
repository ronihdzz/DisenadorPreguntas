from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import datetime

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from DISENO.Creador_Ejecutador.VisualizadorPreguntas_d import Ui_Form
from LOGICA.Creador_Pregunta_Binaria.Visualizador_PreguntaBinaria import VisualizadorPreguntaBinaria
from LOGICA.Creador_Pregunta_Multiple.Visualizador_PreguntaMultiple import VisualizadorPreguntaMultiple
from LOGICA.Creador_Preguna_CheckBox.Visualizador_PreguntaCheckBox import VisualizadorPregunta_CheckBox
from LOGICA.Creador_Pregunta_Abierta.Visualizador_PreguntaAbierta import VisualizadorPregunta_Abierta

###############################################################
#  MIS LIBRERIAS...
##############################################################



class VisualizadorPreguntas(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        # creando multiples ventanas...
        self.ventanas = []
        self.ventanas.append( VisualizadorPreguntaBinaria() )  # pregunta binaria
        self.ventanas.append( VisualizadorPreguntaMultiple() ) #pregunta multiple
        self.ventanas.append( VisualizadorPregunta_CheckBox() ) #visualizador pregunta checkbox
        self.ventanas.append(  VisualizadorPregunta_Abierta() ) #visualizador de pregunta abierta...

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()


        #Qtimer().......
        self.timer = QTimer()
        self.timer.timeout.connect(self.cuentaRegresivaPregunta)
        self.pausarTimePregunta=True
        self.punteroWidgetTipoPregunta=-1

        self.btn_next.clicked.connect(self.calificarRespuesta)


        datosPregunta,datosRespuesta=self.getDataPruebaPregunta_binaria()
        self.visualizarPregunta(0,datosPregunta,datosRespuesta)


##############################################################################################################################
#  VISUALIZADOR DE PREGUNTA
##############################################################################################################################


    def visualizarPregunta(self,tipoRespuesta,datosPregunta,datosRespuesta):
        tiempoPregunta=datosPregunta["TIEMPO_SEGUNDOS"]
        #PONIENDO TIEMPOS:
        self.punteroTimePregunta = datetime.timedelta(seconds=tiempoPregunta)
        self.lcdNum_timePregunta.display(str(self.punteroTimePregunta) )
        #Iniciando cuenta regresiva...
        self.pausarTimePregunta=False
        self.iniciarCuentaRegresiva()

        self.punteroWidgetTipoPregunta=tipoRespuesta
        self.listWidget_panelVersion.setCurrentIndex(tipoRespuesta)
        self.ventanas[tipoRespuesta].abrirPregunta(datosPregunta,datosRespuesta)

    def calificarRespuesta(self):
        estadoRespuesta=self.ventanas[self.punteroWidgetTipoPregunta].calificarRespuesta()
        if estadoRespuesta==True:
            self.bel_estadoRespuesta.setText("Respuesta correcta")
        else:
            self.bel_estadoRespuesta.setText("Respuesta incorrecta")

    def limpiarPregunta(self):
        if self.punteroWidgetTipoPregunta>=0:
            self.ventanas[self.punteroWidgetTipoPregunta].limpiarWidget()

    def closeEvent(self, event):
        self.terminarCuentaRegresiva()
        event.accept()

##############################################################################################################################
#  C U E N T A     R E G R E S I V A  :
##############################################################################################################################

    def cuentaRegresivaPregunta(self):
        #Si no esta pausado el tiempo de la pregunta...
        if not(self.pausarTimePregunta):
            if(self.punteroTimePregunta.seconds>0):
                self.punteroTimePregunta=self.punteroTimePregunta-datetime.timedelta(seconds=1)
                self.lcdNum_timePregunta.display(str(self.punteroTimePregunta))
            else:
                self.pausarTimePregunta=True
                self.bel_estadoRespuesta.setText("TIEMPO AGOTADO :'v ")

    def iniciarCuentaRegresiva(self):
        #le decimos cada cuando producira un cambio para que active el
        #evento timeout.connect  ....
        self.timer.start(1000)

    def terminarCuentaRegresiva(self):
        self.timer.stop()

    def reiniciarTimePregunta(self):
        self.punteroTimePregunta = datetime.timedelta(seconds=self.sPregunta)
        self.lcdNum_timePregunta.display(str(self.punteroTimePregunta) )



##############################################################################################################################
#  DATOS DE PRUEBA...
##############################################################################################################################

    def getDataPruebaPregunta_binaria(self):
        datosPregunta = {
            "GRADO_IMAGENES": 1,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 60,
            "TEXTO_PREGUNTA": "¿Roni es gay?",
            "IMAGEN_PREGUNTA": "roni.png",
            "TAMANO_PREGUNTA": 30,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 70,
            "POSICION_RESPUESTA": 1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR": 0,  # 0=todas 1=cualquiera
            "RESPUESTAS": "1,1"
        }

        datosRespuesta = {
            "TEXTO_RESPA": "CIERTO",
            "TEXTO_RESPB": "FALSO",
        }

        return datosPregunta, datosRespuesta

    def getDataPruebaPregunta_multiple(self):
        datosPregunta = {
            "GRADO_IMAGENES": 3,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 60,
            "TEXTO_PREGUNTA": "¿Actitudes de Roni?",
            "IMAGEN_PREGUNTA": "roni.png",
            "TAMANO_PREGUNTA": 30,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 20,
            "POSICION_RESPUESTA": 1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR": 1,  # 0=todas 1=cualquiera
            "RESPUESTAS": "0,1,0,1"
        }

        datosRespuesta = {
            "TEXTO_RESPA": "Lealtad",
            "IMAGEN_RESPA": "",
            "TEXTO_RESPB": "Respto",
            "IMAGEN_RESPB": "",
            "TEXTO_RESPC": "Pasion",
            "IMAGEN_RESPC": "",
            "TEXTO_RESPD": "Perserverancia",
            "IMAGEN_RESPD": ""
        }
        return datosPregunta, datosRespuesta

    def getDataPruebaPregunta_checkBox(self):
        datosPregunta = {
            "GRADO_IMAGENES": 1,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 60,
            "TEXTO_PREGUNTA": "¿Quien es Roni Hernandez?",
            "IMAGEN_PREGUNTA": "roni.png",
            "TAMANO_PREGUNTA": 15,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 15,
            "POSICION_RESPUESTA": 1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR": 0,  # 0=todas 1=cualquiera  ya que deben elegirse todas las opcciones correctas
            "RESPUESTAS": "0,0,1,0"
        }

        datosRespuesta = {
            "TEXTO_ITEMS": "jorge,dilan,roni,gaby"
        }

        return datosPregunta, datosRespuesta

    def getDataPruebaPregunta_abierta(self):
        datosPregunta = {
            "GRADO_IMAGENES": 1,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 70,
            "TEXTO_PREGUNTA": "¿Con cual sentencia se imprime en python?",
            "IMAGEN_PREGUNTA": "roni.png",
            "TAMANO_PREGUNTA": 25,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 0, #no esta definida...
            "POSICION_RESPUESTA": 1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR": 0,  # 0=preguntasString  1=preguntasNumero
            "RESPUESTAS": "print"
        }
        datosRespuesta = None
        return datosPregunta, datosRespuesta


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = VisualizadorPreguntas()
    application.show()
    app.exec()
    #sys.exit(app.exec())




