from PyQt5 import QtWidgets
from PyQt5.QtWidgets import  QMessageBox


import numpy as np
from comportEditTextEdit import comportEditTextEdit
from comporSelect_btnsImagen import comporSelec_btnsImagen
from PyQt5.QtCore import pyqtSignal
from DISENOS.modRespAbierta_d import  Ui_Form
from PreguntaAbiertaImagen_0 import PreguntaAbiertaImagen_0
from PreguntaAbiertaImagen_50 import PreguntaAbiertaImagen_50


#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaAbierta(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.ventanas = []
        self.ventanas.append( PreguntaAbiertaImagen_0() )  # pregunta binaria
        self.ventanas.append( PreguntaAbiertaImagen_50() )  # preguntas multiples

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()

        self.textPregunta=""
        self.punteroWidget=0

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

        self.dSpin_pregTam.setMinimum(10)
        self.dSpin_pregTam.setMaximum(15)
        self.dSpin_pregTam.setValue(50)


####################################################################################################################################
#       C O N T R O L    D E   RESPUESTAS STRING O RESPUESTAS NUMERO...
####################################################################################################################################
        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_respStrOdouble = (self.btn_respString, self.btn_respNumero)
        self.respStrOdouble = (
                                "ICONOS/icon_respPalabra.png",
                                "ICONOS/icon_respNumber.png"
                               )
        self.nombreTipoRespuestas=("PALABRA","NUMERO")

        self.control_2 = comporSelec_btnsImagen(self.listBtnPunteros_respStrOdouble,
                                                self.respStrOdouble)
        # self.control_2.COLOR_SELECCION="#13B470" #cambiando el color de seleccion
        # a uno de color rosa
        self.control_2.botonFuePresionado.connect(self.cambio_pregANDpregOR)
        self.pregStr_Double = 0  # RESPUESTA DEFAULT STRING...
        self.control_2.btnElegido = -1
        self.LIMITE_CARACTERES=30

        self.bel_maxChars.setText(str(self.LIMITE_CARACTERES))
        self.lineEdit_respuesta.textChanged.connect(lambda x: self.bel_noChars.setText( str(len(self.lineEdit_respuesta.text()))) )

        validator = QRegExpValidator(QRegExp("[^\n  ]{1,"+str(self.LIMITE_CARACTERES)+"}"))
        self.lineEdit_respuesta.setValidator(validator)
        self.lineEdit_respuesta.setMaxLength(self.LIMITE_CARACTERES)
        self.control_2.marcarDesmarcarRespuesta_automatico(self.pregStr_Double, False)
####################################################################################################################################
#       C O N T R O L    D E     BOTONES DE PREGUNTAS HIBRIDAS :
####################################################################################################################################
        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_hibridasPreg = (self.btn_pregImag0, self.btn_pregImag50)
        self.listImagen_hibridasPreg=("ICONOS/icon_preg0.png",
                                      "ICONOS/icon_preg50.png")
        self.listNombres_preguntasHibridas=["MUTAPREGIMAG 0%","MUTAPREGIMAG 50%"]
        self.control=comporSelec_btnsImagen(self.listBtnPunteros_hibridasPreg,
                                            self.listImagen_hibridasPreg)
        self.control.COLOR_SELECCION="#D79DDB" #cambiando el color de seleccion
                                               #a uno de color rosa
        self.control.botonFuePresionado.connect(self.cambioHibridoPregunta)
        self.mutacionPregunta=0
        self.control.btnElegido=-1
        self.control.marcarDesmarcarRespuesta_automatico(self.mutacionPregunta,False)


    def cambio_pregANDpregOR(self,idBtnFuePresionado):
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quieres cambiar a \n"
                                         f"respuestas de tipo {self.nombreTipoRespuestas[idBtnFuePresionado]}?\n"
                                         "de ser asi debes considerar que el\n"
                                         "contenido de tu respuesta de ahorita\n"
                                         "se borrara",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.control_2.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)
            self.pregStr_Double=idBtnFuePresionado
            print("BOTON...", self.pregStr_Double)
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
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quiere cambiar al formato \n"
                                         f"de pregunta: '{self.listNombres_preguntasHibridas[idBtnFuePresionado]}' ?\n",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.listWidget_panelVersion.setCurrentIndex(idBtnFuePresionado)
            self.control.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado,False)

            #cargando el texto del edit text del widget al que nos pasaremos...
            self.textPregunta= self.matrizEditTextPreguntas[self.punteroWidget][0].toPlainText()
            self.punteroWidget=idBtnFuePresionado
            self.matrizEditTextPreguntas[self.punteroWidget][0].setText(self.textPregunta)
            #Refrescando las posiciones ya que por alguna extraña razon, cuando lo poner un nuevo
            #texto su posicion de ve alterada
            self.controlABSOLUTO_editTextPreguntas.refrescarPosEditText(idBtnFuePresionado)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaAbierta()
    application.show()
    app.exec()
    #sys.exit(app.exec())

'''



        respuestaTexto=QLineEdit()
        validator = QRegExpValidator(QRegExp("[^\n  ]{1,50}"))
        respuestaTexto.setValidator(validator)QRegExp("[^\n  ]{1,50}")

        respuestaTexto.setMinimumSize(500,200)
        respuestaTexto.setMaximumSize(500,200)
        self.layoutRespuesta.addWidget(respuestaTexto)

setValidator()
Sets the validation rules. Available validators are
QIntValidator − Restricts input to integer
QDoubleValidator − Fraction part of number limited to specified decimals
QRegexpValidator − Checks input against a Regex expression
'''