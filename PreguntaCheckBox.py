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

        self.punteroWidget=0

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
        self.dSpin_pregTam.setMinimum(8)
        self.dSpin_pregTam.setMaximum(40)
        self.dSpin_pregTam.setValue(15)

####################################################################################################################################
#       C O N T R O L    D E     POSICIONES DE RESPUESTAS :
####################################################################################################################################
        # CREANDO LA MATRIZ DE EDIT TEXT...
        self.matrizEditTextRespuestas = np.empty((1,0),dtype=QTextEdit).reshape(1,0)
        print(self.matrizEditTextRespuestas.shape)
        # CREANDO EL VECTOR REGLON DE BOTONES ALIGN...
        ## Comportamiento de las ediciones de un edit text...
        self.vectorRenglon_btnAlignRespuestas = np.array([[self.btn_respIzq, self.btn_respCen, self.btn_respDer]])

        self.controlABSOLUTO_editTextRespuestas = comportEditTextEdit(self.vectorRenglon_btnAlignRespuestas,
                                                                      self.dSpin_respTam,
                                                                      self.matrizEditTextRespuestas)
        self.dSpin_respTam.setMinimum(8)
        self.dSpin_respTam.setMaximum(25)
        self.dSpin_respTam.setValue(15)
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
        self.btn_addCheckBox.clicked.connect(self.agregarCheckBox)

        self.listaItemsRonianos=[]
        self.textPregunta=""
        self.listIdsItemsVivos=[]



###########################################################################################################################
#
#
#       M    E     T     O     D     O     S    :
#
#
##############################################################################################################################

    def agregarCheckBox(self):
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
            botonCerrar = QPushButton()
            a="QPushButton{border-image:url("+self.IMAGEN_ELIMINAR+");}"
            b="QPushButton:hover{border-image:url("+self.IMAGEN_ELIMINAR_2+");}"
            c="QPushButton:pressed{border-image:url("+self.IMAGEN_ELIMINAR+");}"
            botonCerrar.setStyleSheet(a+b+c)
            botonCerrar.setMaximumSize(20,20)
            botonCerrar.setMinimumSize(20,20)
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
    application = PreguntaCheckBox()
    application.show()
    app.exec()
    #sys.exit(app.exec())



#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke
