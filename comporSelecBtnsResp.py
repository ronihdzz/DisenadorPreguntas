from functools import partial
from PyQt5 import QtWidgets, QtGui, Qt, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem  # para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiplesImagen0_d import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

from PyQt5.QtCore import Qt, pyqtSignal, QFile
from functools import partial

# Comportamiento de selecciones de botones....
class comporSelecBtnsResp():
    # quierePreguntaImagen = pyqtSignal()
    # listEditText,listBtn
    '''
    1)lisBtnResp ==> Lista de los botones que representan
    a la respuesta correcta...

    '''

    def __init__(self, listBtnResp):

        self.COLOR_NORMAL = "#EEF2F3"
        self.COLOR_SELECCION = "#9AE5E0"

        # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.listBtnResp =listBtnResp

        self.listRespCorrectas=[]
        # todas inicialmente son consideradas
        # incorrectas...
        for _ in self.listBtnResp:
            self.listRespCorrectas.append(False)

        for x in range(len(self.listBtnResp)):
            self.listBtnResp[x].clicked.connect(partial(self.marcarDesmarcarRespuesta, x))

###################################################################################################
#   S E C C I O N     BOTONES SELECCIONADOS
####################################################################################################
    def marcarDesmarcarRespuesta(self,idBtnRespuesta):
        print("boton:",idBtnRespuesta)
        if self.listRespCorrectas[idBtnRespuesta]==True:
            self.listRespCorrectas[idBtnRespuesta]=False
            self.listBtnResp[idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                   "border-radius: 20px;"
                                                                   "border: 1px solid #555;")
        else:
            self.listRespCorrectas[idBtnRespuesta]=True
            self.listBtnResp[idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                   f"border-radius: 20px;"
                                                                   "border: 1px solid #555;")