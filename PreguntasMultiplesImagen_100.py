from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiplesImagen100_d import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from comporEdit_TextEdit import comporEdit_TextEdit
from comporSelecBtnsResp import comporSelecBtnsResp

import numpy as np
from PyQt5.QtCore import Qt, pyqtSignal, QFile,QObject
###############################################################################################################
#   NUESTROS PAQUETES...
###############################################################################################################
from comportSelectImagen_label import comportSelectImagen_label


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiplesImagen100(QtWidgets.QWidget, Ui_Form):
    alguienEligioImagen = pyqtSignal(list)  # idLabelEscogioImagen/direcImagenGuardada
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.vectorRenglon_labelsImagen=np.array([[self.bel_pregImage,self.bel_imageRespA,self.bel_imageRespB,
                                                   self.bel_imageRespC,self.bel_imageRespD]]).reshape(1,5)



        self.controlABSOLUTO_labelImagen=comportSelectImagen_label(self,
                                                                   self.vectorRenglon_labelsImagen,
                                                                   "Roni",
                                                                   "HOLA",
                                                                   "ICONOS/icon_escogerImagen.png")

        self.controlABSOLUTO_labelImagen.alguienEligioImagen.connect(self.notificarMain)

    def notificarMain(self,listaInformacion):
        self.alguienEligioImagen.emit(listaInformacion)
        idLabelEligioImagen=listaInformacion[0]
        direcGuardoImagen=listaInformacion[1]
        print("Label:",idLabelEligioImagen," Direc: ",direcGuardoImagen)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiplesImagen100()
    application.show()
    app.exec()
    #sys.exit(app.exec())


'''


        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPosPreg = (self.btn_pregIzq, self.btn_pregCen, self.btn_pregDer)
        self.control = comporEdit_TextEdit(self.listBtnPosPreg, self.dSpin_pregTam, [self.txtEdit_preg])

        # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.listBtnPunterosResp = (self.btn_respA, self.btn_respB, self.btn_respC, self.btn_respD)
        self.control3 = comporSelecBtnsResp(self.listBtnPunterosResp)






'''