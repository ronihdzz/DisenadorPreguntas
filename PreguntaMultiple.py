from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiples_d import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas
from comportSelectBtnsRespG import comporSelecBtnsResp


#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from PreguntasMultiplesImagen_0 import PreguntasMultiplesImagen_0
from PreguntasMultiplesImagen_50 import PreguntasMultiplesImagen50
from PreguntasMultiplesImagen_75 import PreguntasMultiplesImagen75
from PreguntasMultiplesImagen_100 import PreguntasMultiplesImagen100
from comporSelect_btnsImagen import comporSelec_btnsImagen
from comportEditTextEdit import comportEditTextEdit
from comportAutoguardado_textEdit import comportAutoguardado_textEdit
from PyQt5.QtWidgets import  QMessageBox
import numpy as np

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaMultiple(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
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
####################################################################################################################################
#       C O N T R O L    D E     B O T O N E S :
####################################################################################################################################

        #CREANDO UNA MATRIZ DE PUROS BOTONES...
        renglonBotones= np.array( [[self.ventanas[0].btn_respA,self.ventanas[0].btn_respB,
                                    self.ventanas[0].btn_respC,self.ventanas[0].btn_respD]] )
        self.matrizBotonesRespuesta=renglonBotones
        for i in range(1, len(self.ventanas)):
            # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
            renglonBotones = np.array( [[self.ventanas[i].btn_respA, self.ventanas[i].btn_respB,
                                       self.ventanas[i].btn_respC, self.ventanas[i].btn_respD]])
            self.matrizBotonesRespuesta = np.append(self.matrizBotonesRespuesta, renglonBotones, axis=0)
        self.controlABSOLUTO_botones=comporSelecBtnsResp(self.matrizBotonesRespuesta,BORDER_RADIUS="5")
        print(self.matrizBotonesRespuesta.shape)
####################################################################################################################################
#       C O N T R O L    D E     POSICIONES DE RESPUESTAS :
####################################################################################################################################
        # CREANDO LA MATRIZ DE EDIT TEXT...
        renglonTxtEditRespuestas = np.array([[self.ventanas[0].txtEdit_respA, self.ventanas[0].txtEdit_respB,
                                    self.ventanas[0].txtEdit_respC, self.ventanas[0].txtEdit_respD]])
        self.matrizEditTextRespuestas = renglonTxtEditRespuestas
        for i in range(1, len(self.ventanas)):
            renglonTxtEditRespuestas = np.array([[self.ventanas[i].txtEdit_respA, self.ventanas[i].txtEdit_respB,
                                        self.ventanas[i].txtEdit_respC, self.ventanas[i].txtEdit_respD]])
            self.matrizEditTextRespuestas= np.append(self.matrizEditTextRespuestas, renglonTxtEditRespuestas, axis=0)

       #CREANDO EL VECTOR REGLON DE BOTONES ALIGN...
        ## Comportamiento de las ediciones de un edit text...
        self.vectorRenglon_btnAlignRespuestas = np.array([[self.btn_respIzq, self.btn_respCen, self.btn_respDer]])

        self.controlABSOLUTO_editTextRespuestas = comportEditTextEdit(self.vectorRenglon_btnAlignRespuestas,
                                                                      self.dSpin_respTam,
                                                                      self.matrizEditTextRespuestas)
####################################################################################################################################
#       C O N T R O L    D E     POSICIONES DE PREGUNTAS :
####################################################################################################################################
        # CREANDO LA MATRIZ DE EDIT TEXT...
        renglonTxtEditPreguntas= np.array([[self.ventanas[0].txtEdit_preg]])
        self.matrizEditTextPreguntas = renglonTxtEditPreguntas
        for i in range(1, len(self.ventanas)):
            renglonTxtEditPreguntas = np.array([[self.ventanas[i].txtEdit_preg]])
            self.matrizEditTextPreguntas = np.append(self.matrizEditTextPreguntas, renglonTxtEditPreguntas, axis=0)

        # CREANDO EL VECTOR REGLON DE BOTONES ALIGN...
        ## Comportamiento de las ediciones de un edit text...
        self.vectorRenglon_btnAlignPreguntas = np.array([[self.btn_pregIzq, self.btn_pregCen,self.btn_pregDer]])

        self.controlABSOLUTO_editTextPreguntas = comportEditTextEdit(self.vectorRenglon_btnAlignPreguntas,
                                                                      self.dSpin_pregTam,
                                                                      self.matrizEditTextPreguntas)
        print("QUE PEDO..",self.matrizEditTextPreguntas.shape)
####################################################################################################################################
#       C O N T R O L    D E     BOTONES DE PREGUNTAS HIBRIDAS :
####################################################################################################################################
        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_hibridasPreg = (self.btn_pregImag0, self.btn_pregImag50, self.btn_pregImag75,
                               self.btn_pregImag100)
        self.listImagen_hibridasPreg=("ICONOS/icon_preg0.png",
                                      "ICONOS/icon_preg50.png",
                                      "ICONOS/icon_preg75.png",
                                      "ICONOS/icon_preg100.png"
                                     )
        self.listNombres_preguntasHibridas=["MUTAPREGIMAG 0%","MUTAPREGIMAG 50%",
                                            "MUTAPREGIMAG 75%", "MUTAPREGIMAG 100%"]
        self.control=comporSelec_btnsImagen(self.listBtnPunteros_hibridasPreg,
                                            self.listImagen_hibridasPreg)
        self.control.COLOR_SELECCION="#D79DDB" #cambiando el color de seleccion
                                               #a uno de color rosa
        self.control.botonFuePresionado.connect(self.cambioHibridoPregunta)
        self.mutacionPregunta=0
        self.control.btnElegido=-1
        self.control.marcarDesmarcarRespuesta_automatico(self.mutacionPregunta,False)

####################################################################################################################################
#       C O N T R O L    D E   PREGUNTAS ESPECIFICAS U ABIERTAS :
####################################################################################################################################
        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_pregANDpregOR= (self.btn_pregAND,self.btn_pregOR)
        self.listImagen_pregANDpregOR=("ICONOS/icon_and.png",
                                      "ICONOS/icon_or.png",
                                     )
        self.control_2=comporSelec_btnsImagen(self.listBtnPunteros_pregANDpregOR,
                                              self.listImagen_pregANDpregOR)
        #self.control_2.COLOR_SELECCION="#13B470" #cambiando el color de seleccion
                                               #a uno de color rosa
        self.control_2.botonFuePresionado.connect(self.cambio_pregANDpregOR)
        self.pregAND_pregOR=1 #PREGUNTA DEFAULT PREG OR
        self.control_2.btnElegido=-1
        self.control_2.marcarDesmarcarRespuesta_automatico(self.pregAND_pregOR,False)
        self.COLOR_OR="#5DD1D6"
        self.COLOR_AND="#F51E8C"

####################################################################################################################################
#       C O N T R O L    D E     AUTOGUARDADO....
####################################################################################################################################

        self.matrizTodos_textEdit=self.matrizEditTextPreguntas
        print(self.matrizTodos_textEdit.shape)
        self.matrizTodos_textEdit=np.append(self.matrizTodos_textEdit,self.matrizEditTextRespuestas,axis=1)
        self.controlABSOULUTO_autoguardado=comportAutoguardado_textEdit(self.matrizTodos_textEdit)
        self.controlABSOULUTO_autoguardado.horaGuardarCambios.connect(self.guardarCambios)
        self.textoPregunta=""
        self.textoRespuestas=["","","",""]

        print(self.matrizTodos_textEdit.shape)


###########################################################################################################################
#
#
#       M    E     T     O     D     O     S    :
#
#
##############################################################################################################################


    def guardarCambios(self,listaDatos):
        idTxtRespueta=listaDatos[0]
        texto=listaDatos[1]
        if idTxtRespueta==0: #significa que es de la pregunta...
            self.textoPregunta=texto
        else: #significara que son los edit text de las respuestas..
            self.textoRespuestas[idTxtRespueta-1]=texto
        print(texto)


    def cambio_pregANDpregOR(self,idBtnFuePresionado):
        self.control_2.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)
        self.pregAND_pregOR=idBtnFuePresionado
        print("BOTON...",self.pregAND_pregOR)
        if idBtnFuePresionado==0:
            self.controlABSOLUTO_botones.setColor(self.COLOR_AND)
        else:
            self.controlABSOLUTO_botones.setColor(self.COLOR_OR)

    def cambioHibridoPregunta(self,idBtnFuePresionado):
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quiere cambiar al formato \n"
                                         f"de pregunta: '{self.listNombres_preguntasHibridas[idBtnFuePresionado]}' ?\n",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            #actulizando contenido de respuestas
            self.controlABSOULUTO_autoguardado.registrarRespuestas(False) #actualizamos los datos
                                                     #del ultimo edit text que se estaba editando

            #cargando el texto del edit text del widget al que nos pasaremos...
            self.matrizEditTextPreguntas[idBtnFuePresionado][0].setText(self.textoPregunta)
            #cargando el texto en lo edit text de las respuesta del widget donde nos pasaremos
            for respuesta in range(len(self.textoRespuestas)):
                self.matrizEditTextRespuestas[idBtnFuePresionado][respuesta].setText(self.textoRespuestas[respuesta])

            #Refrescando las posiciones ya que por alguna extraña razon, cuando lo poner un nuevo
            #texto su posicion de ve alterada
            self.controlABSOLUTO_editTextPreguntas.refrescarPosEditText(idBtnFuePresionado)
            self.controlABSOLUTO_editTextRespuestas.refrescarPosEditText(idBtnFuePresionado)

            self.listWidget_panelVersion.setCurrentIndex(idBtnFuePresionado)
            self.control.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)
################################################################################################################



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaMultiple()
    application.show()
    app.exec()
    #sys.exit(app.exec())


#https://blog.nubecolectiva.com/forma-ideal-de-trabajar-con-imagenes-y-una-base-de-datos-en-un-proyecto-web/

#https://pynative.com/python-sqlite-blob-insert-and-retrieve-digital-data/

#https://stackoverflow.com/questions/3309957/pysqlite-how-to-save-images

#https://www.quora.com/Whats-the-best-way-to-store-images-in-an-SQLite-database-using-Python-Ive-read-that-its-a-bad-idea-to-store-images-in-a-database-however-Im-not-building-a-mass-market-consumer-application-Is-it-a-bad-idea-What-are

'''
        self.controlABSOULUTO_autoguardadoResp=comportAutoguardado_textEdit(self.matrizEditTextRespuestas)
        self.controlABSOULUTO_autoguardadoResp.horaGuardarCambios.connect(self.guardarCambiosRespuesta)

        self.textoRespuestas=["","","",""] #a,b,c,d

        self.controlABSOULUTO_autoguardadoPreg = comportAutoguardado_textEdit(self.matrizEditTextPreguntas)
        self.controlABSOULUTO_autoguardadoPre.horaGuardarCambios.connect(self.guardarCambiosPregunta)
        self.textoPregunta = ""

'''