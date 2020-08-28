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

    def __init__(self,matrizBotones,BORDER_RADIUS = "7",seleccionBotonesMultiple=True):

        self.COLOR_NORMAL = "#EEF2F3"
        self.COLOR_SELECCION = "#9AE5E0"
        self.BORDER_RADIUS = BORDER_RADIUS

        # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.matrizBotones =matrizBotones

        self.ultimoBotonPresionado=-1

        self.seleccionMultiple=seleccionBotonesMultiple # 0 puede seleccionar mas de un boton...
                                                    # solo puede seleccionar uno...

        self.listRespCorrectas=[]
        # todas inicialmente son consideradas
        # incorrectas...
        for _ in range(self.matrizBotones.shape[1]):
            self.listRespCorrectas.append(0)#0=False,1=True


        for c in range(self.matrizBotones.shape[1]):  # columnas
            for r in range(self.matrizBotones.shape[0]):  # renglones
                self.matrizBotones[r][c].clicked.connect(partial(self.marcarDesmarcarRespuesta, c))

        self.incializar()

###################################################################################################
#   S E C C I O N     BOTONES SELECCIONADOS
####################################################################################################

    def dameTodoLoQueRespondio(self):
        return self.listRespCorrectas.copy()

    def dameLaRespuestaEscogio(self):
        posBotonEscogio=self.ultimoBotonPresionado
        return posBotonEscogio

    def getRespuesta(self):
        if self.seleccionMultiple==True: #0==>mas de uno  1==>solo uno
            return self.listRespCorrectas.copy()
        else:
            posBotonEscogio=self.ultimoBotonPresionado
            return posBotonEscogio


    def marcarDesmarcarRespuesta(self,idBtnRespuesta):
        if self.seleccionMultiple==True: #0==>mas de uno  1==>solo uno
            if self.listRespCorrectas[idBtnRespuesta] == True:  # 0=False,1=True
                self.listRespCorrectas[idBtnRespuesta] = 0  # 0=False,1=True
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                        f"border-radius:{self.BORDER_RADIUS}px;"
                                                                        "border: 1px solid #555;")
            else:
                self.listRespCorrectas[idBtnRespuesta] = 1  # 0=False,1=True
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                        f"border-radius:{self.BORDER_RADIUS}px;"
                                                                        "border: 1px solid #555;")
        else: #0==>mas de uno  1==>solo uno
            # si el boton que tratan de seleccionar no fue seleccionado
            if self.ultimoBotonPresionado != idBtnRespuesta and idBtnRespuesta >= 0:
                self.listRespCorrectas[idBtnRespuesta] = 1  # 0=False,1=True
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][self.ultimoBotonPresionado].setStyleSheet(
                        f"background-color:{self.COLOR_NORMAL};"
                        f"border-radius:{self.BORDER_RADIUS}px;"
                        "border: 1px solid #555;")
                self.ultimoBotonPresionado = idBtnRespuesta
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][self.ultimoBotonPresionado].setStyleSheet(
                        f"background-color:{self.COLOR_SELECCION};"
                        f"border-radius:{self.BORDER_RADIUS}px;"
                        "border: 1px solid #555;")

    def setAllRespuestas(self,newValue):
        self.listRespCorrectas=newValue
        for idBtnRespuesta in range(len(self.listRespCorrectas)):
            if self.listRespCorrectas[idBtnRespuesta]==True:
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                        f"border-radius:{self.BORDER_RADIUS}px;"
                                                                       "border: 1px solid #555;")
            else:
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                        f"border-radius:{self.BORDER_RADIUS}px;"
                                                                        "border: 1px solid #555;")

    def incializar(self):
        for columna in range(self.matrizBotones.shape[1]):  # columnas...
            for renglon in range(self.matrizBotones.shape[0]): #renglones...
                self.matrizBotones[renglon][columna].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                   f"border-radius:{self.BORDER_RADIUS}px;"
                                                                   "border: 1px solid #555;")


    def setColor(self, newColor):
        self.COLOR_SELECCION=newColor #actualizando el color...
        for columna in range(self.matrizBotones.shape[1]):  # columnas...
            if self.listRespCorrectas[columna]==True:
                for renglon in range(self.matrizBotones.shape[0]): #renglones...
                    self.matrizBotones[renglon][columna].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                       f"border-radius:{self.BORDER_RADIUS}px;"
                                                                       "border: 1px solid #555;")
