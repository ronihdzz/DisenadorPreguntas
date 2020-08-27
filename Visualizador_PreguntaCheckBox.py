from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QGridLayout,QCheckBox,QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.VisualizadorCheckBox_d import Ui_Form
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


class itemRoniano_visualizador(QObject):
    def __init__(self,id,checkBox_estado,textEdit_texto):
        QObject.__init__(self)
        self.id=id
        self.checkBox_estado=checkBox_estado
        self.textEdit_texto=textEdit_texto


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class VisualizadorPregunta_CheckBox(QtWidgets.QWidget, Ui_Form):
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

        self.listaItemsRonianos=[]
        self.textPregunta=""
        self.listIdsItemsVivos=[]
        self.punteroWidget = 0




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
        #iterando sobre todos los items existentes....
        respuestas=[]
        estadoRespuesta=False
        for item in self.listaItemsRonianos:
            respuestas.append( int(item.checkBox_estado.isChecked()) )

        if respuestas==self.respuestasCorrectas:
            estadoRespuesta=True
        return estadoRespuesta

    def limpiarWidget(self):
        self.borrarTodosItems()
        if self.noWidgetAbrir>0: #1,2,3
            self.ventanas[self.noWidgetAbrir].controlABSOLUTO_labelImagen.ponerEnDafultTodasLabel()


    def abrirPregunta(self, datosPregunta, datosRespuesta):
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
        formaEvaluar=self.PROPIEDADES_PREGUNTA["FORMA_EVALUAR"]#esta siempre sera 0,(AND)....

        # RESPUESTAS...
        respuestasCorrectas = self.PROPIEDADES_PREGUNTA["RESPUESTAS"]
        if respuestasCorrectas!=None and respuestasCorrectas!="":
            respuestasCorrectas = [int(x) for x in respuestasCorrectas.split(",")]
            # R E S P U E S T A S :
            listItems=self.PROPIEDADES_RESPUESTA["TEXTO_ITEMS"]
            listItems=listItems.split(",")
            #Creando los items que son...
            for noItem in range(len(listItems)):
                self.agregarCheckBox(listItems[noItem])

            for n in range(len(self.listaItemsRonianos)):
                itemRoniano=self.listaItemsRonianos[n]
                textEdit=itemRoniano.textEdit_texto
                self.cambiarTam(textEdit, tamRespuesta)
                self.cambiarPosEditsText(textEdit, posRespuesta)
                textEdit.setReadOnly(True)

        #ATRIBUTOS QUE SI UTILIZARE...
        self.noWidgetAbrir=noWidgetAbrir
        self.respuestasCorrectas=respuestasCorrectas
        self.formaEvaluar=formaEvaluar



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
#  M E T O D O S     C H E C K    B O X
##############################################################################################################################

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
            newItemRoniano=itemRoniano_visualizador(self.contadorIdsVivosMuertos,checkBox,textEdit)
            self.listIdsItemsVivos.append(self.contadorIdsVivosMuertos)
            self.listaItemsRonianos.append(newItemRoniano)
            #addWidget (self, QWidget, row, column, rowSpan, columnSpan, Qt.Alignment alignment = 0)
            gridLayout.addWidget(checkBox,0,0,1,1)
            gridLayout.addWidget(textEdit,0,1,-1,-1)
            gridLayout.setContentsMargins(0, 0, 0, 0)  # Set the zero padding
            self.vbox.addWidget(widget)
            self.punteroNoItems+=1
            self.contadorIdsVivosMuertos+=1

        else:
            QMessageBox.question(self, "DelphiPreguntas",
                                 "El numero maximo de items es de:\n"
                                 f"{self.MAX_ITEMS} items, y usted ya ha llegado\n"
                                 "a dicho limite.",
                                 QMessageBox.Ok)

    def borrarTodosItems(self):
        print("BORRAREMOS ",self.punteroNoItems," items,,,")
        print("lista de posiciones...",self.listIdsItemsVivos)

        #Debemos hacer una copia a esa lista ya que cuando
        #estemos eliminando elemento por elemento puede
        #suceder un error...
        copyList=self.listIdsItemsVivos.copy()
        print("COPY...",copyList)

        for x in copyList:
            self.borrarItem(x,False)

    def borrarItem(self,idItemAMatar,ordenAutomatica=True):
        posItemMatar=self.listIdsItemsVivos.index(idItemAMatar)
        resultado=QMessageBox.Yes
        if ordenAutomatica:
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

##############################################################################################################################
#  DATOS DEFAULT...
##############################################################################################################################

    def datosDefault(self):
            datosPregunta={
                "GRADO_IMAGENES": 1,  # 0=sin imagen 1=con imagen en pregunta....
                "TIEMPO_SEGUNDOS": 60,
                "TEXTO_PREGUNTA": "¿Quien es Roni Hernandez?",
                "IMAGEN_PREGUNTA": "roni.png",
                "TAMANO_PREGUNTA": 15,
                "POSICION_PREGUNTA": 1,  # 0=left 1=center  2=rigth
                "TAMANO_RESPUESTA": 15,
                "POSICION_RESPUESTA":1,  # 0=left 1=center  2=rigth
                "FORMA_EVALUAR":0,  # 0=todas 1=cualquiera  ya que deben elegirse todas las opcciones correctas
                "RESPUESTAS": "0,0,1,0"
            }

            datosRespuesta={
                "TEXTO_ITEMS":"jorge,dilan,roni,gaby"
            }

            return datosPregunta,datosRespuesta


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = VisualizadorPregunta_CheckBox()
    application.show()
    app.exec()
    #sys.exit(app.exec())





#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke
