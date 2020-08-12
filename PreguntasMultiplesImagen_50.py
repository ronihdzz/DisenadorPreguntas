from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiplesImagen50_d  import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
                             QLabel, QLineEdit, QMessageBox)
from os import getcwd, makedirs
from functools import partial

from comporSelecBtnsResp import comporSelecBtnsResp
from comporEdit_TextEdit import comporEdit_TextEdit


#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiplesImagen50(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPosPreg = (self.btn_pregIzq, self.btn_pregCen, self.btn_pregDer)
        self.control = comporEdit_TextEdit(self.listBtnPosPreg, self.dSpin_pregTam, [self.txtEdit_preg])

        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPosResp = (self.btn_respIzq, self.btn_respCen, self.btn_respDer)
        self.control2 = comporEdit_TextEdit(self.listBtnPosResp, self.dSpin_respTam,
                                            [self.txtEdit_respA, self.txtEdit_respB, self.txtEdit_respC,
                                             self.txtEdit_respD])

        # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.listBtnPunterosResp = (self.btn_respA, self.btn_respB, self.btn_respC, self.btn_respD)
        self.control3 = comporSelecBtnsResp(self.listBtnPunterosResp)

        #Botones...
        self.btn_pregImage.clicked.connect(self.seleccionarImagen)


    def seleccionarImagen(self):
        imagen, extension = QFileDialog.getOpenFileName(self, "Seleccionar imagen", getcwd(),
                                                        "Archivos de imagen (*.png *.jpg)",
                                                        options=QFileDialog.Options())
        if imagen:
            # Adaptar imagen
            ancho=self.bel_pregImage.width()
            alto=self.bel_pregImage.height()

            #pixmapImagen = QPixmap(imagen).scaled(ancho*0.9,alto*0.9, Qt.KeepAspectRatio,
            #                                     Qt.SmoothTransformation)

            pixmapImagen = QPixmap(imagen).scaled(ancho*0.95,alto*0.95, Qt.IgnoreAspectRatio,
                                                 Qt.SmoothTransformation)

            #Qt::IgnoreAspectRatio	0 El tamaño se escala libremente.
            # La relación de aspecto no se conserva.

            #Qt::KeepAspectRatio	1	El tamaño se escala a un rectángulo lo más
            # grande posible dentro de un rectángulo dado, conservando la relación
            # de aspecto.

            #QPixmap QPixmap::scaled(int width, int height,
            # Qt::AspectRatioMode aspectRatioMode = Qt::IgnoreAspectRatio,
            # Qt::TransformationMode transformMode = Qt::FastTransformation)

            #Qt::FastTransformation	0	La transformación se realiza rápidamente,
            # sin suavizado.
            # Qt::SmoothTransformation	1 La imagen resultante se transforma
            # mediante filtrado bilineal.

            # Mostrar imagen
            self.bel_pregImage.setAlignment(Qt.AlignCenter)
            self.bel_pregImage.setPixmap(pixmapImagen)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiplesImagen50()
    application.show()
    app.exec()
    #sys.exit(app.exec())
