from functools import partial
from PyQt5 import QtWidgets, QtGui, Qt, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem  # para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiplesImagen0_d import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

from PyQt5.QtCore import Qt, pyqtSignal, QFile,QObject
from functools import partial

# Comportamiento de selecciones de botones....
class comporSelec_btnsImagen(QObject):
    botonFuePresionado = pyqtSignal(int)
    def __init__(self, listBtnResp,listImageBtn):
        QObject.__init__(self)

        self.COLOR_NORMAL = "#EEF2F3"
        self.COLOR_SELECCION = "#9AE5E0"
        self.BORDER_RADIUS="7"
        self.automatico_activado=False

        # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.listBtnResp =listBtnResp
        self.listImageBtn=listImageBtn
        self.btnElegido=-1
        for x in range(len(self.listBtnResp)):
            self.listBtnResp[x].clicked.connect(partial(self.marcarDesmarcarRespuesta_automatico,x,True))
            self.listBtnResp[x].clicked.connect(partial(self.botonPresionado,x))

###################################################################################################
#   S E C C I O N     BOTONES SELECCIONADOS
####################################################################################################
    def botonPresionado(self,idBtnRespuesta):
        if idBtnRespuesta!=self.btnElegido:
            self.botonFuePresionado.emit(idBtnRespuesta)

    def marcarDesmarcarRespuesta_automatico(self,idBtnRespuesta,ordenAutomatica):
        print("boton:",idBtnRespuesta)
        if (self.automatico_activado and ordenAutomatica) or not(ordenAutomatica):
            if self.btnElegido!=idBtnRespuesta:
                self.listBtnResp[self.btnElegido].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                       f"border-radius:{self.BORDER_RADIUS}px;"
                                                                       #"border: 1px solid #555;"
                                                                f"border-image: url({self.listImageBtn[self.btnElegido]});")
                self.btnElegido=idBtnRespuesta
                self.listBtnResp[self.btnElegido].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                       f"border-radius:{self.BORDER_RADIUS}px;"
                                                                       #"border: 1px solid #555;"
                                                                f"border-image: url({self.listImageBtn[self.btnElegido]});")

