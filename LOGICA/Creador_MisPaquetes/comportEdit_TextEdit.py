from functools import partial
from PyQt5 import QtWidgets, QtGui, Qt, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem  # para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENO.modRespMultiplesImagen0_d import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

from PyQt5.QtCore import Qt, pyqtSignal, QFile
from functools import partial


# DISENO DE LOS MULTIPLES TIPOS DE PREGUNTAS


# Comportamiento de las ediciones de un edit text...
class comporEdit_TextEdit():
    # quierePreguntaImagen = pyqtSignal()
    # listEditText,listBtn
    '''
    1)lisBtnAlin ==> Lista de los botones de alineacion
        Esta lista debe respetar el siguiente orden...
        [botonAlineacionIzquierda,botonAlineacionCentrada,botonAlineacionDerecha]
    3)Double Spin ==>para editar el texto

    2)listEdit ==> Lista de los edit text a los cuales los botones
      controlaran de forma uniforme
    '''

    def __init__(self, listBtnAlin, dSpin_editTam, listEditText):

        self.COLOR_NORMAL = "#EEF2F3"
        self.COLOR_SELECCION = "#9AE5E0"

        # Iconos de las imagenes...
        self.listImagBtnPos = ["ICONOS/alinear_izquierda.png",
                               "ICONOS/alinear_centrar.png",
                               "ICONOS/alinear_derecho.png"
                               ]
        self.listBtnAlin = listBtnAlin
        self.dSpin_editTam = dSpin_editTam
        self.listEditText = listEditText

        # Posicion del texto de  la pregunta...
        self.posPregunta = 1  # 0=izquierda 1=centro 2=derecha

        for x in range(len(self.listBtnAlin)):
            self.listBtnAlin[x].clicked.connect(partial(self.editPosEditsText, x))
        self.editPosEditsText(1)

        # Cambiar tamaño de pregunta....
        self.dSpin_editTam.setMinimum(8)
        self.dSpin_editTam.setMaximum(40)
        self.dSpin_editTam.setValue(15)
        self.cambiarTam(15)
        self.dSpin_editTam.valueChanged.connect(self.cambiarTam)

###################################################################################################
#   S E C C I O N     DISENO DE PREGUNTAS Y RESPUESTAS
####################################################################################################

    def cambiarTam(self, newValor):
        # Cambiando el tamaño
        font = QtGui.QFont()
        font.setPointSize(int(newValor))
        for cadaTextEdit in self.listEditText:
            cadaTextEdit.setFont(font)

    def editPosEditsText(self, newPosicion):
        if newPosicion == 0:
            for cadaTextEdit in self.listEditText:
                cadaTextEdit.setAlignment(Qt.AlignLeft)
        elif newPosicion == 1:
            for cadaTextEdit in self.listEditText:
                cadaTextEdit.setAlignment(Qt.AlignHCenter)
        elif newPosicion == 2:
            for cadaTextEdit in self.listEditText:
                cadaTextEdit.setAlignment(Qt.AlignRight)
        self.listBtnAlin[self.posPregunta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                         f"border-image: url({self.listImagBtnPos[self.posPregunta]});")
        self.posPregunta = newPosicion
        self.listBtnAlin[self.posPregunta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                         f"border-image: url({self.listImagBtnPos[self.posPregunta]});")