from PyQt5 import QtGui, Qt
from PyQt5.QtCore import Qt
from functools import partial


# DISENO DE LOS MULTIPLES TIPOS DE PREGUNTAS


# Comportamiento de las ediciones de un edit text...
class comportEditTextEdit():
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

    def __init__(self, vectorRenglon_btnAlin, dSpinEditTam, matrizEditText,listImageBtn):

        self.COLOR_NORMAL = "#EEF2F3"
        self.COLOR_SELECCION = "#9AE5E0"


        self.vectorRenglon_btnAlin =vectorRenglon_btnAlin
        self.dSpinEditTam = dSpinEditTam
        self.matrizEditText = matrizEditText
        self.listImageBtn = listImageBtn

        # Posicion del texto de  la pregunta...
        self.punteroPOS = 1  # 0=izquierda 1=centro 2=derecha

        #Conectando los botones que tendran el control de la alineacion del texto...
        for x in range(self.vectorRenglon_btnAlin.shape[1]):
            self.vectorRenglon_btnAlin[0][x].clicked.connect(partial(self.editPosEditsText, x))
        self.editPosEditsText(1)

        #Estableciendo tamanos por default...
        self.dSpinEditTam.setMinimum(10)
        self.dSpinEditTam.setMaximum(40)
        self.dSpinEditTam.setValue(15)
        self.dSpinEditTam.valueChanged.connect(self.cambiarTam)
        self.cambiarTam(15)

###################################################################################################
#   S E C C I O N     DISENO DE PREGUNTAS Y RESPUESTAS
####################################################################################################
    def cambiarTam(self, newValor):
        if self.matrizEditText.shape[1]>0:
            # Cambiando el tamaño
            font = QtGui.QFont()
            font.setPointSize(int(newValor))
            for renglon in range(self.matrizEditText.shape[0]):
                for columna in range(self.matrizEditText.shape[1]):
                    self.matrizEditText[renglon][columna].setFont(font)

    def refrescarPosEditText(self,widgetNo):
        posicion=self.punteroPOS
        if self.matrizEditText.shape[1]>0:
            if posicion == 0:
                for columna in range(self.matrizEditText.shape[1]):
                    self.matrizEditText[widgetNo][columna].setAlignment(Qt.AlignLeft)
            elif posicion == 1:
                for columna in range(self.matrizEditText.shape[1]):
                    self.matrizEditText[widgetNo][columna].setAlignment(Qt.AlignHCenter)
            elif posicion == 2:
                for columna in range(self.matrizEditText.shape[1]):
                    self.matrizEditText[widgetNo][columna].setAlignment(Qt.AlignRight)

    def editPosEditsText(self, newPosicion):
        if self.matrizEditText.shape[1] > 0:
            if newPosicion == 0:
                for renglon in range(self.matrizEditText.shape[0]):
                    for columna in range(self.matrizEditText.shape[1]):
                        self.matrizEditText[renglon][columna].setAlignment(Qt.AlignLeft)
            elif newPosicion == 1:
                for renglon in range(self.matrizEditText.shape[0]):
                    for columna in range(self.matrizEditText.shape[1]):
                        self.matrizEditText[renglon][columna].setAlignment(Qt.AlignHCenter)
            elif newPosicion == 2:
                for renglon in range(self.matrizEditText.shape[0]):
                    for columna in range(self.matrizEditText.shape[1]):
                        self.matrizEditText[renglon][columna].setAlignment(Qt.AlignRight)

        self.vectorRenglon_btnAlin[0][self.punteroPOS].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                         f"border-image: url({self.listImageBtn[self.punteroPOS]});")
        self.punteroPOS = newPosicion
        self.vectorRenglon_btnAlin[0][self.punteroPOS].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                         f"border-image: url({self.listImageBtn[self.punteroPOS]});")