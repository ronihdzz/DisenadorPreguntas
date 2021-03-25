from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMessageBox
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QDoubleValidator,QRegExpValidator
from PyQt5 import QtCore
import numpy as np
from PyQt5.QtCore import pyqtSignal

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Pregunta_Abierta.modRespAbierta_d import Ui_Form
from CUERPO.LOGICA_creador.Creador_Pregunta_Abierta.PreguntaAbiertaImagen_0  import PreguntaAbiertaImagen_0
from CUERPO.LOGICA_creador.Creador_Pregunta_Abierta.PreguntaAbiertaImagen_50 import PreguntaAbiertaImagen_50

###############################################################
#  MIS LIBRERIAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.comportSelect_btnsImagen import comporSelec_btnsImagen
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
from CUERPO.LOGICA_creador.Creador_MisPaquetes.comportEditTextEdit import comportEditTextEdit

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaAbierta(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self,nombreCreador="",direc_carpetaImagenes=""):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.ventanas = []
        self.ventanas.append( PreguntaAbiertaImagen_0() )  # pregunta binaria
        self.ventanas.append( PreguntaAbiertaImagen_50(nombreCreador,direc_carpetaImagenes) )  # preguntas multiples

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()

        self.listImagenBotonesPosiciones=[RecursosCreadorCuestionarios.ICONO_POS_LEFT,
                                          RecursosCreadorCuestionarios.ICONO_POS_CENTER,
                                          RecursosCreadorCuestionarios.ICONO_POS_RIGTH
                                        ]
        self.DIREC_IMAGENES=direc_carpetaImagenes


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
                                                                      self.matrizEditTextPreguntas,
                                                                      self.listImagenBotonesPosiciones)

####################################################################################################################################
#       C O N T R O L    D E   RESPUESTAS STRING O RESPUESTAS NUMERO...
####################################################################################################################################
        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_respStrOdouble = (self.btn_respString, self.btn_respNumero)
        self.respStrOdouble = (
                                RecursosCreadorCuestionarios.ICONO_RESP_STRING,
                                RecursosCreadorCuestionarios.ICONO_RESP_NUMBER
                               )
        self.nombreTipoRespuestas=("PALABRA","NUMERO")

        self.control_2 = comporSelec_btnsImagen(self.listBtnPunteros_respStrOdouble,
                                                self.respStrOdouble)
        # self.control_2.COLOR_SELECCION="#13B470" #cambiando el color de seleccion
        # a uno de color rosa
        self.control_2.botonFuePresionado.connect(self.cambio_pregANDpregOR)
        self.LIMITE_CARACTERES=30
        self.lineEdit_respuesta.setMaxLength(self.LIMITE_CARACTERES)
        self.bel_maxChars.setText(str(self.LIMITE_CARACTERES))
        self.lineEdit_respuesta.textChanged.connect(lambda x: self.bel_noChars.setText( str(len(self.lineEdit_respuesta.text()))) )

####################################################################################################################################
#       C O N T R O L    D E     BOTONES DE PREGUNTAS HIBRIDAS :
####################################################################################################################################
        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_hibridasPreg = (self.btn_pregImag0, self.btn_pregImag50)
        self.listImagen_hibridasPreg=(RecursosCreadorCuestionarios.ICONO_INCLUIR_IMAGENES_0,
                                      RecursosCreadorCuestionarios.ICONO_INCLUIR_IMAGENES_50
                                     )
        self.listNombres_preguntasHibridas=["MUTAPREGIMAG 0%","MUTAPREGIMAG 50%"]
        self.control=comporSelec_btnsImagen(self.listBtnPunteros_hibridasPreg,
                                            self.listImagen_hibridasPreg)
        self.control.COLOR_SELECCION="#D79DDB" #cambiando el color de seleccion
                                               #a uno de color rosa
        self.control.botonFuePresionado.connect(self.cambioHibridoPregunta)
####################################################################################################################################
#      I M A G E N E S :
####################################################################################################################################
        self.ventanas[1].alguienEligioImagen.connect(self.eligioImagen)  # contiene la widget de imagenes 50%

        #Constantes de tamano maximo perimitido de letra...
        self.dSpin_pregTam.setMinimum(10)
        self.dSpin_pregTam.setMaximum(35)
        self.dSpin_pregTam.setValue(15)

        self.preguntaBlanco()



    def preguntaBlanco(self):
        self.ventanas[1].controlABSOLUTO_labelImagen.ponerEnDafultTodasLabel()
        datosPregunta,datosRespuesta=self.datosDefault()
        self.abrirPregunta(datosPregunta,datosRespuesta)
        return self.getDatos()


    def getDatos(self,tupleFormat=True):

        #obteniendo el tiempo destinado a la pregunta...
        segundos=self.timeEdit.time().second()+self.timeEdit.time().minute()*60
        self.PROPIEDADES_PREGUNTA["TIEMPO_SEGUNDOS"]=segundos
        self.PROPIEDADES_PREGUNTA["POSICION_PREGUNTA"]=self.controlABSOLUTO_editTextPreguntas.punteroPOS

        self.PROPIEDADES_PREGUNTA["TAMANO_PREGUNTA"]=self.dSpin_pregTam.value()

        # Como no hay autoguardado es necesario hacer lo siguiente...
        punteroWidgget=self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"]
        self.PROPIEDADES_PREGUNTA["TEXTO_PREGUNTA"]=self.ventanas[punteroWidgget].txtEdit_preg.toPlainText()
        self.PROPIEDADES_PREGUNTA["RESPUESTAS"]=self.lineEdit_respuesta.text()

        for a,b in self.PROPIEDADES_PREGUNTA.items():
            print(a,"-",b)

        if tupleFormat:
            return tuple(self.PROPIEDADES_PREGUNTA.values()),None
        else:
            return self.PROPIEDADES_PREGUNTA.copy(),None

    def closeEvent(self, event):
        print(self.getDatos())
        event.accept()


    def datosDefault(self):
        datosPregunta = {
            "GRADO_IMAGENES": 0,  # 0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS": 60,
            "TEXTO_PREGUNTA": "",
            "IMAGEN_PREGUNTA": "r",
            "TAMANO_PREGUNTA": 15,
            "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
            "TAMANO_RESPUESTA": 0, #NO TIENE ESTA PROPIEDAD....
            "POSICION_RESPUESTA": 1,  # 0=left 1=center  2=rigth
            "FORMA_EVALUAR": 0,  # 0=preguntasString  1=preguntasNumero
            "RESPUESTAS": ""
        }
        datosRespuesta = None
        return datosPregunta, datosRespuesta

    def abrirPregunta(self, datosPregunta, datosRespuesta):
        self.PROPIEDADES_PREGUNTA = datosPregunta
        self.PROPIEDADES_RESPUESTA = datosRespuesta
        # P R E G U N T A   :
        # GRADO_IMAGENES...

        self.NUEVA_PREGUNTA = True
        gradoImagenes = self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"]
        self.control.botonPresionado(gradoImagenes)  # 0=0%imagen  1=50%imagen
        # TIEMPO_SEGUNDOS...
        tiempo = self.PROPIEDADES_PREGUNTA["TIEMPO_SEGUNDOS"]
        self.timeEdit.setTime(QtCore.QTime(0, int(tiempo / 60), tiempo % 60, 0))  # 1 minuto
        # TEXTO_PREGUNTA...
        # Poniendo el texto por default....

        texto = self.PROPIEDADES_PREGUNTA["TEXTO_PREGUNTA"]
        for i in range(len(self.ventanas)):
            self.ventanas[i].txtEdit_preg.setText(texto)
        # IMAGEN_PREGUNTA... ya lo hace la funcion anterior...
        # imagenPregunta = self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]
        # self.ventanas[1].controlABSOLUTO_pregImagen.escogioImagen(0, False, imagenPregunta)

        # TAMANO_PREGUNTA...
        self.dSpin_pregTam.setValue(self.PROPIEDADES_PREGUNTA["TAMANO_PREGUNTA"])
        # POSICION_PREGUNTA...
        # 0=izquierda 1=centro 2=derecha
        self.controlABSOLUTO_editTextPreguntas.editPosEditsText(self.PROPIEDADES_PREGUNTA["POSICION_PREGUNTA"])
        # TAMANO_RESPUESTA...
        # POSICION_RESPUESTA...
       # FORMA_EVALUAR...
        # 0=eligeTodas 1=eligeCualquiera
        self.cambio_pregANDpregOR(self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"])
        # RESPUESTAS...
        respuesta = self.PROPIEDADES_PREGUNTA["RESPUESTAS"]
        self.lineEdit_respuesta.setText(str(respuesta))

        self.NUEVA_PREGUNTA=False


    def eligioImagen(self, listaInformacion):
        # 0=imagenPregunta, 1=imagenRespuesta_A, 2=imagenRespuesta_B....
        idLabelEligioImagen = listaInformacion[0]
        direcGuardoImagen = listaInformacion[1]
        noLabelsImagen = listaInformacion[2]

        if (idLabelEligioImagen == 0 and noLabelsImagen == 1):  # es una imagen pregunta...
            imagenAntiguaAlmacenada = self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]
            self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"] = direcGuardoImagen
            if imagenAntiguaAlmacenada != "" and imagenAntiguaAlmacenada != None and self.NUEVA_PREGUNTA == False:
                # Debemos eliminar la imagen...
                os.remove(self.DIREC_IMAGENES + imagenAntiguaAlmacenada)





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

    def cambio_pregANDpregOR(self,idBtnFuePresionado):
        resultado=QMessageBox.Yes
        if self.NUEVA_PREGUNTA == False:
            resultado = QMessageBox.question(self, "DelphiPreguntas",
                                             "¿Esta seguro que quieres cambiar a \n"
                                             f"respuestas de tipo {self.nombreTipoRespuestas[idBtnFuePresionado]}?\n"
                                             "de ser asi debes considerar que el\n"
                                             "contenido de tu respuesta de ahorita\n"
                                             "se borrara",
                                             QMessageBox.Yes | QMessageBox.No)
        if resultado==QMessageBox.Yes:
            self.control_2.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)
            self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"] = idBtnFuePresionado  # 0=cualquiera  1=todas
            if idBtnFuePresionado==0:#respuesta string....
                self.bel_noChars.setText("0")
                self.lineEdit_respuesta.setText("")
                validator = QRegExpValidator(QRegExp("[^\n  ]{1," + str(self.LIMITE_CARACTERES) + "}"))
                self.lineEdit_respuesta.setValidator(validator)
            else: #respuesta double..
                self.bel_noChars.setText("0")
                self.lineEdit_respuesta.setText("")
                self.lineEdit_respuesta.setValidator(QDoubleValidator())


    def cambioHibridoPregunta(self,idBtnFuePresionado):
        resultado = QMessageBox.Yes
        if self.NUEVA_PREGUNTA == False:
            resultado = QMessageBox.question(self, "DelphiPreguntas",
                                             "¿Esta seguro que quiere cambiar al formato \n"
                                             f"de pregunta: '{self.listNombres_preguntasHibridas[idBtnFuePresionado]}' ?\n",
                                             QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.listWidget_panelVersion.setCurrentIndex(idBtnFuePresionado)
            self.control.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)
            punteroWidget=self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"]
            #cargando el texto del edit text del widget al que nos pasaremos...
            self.textPregunta= self.matrizEditTextPreguntas[punteroWidget][0].toPlainText()
            self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"] = idBtnFuePresionado  # 0=sin imagen 1=con imagen en pregunta....
            punteroWidget=self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"]
            self.matrizEditTextPreguntas[punteroWidget][0].setText(self.textPregunta)
            #Refrescando las posiciones ya que por alguna extraña razon, cuando lo poner un nuevo
            #texto su posicion de ve alterada
            self.controlABSOLUTO_editTextPreguntas.refrescarPosEditText(idBtnFuePresionado)

            # Cargando las imagenes....
            # IMAGEN_PREGUNTA...
            if idBtnFuePresionado > 0:  # Significa que es una pregunta con respuestas imagenes...
                if idBtnFuePresionado == 1:  # preguntaImagen 50%....
                    # IMAGEN_PREGUNTA...
                    imagenPregunta = self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]
                    # Cagaremos la imagen pero no la respuesta...
                    i=imagenPregunta
                    if not (i == None or i == False or i == "" or i == "NULL"):
                        imagenPregunta = self.DIREC_IMAGENES + imagenPregunta
                    self.ventanas[idBtnFuePresionado].controlABSOLUTO_labelImagen.escogioImagen(0, False,imagenPregunta)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaAbierta()
    application.show()
    app.exec()
    #sys.exit(app.exec())



