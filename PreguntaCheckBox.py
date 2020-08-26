from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QGridLayout,QCheckBox,QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespCheckBox_d  import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

from PyQt5.QtCore import Qt, pyqtSignal, QFile
from functools import partial

from comporEdit_TextEdit import comporEdit_TextEdit
from comporSelecBtnsResp import comporSelecBtnsResp
#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from functools import partial
import numpy as np
from PyQt5.QtWidgets import  QMessageBox

from PreguntaCheckBoxImagen_0 import PreguntaCheckBoxImagen_0
from PreguntaCheckBoxImagen_50 import PreguntaCheckBoxImagen_50
from comporSelect_btnsImagen import comporSelec_btnsImagen
from comportEditTextEdit import comportEditTextEdit
from PyQt5.QtCore import Qt, pyqtSignal, QFile,QObject
import os
from functools import partial


class itemRoniano(QObject):
    suHoraMorir= pyqtSignal(int)#indicara quien es el objeto que quiere morir...
    def __init__(self,id,checkBox_estado,textEdit_texto,boton_muerte):

        QObject.__init__(self)
        self.id=id
        self.checkBox_estado=checkBox_estado
        self.textEdit_texto=textEdit_texto
        self.boton_muerte=boton_muerte
        self.boton_muerte.clicked.connect(self.mandarSenalMuerto)

    def mandarSenalMuerto(self):
        self.suHoraMorir.emit(self.id)


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaCheckBox(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # creando multiples ventanas...
        self.ventanas = []
        self.ventanas.append(PreguntaCheckBoxImagen_0())
        self.ventanas.append(PreguntaCheckBoxImagen_50())

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()



####################################################################################################################################
#       C O N T R O L    D E     POSICIONES DE PREGUNTAS :
####################################################################################################################################
        # CREANDO LA MATRIZ DE EDIT TEXT...
        renglonTxtEditPreguntas = np.array([[self.ventanas[0].txtEdit_preg]])
        self.matrizEditTextPreguntas = renglonTxtEditPreguntas
        for i in range(1, len(self.ventanas)):
            renglonTxtEditPreguntas = np.array([[self.ventanas[i].txtEdit_preg]])
            self.matrizEditTextPreguntas = np.append(self.matrizEditTextPreguntas, renglonTxtEditPreguntas, axis=0)

        # CREANDO EL VECTOR REGLON DE BOTONES ALIGN...
        ## Comportamiento de las ediciones de un edit text...
        self.vectorRenglon_btnAlignPreguntas = np.array([[self.btn_pregIzq, self.btn_pregCen, self.btn_pregDer]])

        self.controlABSOLUTO_editTextPreguntas = comportEditTextEdit(self.vectorRenglon_btnAlignPreguntas,
                                                                     self.dSpin_pregTam,
                                                                     self.matrizEditTextPreguntas)

####################################################################################################################################
#       C O N T R O L    D E     POSICIONES DE RESPUESTAS :
####################################################################################################################################
        # CREANDO LA MATRIZ DE EDIT TEXT...
        self.matrizEditTextRespuestas = np.empty((1,0),dtype=QTextEdit).reshape(1,0)
        # CREANDO EL VECTOR REGLON DE BOTONES ALIGN...
        ## Comportamiento de las ediciones de un edit text...
        self.vectorRenglon_btnAlignRespuestas = np.array([[self.btn_respIzq, self.btn_respCen, self.btn_respDer]])

        self.controlABSOLUTO_editTextRespuestas = comportEditTextEdit(self.vectorRenglon_btnAlignRespuestas,
                                                                      self.dSpin_respTam,
                                                                      self.matrizEditTextRespuestas)
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


        self.widget = QWidget()  # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()  # The Vertical Box that contains the Horizontal Boxes of  labels and buttons
        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll_barra.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setWidget(self.widget)
        self.MAX_ITEMS=6
        self.punteroNoItems=0
        self.contadorIdsVivosMuertos = 0
        self.IMAGEN_ELIMINAR="ICONOS/icon_tache.png"
        self.IMAGEN_ELIMINAR_2="ICONOS/icon_tache2.png"

        self.DIREC_IMAGENES="HOLA/"
        self.btn_addCheckBox.clicked.connect(partial(self.agregarCheckBox,"",False))

        self.listaItemsRonianos=[]
        self.textPregunta=""
        self.listIdsItemsVivos=[]
        self.dSpin_respTam.setMinimum(8)
        self.dSpin_respTam.setMaximum(25)
        self.dSpin_respTam.setValue(15)
        self.dSpin_pregTam.setMinimum(8)
        self.dSpin_pregTam.setMaximum(40)
        self.dSpin_pregTam.setValue(15)
        self.punteroWidget = 0


        datosPregunta,datosRespuesta=self.datosDefault()
        self.abrirPregunta(datosPregunta,datosRespuesta)



###########################################################################################################################
#
#
#       M    E     T     O     D     O     S    :
#
#
##############################################################################################################################

    def getDatos(self):

        #obteniendo el tiempo destinado a la pregunta...
        segundos=self.timeEdit.time().second()+self.timeEdit.time().minute()*60
        self.PROPIEDADES_PREGUNTA["TIEMPO_SEGUNDOS"]=segundos
        self.PROPIEDADES_PREGUNTA["POSICION_PREGUNTA"]=self.controlABSOLUTO_editTextPreguntas.punteroPOS
        self.PROPIEDADES_PREGUNTA["POSICION_RESPUESTA"]=self.controlABSOLUTO_editTextRespuestas.punteroPOS

        self.PROPIEDADES_PREGUNTA["TAMANO_PREGUNTA"]=self.dSpin_pregTam.value()
        self.PROPIEDADES_PREGUNTA["TAMANO_RESPUESTA"] = self.dSpin_respTam.value()

        #Como no hay autoguardado es necesario hacer lo siguiente...
        punteroWidgget=self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"]
        self.PROPIEDADES_PREGUNTA["TEXTO"]=self.ventanas[punteroWidgget].txtEdit_preg.toPlainText()


        #iterando sobre todos los items existentes....
        respuestas=""
        textoRespuestas=""
        for item in self.listaItemsRonianos:
            respuestas+=str(int(item.checkBox_estado.isChecked()))+","
            textoRespuestas+=item.textEdit_texto.toPlainText()+","

        self.PROPIEDADES_PREGUNTA["RESPUESTAS"]=str(respuestas)[:-1] #quitando la coma sobrante
        self.PROPIEDADES_RESPUESTA["TEXTO_ITEMS"]=str(textoRespuestas)[:-1]  #quitando la coma sobrante


        for a,b in self.PROPIEDADES_PREGUNTA.items():
            print(a,"-",b)

        for a,b in self.PROPIEDADES_RESPUESTA.items():
            print(a,"-",b)

        return tuple(self.PROPIEDADES_PREGUNTA.values()),tuple(self.PROPIEDADES_RESPUESTA.values())



    def closeEvent(self, event):
        print(self.getDatos())
        event.accept()











    def datosDefault(self):
            datosPregunta={
                "GRADO_IMAGENES": 1,  # 0=sin imagen 1=con imagen en pregunta....
                "TIEMPO_SEGUNDOS": 60,
                "TEXTO_PREGUNTA": "Caracteristicas de Roni",
                "IMAGEN_PREGUNTA": None,
                "TAMANO_PREGUNTA": 30,
                "POSICION_PREGUNTA": 0,  # 0=left 1=center  2=rigth
                "TAMANO_RESPUESTA": 20,
                "POSICION_RESPUESTA":0,  # 0=left 1=center  2=rigth
                "FORMA_EVALUAR":0,  # 0=todas 1=cualquiera  ya que deben elegirse todas las opcciones correctas
                "RESPUESTAS": "1,1"
            }

            datosRespuesta={
                "NO_ITEMS":2,
                "TEXTO_ITEMS":"Amor,Odio"
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
        # IMAGEN_PREGUNTA... ya lo hace la funcion anterior...
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
        #self.cambio_pregANDpregOR(self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"])
        # RESPUESTAS...
        listRespuestas = self.PROPIEDADES_PREGUNTA["RESPUESTAS"]
        if listRespuestas!=None:
            listRespuestas = [int(x) for x in listRespuestas.split(",")]
            # R E S P U E S T A S :
            listItems=self.PROPIEDADES_RESPUESTA["TEXTO_ITEMS"]
            listItems=listItems.split(",")
            #Creando los items que son...
            for noItem in range(len(listItems)):
                self.agregarCheckBox(listItems[noItem],listRespuestas[noItem])

        self.NUEVA_PREGUNTA = False
        #self.dSpin_respTam.setValue(self.PROPIEDADES_PREGUNTA["TAMANO_RESPUESTA"])

        # POSICION_RESPUESTA...
        # 0=izquierda 1=centro 2=derecha
        #actualizando tamanos y posiciones en los items...
        self.controlABSOLUTO_editTextRespuestas.editPosEditsText(self.PROPIEDADES_PREGUNTA["POSICION_RESPUESTA"])
        self.controlABSOLUTO_editTextRespuestas.cambiarTam(self.PROPIEDADES_PREGUNTA["TAMANO_RESPUESTA"])


    def eligioImagen(self,listaInformacion):
        #0=imagenPregunta, 1=imagenRespuesta_A, 2=imagenRespuesta_B....
        idLabelEligioImagen=listaInformacion[0]
        direcGuardoImagen=listaInformacion[1]
        noLabelsImagen=listaInformacion[2]

        if (idLabelEligioImagen == 0 and noLabelsImagen==1):  # es una imagen pregunta...
            imagenAntiguaAlmacenada = self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]
            self.PROPIEDADES_PREGUNTA["IMAGEN_PREGUNTA"]=direcGuardoImagen
            if imagenAntiguaAlmacenada != "NULL" and imagenAntiguaAlmacenada != None and self.NUEVA_PREGUNTA == False:
                # Debemos eliminar la imagen...
                os.remove(self.DIREC_IMAGENES + imagenAntiguaAlmacenada)

    def agregarCheckBox(self,texto="",estado=0):
        if self.punteroNoItems<self.MAX_ITEMS:
            widget = QWidget()
            widget.setMinimumHeight(75)
            widget.setMaximumHeight(75)
            gridLayout = QGridLayout(widget)  # Set the checkbox in the layer
            checkBox = QCheckBox()
            checkBox.setStyleSheet("QCheckBox::indicator {width:30px; height:30px; }"
                                   "QCheckBox::indicator:pressed{background-color:#0C868C;}"
                                   )
            textEdit = QTextEdit()
            textEdit.setStyleSheet("border: 1px solid black;")
            botonCerrar = QPushButton()
            a="QPushButton{border-image:url("+self.IMAGEN_ELIMINAR+");}"
            b="QPushButton:hover{border-image:url("+self.IMAGEN_ELIMINAR_2+");}"
            c="QPushButton:pressed{border-image:url("+self.IMAGEN_ELIMINAR+");}"
            botonCerrar.setStyleSheet(a+b+c)
            botonCerrar.setMaximumSize(20,20)
            botonCerrar.setMinimumSize(20,20)
            textEdit.setText(texto)
            checkBox.setChecked(estado)
            newItemRoniano=itemRoniano(self.contadorIdsVivosMuertos,checkBox,textEdit,botonCerrar)
            self.listIdsItemsVivos.append(self.contadorIdsVivosMuertos)
            newItemRoniano.suHoraMorir.connect(self.borrarItem)
            self.listaItemsRonianos.append(newItemRoniano)
            #addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
            gridLayout.addWidget(botonCerrar,0,0,1,-1,alignment=QtCore.Qt.AlignRight)
            gridLayout.addWidget(checkBox,1,0,1,1)
            gridLayout.addWidget(textEdit,1,1,-1,-1)
            gridLayout.setContentsMargins(0, 0, 0, 0)  # Set the zero padding
            self.vbox.addWidget(widget)
            #agregamos el edit text por paso por referencia...
            vectorColumna = np.array([[textEdit]]).reshape(1,1)
            self.matrizEditTextRespuestas=np.append(self.matrizEditTextRespuestas,vectorColumna, axis=1)
            print(self.matrizEditTextRespuestas.shape)
            self.controlABSOLUTO_editTextRespuestas.matrizEditText=self.matrizEditTextRespuestas
            self.controlABSOLUTO_editTextRespuestas.refrescarPosEditText(0)
            self.punteroNoItems+=1
            self.contadorIdsVivosMuertos+=1
            self.controlABSOLUTO_editTextRespuestas.cambiarTam(self.dSpin_respTam.value())


        else:
            QMessageBox.question(self, "DelphiPreguntas",
                                 "El numero maximo de items es de:\n"
                                 f"{self.MAX_ITEMS} items, y usted ya ha llegado\n"
                                 "a dicho limite.",
                                 QMessageBox.Ok)

    def borrarItem(self,idItemAMatar):
        posItemMatar=self.listIdsItemsVivos.index(idItemAMatar)
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quieres\n"
                                         f"eliminar el item numero {posItemMatar+1}?",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            layout=self.vbox
            noWidgetBorrar=posItemMatar
            widgetToRemove = layout.itemAt(noWidgetBorrar).widget()
            # remove it from the layout list
            layout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

            self.listaItemsRonianos.pop(posItemMatar)
            self.listIdsItemsVivos.pop(posItemMatar)
            print("Matriz a abortaar",self.matrizEditTextRespuestas.shape)
            self.matrizEditTextRespuestas=np.delete(self.matrizEditTextRespuestas,posItemMatar,1)
            print("Matriz despues de abortar",self.matrizEditTextRespuestas.shape)
            self.controlABSOLUTO_editTextRespuestas.matrizEditText = self.matrizEditTextRespuestas
            self.punteroNoItems -= 1

    def cambioHibridoPregunta(self,idBtnFuePresionado):
        resultado=QMessageBox.Yes
        if self.NUEVA_PREGUNTA==False:
            resultado = QMessageBox.question(self, "DelphiPreguntas",
                                             "¿Esta seguro que quiere cambiar al formato \n"
                                             f"de pregunta: '{self.listNombres_preguntasHibridas[idBtnFuePresionado]}' ?\n",
                                             QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.PROPIEDADES_PREGUNTA["GRADO_IMAGENES"] = idBtnFuePresionado  # 0=sin imagen 1=con imagen en pregunta....
            # actulizando contenido de respuestas
            self.listWidget_panelVersion.setCurrentIndex(idBtnFuePresionado)
            self.control.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado, False)
            #cargando el texto del edit text del widget al que nos pasaremos...
            self.textPregunta= self.matrizEditTextPreguntas[self.punteroWidget][0].toPlainText()
            self.matrizEditTextPreguntas[self.punteroWidget][0].setText(self.textPregunta)
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
                if imagenPregunta != None:
                    imagenPregunta = self.DIREC_IMAGENES + imagenPregunta
                self.ventanas[idBtnFuePresionado].controlABSOLUTO_labelImagen.escogioImagen(0, False,imagenPregunta)






if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaCheckBox()
    application.show()
    app.exec()
    #sys.exit(app.exec())





#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke
