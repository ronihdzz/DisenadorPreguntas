from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap

from menuTipoPreguntas import menuTipoPreguntas
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
                             QLabel, QLineEdit, QMessageBox)
from os import getcwd, makedirs
from functools import partial

from comporSelecBtnsResp import comporSelecBtnsResp
from comporEdit_TextEdit import comporEdit_TextEdit

from PyQt5.QtCore import Qt, pyqtSignal, QFile,QObject
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
                             QLabel, QLineEdit, QMessageBox)

#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from DISENOS.modRespBinariaImagen50_d import Ui_Form
import numpy as np

###############################################################################################################
#   NUESTROS PAQUETES...
###############################################################################################################
from comportSelectImagen_label import comportSelectImagen_label


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaBinariaImagen_50(QtWidgets.QWidget, Ui_Form):
    alguienEligioImagen = pyqtSignal(list)  # idLabelEscogioImagen/direcImagenGuardada

    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.vectorRenglon_labelsImagen=np.array([[self.bel_pregImage]]).reshape(1,1)


        self.controlABSOLUTO_pregImagen=comportSelectImagen_label(self,
                                                                 self.vectorRenglon_labelsImagen,
                                                                 "Roni",
                                                                 "HOLA",
                                                                "ICONOS/icon_escogerImagen.png")

        self.controlABSOLUTO_pregImagen.alguienEligioImagen.connect(self.notificarMain)

    def notificarMain(self,listaInformacion):
        self.alguienEligioImagen.emit(listaInformacion)
        idLabelEligioImagen=listaInformacion[0]
        direcGuardoImagen=listaInformacion[1]



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaBinariaImagen_50()
    application.show()
    app.exec()
    #sys.exit(app.exec())

