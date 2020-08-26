from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout,QTextEdit,QCheckBox,QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespCheckBoxImagen50_d  import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

from PyQt5.QtCore import Qt, pyqtSignal, QFile
from functools import partial

from comporEdit_TextEdit import comporEdit_TextEdit
from comporSelecBtnsResp import comporSelecBtnsResp
#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from functools import partial
import numpy as np
from PyQt5.QtWidgets import  QMessageBox


###############################################################################################################
#   NUESTROS PAQUETES...
###############################################################################################################
from comportSelectImagen_label import comportSelectImagen_label



#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaCheckBoxImagen_50(QtWidgets.QWidget, Ui_Form):
    alguienEligioImagen = pyqtSignal(list)  # idLabelEscogioImagen/direcImagenGuardada/NO_LABELS_IMAGEN
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.NO_LABELS_IMAGEN = 1

        self.vectorRenglon_labelsImagen=np.array([[self.bel_pregImage]]).reshape(1,1)


        self.controlABSOLUTO_labelImagen=comportSelectImagen_label(self,
                                                                 self.vectorRenglon_labelsImagen,
                                                                 "Roni",
                                                                 "HOLA",
                                                                "ICONOS/icon_escogerImagen.png")

        self.controlABSOLUTO_labelImagen.alguienEligioImagen.connect(self.notificarMain)

    def notificarMain(self,listaInformacion):
        listaInformacion.append(self.NO_LABELS_IMAGEN)
        self.alguienEligioImagen.emit(listaInformacion)
        idLabelEligioImagen=listaInformacion[0]
        direcGuardoImagen=listaInformacion[1]
        print("Label:",idLabelEligioImagen," Direc: ",direcGuardoImagen)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaCheckBoxImagen_50()
    application.show()
    app.exec()
    #sys.exit(app.exec())