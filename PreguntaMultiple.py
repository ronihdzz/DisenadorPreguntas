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
import os

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

####################################################################################################################################
#      I M A G E N E S :
####################################################################################################################################
        #Conectando las imagenes....
        #apartir de la widget 2,todas tienen esa senal...
        for i in range(1,len(self.ventanas)):
            self.ventanas[i].alguienEligioImagen.connect(self.eligioImagen)

####################################################################################################################################
#      PROPEIDADES TIPO DE RESPUESTA...
####################################################################################################################################
        self.DIREC_IMAGENES = "HOLA/"
        self.textoRespuestas = ["", "", "", ""]

        # Estableciendo los limites del tamano letra...
        self.dSpin_respTam.setMinimum(30)
        self.dSpin_respTam.setMaximum(85)
        self.dSpin_pregTam.setMinimum(10)
        self.dSpin_pregTam.setMaximum(45)

        datosPregunta,datosRepuesta=self.datosDefault()

        self.abrirPregunta(datosPregunta,datosRepuesta)

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
        posiblesRespuestas=["A","B","C","D"]
        if idTxtRespueta==0: #significa que es de la pregunta...
            self.PROPIEDADES_PREGUNTA["TEXTO_PREGUNTA"]=texto
        else: #significara que son los edit text de las respuestas..
            respuestaGuardar="TEXTO_RESP"+posiblesRespuestas[idTxtRespueta-1]
            self.PROPIEDADES_RESPUESTA[respuestaGuardar]=texto
            self.textoRespuestas[idTxtRespueta-1]=texto

    def cambio_pregANDpregOR(self,idBtnFuePresionado):
        self.control_2.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)
        self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"]=idBtnFuePresionado #0=cualquiera  1=todas
        if idBtnFuePresionado==0:#FUE ESCOGIDA LA MODALIDAD ABIERTA...
            self.controlABSOLUTO_botones.setColor(self.COLOR_AND)
        else:#FUE ESCOGIDA LA MODALIDAD DE ELIGE TODAS...
            self.controlABSOLUTO_botones.setColor(self.COLOR_OR)



    def cambioHibridoPregunta(self,idBtnFuePresionado):
        resultado = QMessageBox.Yes
        if self.NUEVA_PREGUNTA == False:
            resultado = QMessageBox.question(self, "DelphiPreguntas",
                                             "¿Esta seguro que quiere cambiar al formato \n"
                                             f"de pregunta: '{self.listNombres_preguntasHibridas[idBtnFuePresionado]}' ?\n",
                                             QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"] = idBtnFuePresionado  # 0=sin imagen 1=con imagen en pregunta....
            # actulizando contenido de respuestas
            self.controlABSOULUTO_autoguardado.registrarRespuestas(False)  # actualizamos los datos
            # del ultimo edit text que se estaba editando

            # cargando el texto del edit text del widget al que nos pasaremos...
            textoPregunta = self.PROPIEDADES_PREGUNTA["TEXTO_PREGUNTA"]
            self.matrizEditTextPreguntas[idBtnFuePresionado][0].setText(textoPregunta)
            # cargando el texto en lo edit text de las respuesta del widget donde nos pasaremos
            for respuesta in range(len(self.textoRespuestas)):
                self.matrizEditTextRespuestas[idBtnFuePresionado][respuesta].setText(self.textoRespuestas[respuesta])

            # Refrescando las posiciones ya que por alguna extraña razon, cuando lo poner un nuevo
            # texto su posicion de ve alterada
            self.controlABSOLUTO_editTextPreguntas.refrescarPosEditText(idBtnFuePresionado)
            self.controlABSOLUTO_editTextRespuestas.refrescarPosEditText(idBtnFuePresionado)

            self.listWidget_panelVersion.setCurrentIndex(idBtnFuePresionado)
            self.control.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado, False)

            #Cargando las imagenes....
            # IMAGEN_PREGUNTA...
            if idBtnFuePresionado>0: #Significa que es una pregunta con respuestas imagenes...
                if idBtnFuePresionado==1 or idBtnFuePresionado==3: #preguntaImagen 50% or preguntaImagen 100%
                    # IMAGEN_PREGUNTA...
                    imagenPregunta=self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]
                    #Cagaremos la imagen pero no la respuesta...
                    if imagenPregunta != None:
                        imagenPregunta = self.DIREC_IMAGENES + imagenPregunta
                    self.ventanas[idBtnFuePresionado].controlABSOLUTO_labelImagen.escogioImagen(0, False, imagenPregunta)
                if idBtnFuePresionado>1:#preguntaImagen 50% or preguntaImagen 75%
                    respuestas = ["A", "B", "C", "D"]
                    listaRespuestaImagen = [self.PROPIEDADES_RESPUESTA["IMAGEN_RESP" + letra] for letra in respuestas ]
                    listaRespuestaImagen=[ self.DIREC_IMAGENES+x if x!=None else x for x in listaRespuestaImagen]
                    contador=0
                    if idBtnFuePresionado==3: #si la widget que fue presionada fue la de...
                                              #100% preguntas...
                        contador=1
                    print(listaRespuestaImagen)
                    for i in range(len(respuestas)):
                        self.ventanas[idBtnFuePresionado].controlABSOLUTO_labelImagen.escogioImagen(contador+i, False,listaRespuestaImagen[i])

    def datosDefault(self):
        datosPregunta={
            "GRADO_IMAGENES": 1,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 60,
            "TEXTO_PREGUNTA": None,
            "IMAGEN_PREGUNTA": None,
            "TAMANO_PREGUNTA": 15,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 70,
            "POSICION_RESPUESTA":1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR":1,  # 0=todas 1=cualquiera
            "RESPUESTAS": "0,0,0,0"
        }

        datosRespuesta={
            "TEXTO_RESPA": None,
            "IMAGEN_RESPA":None,
            "TEXTO_RESPB": None,
            "IMAGEN_RESPB": None,
            "TEXTO_RESPC": None,
            "IMAGEN_RESPC": None,
            "TEXTO_RESPD": None,
            "IMAGEN_RESPD": None
        }

        return datosPregunta,datosRespuesta


    def abrirPregunta(self, datosPregunta, datosRespuesta):
        self.PROPIEDADES_PREGUNTA = datosPregunta
        self.PROPIEDADES_RESPUESTA = datosRespuesta
        # P R E G U N T A   :
        # GRADO_IMAGENES...
        self.NUEVA_PREGUNTA = True

        gradoImagenes=self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"]
        self.control.botonPresionado(gradoImagenes)  # 0=0%imagen  1=50%imagen
        # TIEMPO_SEGUNDOS...
        tiempo = self.PROPIEDADES_PREGUNTA["TIEMPO_SEGUNDOS"]
        self.timeEdit.setTime(QtCore.QTime(0, int(tiempo / 60), tiempo % 60, 0))  # 1 minuto
        # TEXTO_PREGUNTA...
        # Poniendo el texto por default....

        texto = self.PROPIEDADES_PREGUNTA["TEXTO_PREGUNTA"]
        for i in range(len(self.ventanas)):
            self.ventanas[i].txtEdit_preg.setText(texto)
        # IMAGEN_PREGUNTA...
        #imagenPregunta = self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]
        #self.ventanas[1].controlABSOLUTO_pregImagen.escogioImagen(0, False, imagenPregunta)

        # TAMANO_PREGUNTA...
        self.dSpin_pregTam.setValue(self.PROPIEDADES_PREGUNTA["TAMANO_PREGUNTA"])
        # POSICION_PREGUNTA...
        # 0=izquierda 1=centro 2=derecha
        self.controlABSOLUTO_editTextPreguntas.editPosEditsText(self.PROPIEDADES_PREGUNTA["POSICION_PREGUNTA"])
        # TAMANO_RESPUESTA...
        # 0=izquierda 1=centro 2=derecha
        self.dSpin_respTam.setValue(self.PROPIEDADES_PREGUNTA["TAMANO_RESPUESTA"])
        # POSICION_RESPUESTA...
        # 0=izquierda 1=centro 2=derecha
        self.controlABSOLUTO_editTextRespuestas.editPosEditsText(self.PROPIEDADES_PREGUNTA["POSICION_RESPUESTA"])
        # FORMA_EVALUAR...
        # 0=eligeTodas 1=eligeCualquiera
        self.cambio_pregANDpregOR(self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"])
        # RESPUESTAS...
        listRespuestas = self.PROPIEDADES_PREGUNTA["RESPUESTAS"]
        a = [int(x) for x in listRespuestas.split(",")]
        self.controlABSOLUTO_botones.setAllRespuestas(a)

        # R E S P U E S T A S :
        # Poniendo el texto por default....
        respuestas=["A","B","C","D"]
        listaRespuestaText=[self.PROPIEDADES_RESPUESTA["TEXTO_RESP"+letra] for letra in respuestas]
        for i in range(len(self.ventanas)):
            self.ventanas[i].txtEdit_respA.setText(listaRespuestaText[0])
            self.ventanas[i].txtEdit_respB.setText(listaRespuestaText[1])
            self.ventanas[i].txtEdit_respC.setText(listaRespuestaText[2])
            self.ventanas[i].txtEdit_respD.setText(listaRespuestaText[3])
        self.textoRespuestas = listaRespuestaText
        self.NUEVA_PREGUNTA = False
        # POSICION_RESPUESTA...
        # 0=izquierda 1=centro 2=derecha
        self.controlABSOLUTO_editTextRespuestas.editPosEditsText(self.PROPIEDADES_PREGUNTA["POSICION_RESPUESTA"])

    def eligioImagen(self,listaInformacion):
        #0=imagenPregunta, 1=imagenRespuesta_A, 2=imagenRespuesta_B....
        idLabelEligioImagen=listaInformacion[0]
        direcGuardoImagen=listaInformacion[1]
        noLabelsImagen=listaInformacion[2]
        respuestas = ["A", "B", "C", "D"]

        if (idLabelEligioImagen == 0 and noLabelsImagen==1) or (idLabelEligioImagen == 0 and noLabelsImagen==5):  # es una imagen pregunta...
            imagenAntiguaAlmacenada = self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]
            self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]=direcGuardoImagen
            if imagenAntiguaAlmacenada != "NULL" and imagenAntiguaAlmacenada != None and self.NUEVA_PREGUNTA == False:
                # Debemos eliminar la imagen...
                os.remove(self.DIREC_IMAGENES + imagenAntiguaAlmacenada)
        else:# es una imagen respuesta...
            if noLabelsImagen==5: #significa si es una pregunta imagen 100% entonces...
                idLabelEligioImagen-=1
            respuestaX = "IMAGEN_RESP" + respuestas[idLabelEligioImagen]
            imagenAntiguaAlmacenada = self.PROPIEDADES_RESPUESTA[respuestaX]
            if imagenAntiguaAlmacenada != "NULL" and imagenAntiguaAlmacenada != None and self.NUEVA_PREGUNTA == False:
                # Debemos eliminar la imagen...
                os.remove(self.DIREC_IMAGENES + imagenAntiguaAlmacenada)
            self.PROPIEDADES_RESPUESTA[respuestaX]=direcGuardoImagen





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