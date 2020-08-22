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
import numpy as np

from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
                             QLabel, QLineEdit, QMessageBox)
from PyQt5.QtCore import Qt, pyqtSignal, QFile,QObject
from os import getcwd, makedirs

from datetime import datetime


class ImagenClick(QObject):
    clicked = pyqtSignal(int)
    def __init__(self,punteroQLabelGui,idImagen):
        QObject.__init__(self)
        self.idImagen = idImagen
        self.punteroQLabelGui=punteroQLabelGui
        self.punteroQLabelGui.mousePressEvent=self.mandarSenalDelClick

    def mandarSenalDelClick(self, event):
        self.clicked.emit(self.idImagen)








# Comportamiento de selecciones de botones....
class comportSelectImagen_label(QObject):
    alguienEligioImagen = pyqtSignal(list) #idLabelEscogioImagen/direcImagenGuardada

    def __init__(self,context,vectorRenglon_labels,infoUnica,direcGuardado,direcImagenDefault):
        QObject.__init__(self)

        self.vectorRenglon_labels=vectorRenglon_labels
        self.context=context
        self.infoUnica=infoUnica
        self.direcGuardado=direcGuardado
        self.direcImagenDefault=direcImagenDefault

        ancho=self.vectorRenglon_labels[0][0].width()
        alto=self.vectorRenglon_labels[0][0].height()
        size=(ancho,alto)
        self.vectorRenglon_sizes=np.array([[size]])
        for n in range(1,self.vectorRenglon_labels.shape[1]):
            ancho = self.vectorRenglon_labels[0][n].width()
            alto = self.vectorRenglon_labels[0][n].height()
            size = (ancho, alto)
            vector = np.array([[size]])
            self.vectorRenglon_sizes = np.append(self.vectorRenglon_sizes,vector, axis=1)

        for n in range(self.vectorRenglon_labels.shape[1]):
            self.vectorRenglon_labels[0][n]=ImagenClick(self.vectorRenglon_labels[0][n],n)
            self.vectorRenglon_labels[0][n].clicked.connect(self.escogioImagen)
            self.ponerImagenDefault(n)




    def getIdImagen(self):
        now = datetime.now()
        # Tiempo apartir del 2020 cuando inicio el juego
        secondYears_50 = 50 * 365 * 24 * 60 * 60
        timeApartir2020 = now.timestamp() - secondYears_50
        redondeo_4 = int(timeApartir2020 * 1000.0)
        return self.infoUnica+"_"+str(redondeo_4)

    def guardarImagen(self,imagen):

            # Verificar si existe la carpeta Fotos, sino existe la creamos
            #if not QFile.exists("Fotos"):
            #    makedirs("Fotos")

            # Guardar la foto
            # cabe aclarar que la variable foto en un objeto de pixmap
            # estamos guardando la imagen en la carpeta fotos con la extension .png
            # conservando toda su calidad...
            nombreImagen = self.getIdImagen()
            nameImagenGuardar =self.direcGuardado+"/"+nombreImagen + ".png"
            imagen.save(nameImagenGuardar, quality=100)
            return nameImagenGuardar


    def escogioImagen(self,idLabelEscogio):
        imagen, extension = QFileDialog.getOpenFileName(self.context, "Seleccionar imagen", getcwd(),
                                                        "Archivos de imagen (*.png *.jpg)",
                                                        options=QFileDialog.Options())
        if imagen:
            # Adaptar imagen
            ancho,alto= self.vectorRenglon_sizes[0][idLabelEscogio]

            # pixmapImagen = QPixmap(imagen).scaled(ancho*0.9,alto*0.9, Qt.KeepAspectRatio,
            #                                     Qt.SmoothTransformation)

            pixmapImagen = QPixmap(imagen).scaled(ancho * 0.95, alto * 0.95, Qt.IgnoreAspectRatio,
                                                  Qt.SmoothTransformation)
            # Mostrar imagen por medio de los punteros labels...
            self.vectorRenglon_labels[0][idLabelEscogio].punteroQLabelGui.setAlignment(Qt.AlignCenter)
            self.vectorRenglon_labels[0][idLabelEscogio].punteroQLabelGui.setPixmap(pixmapImagen)

            direccionImagenGuardada=self.guardarImagen( QPixmap(imagen) )
            self.alguienEligioImagen.emit([idLabelEscogio,direccionImagenGuardada])


    def ponerImagenDefault(self,idLabel):
        # Adaptar imagen
        ancho, alto = self.vectorRenglon_sizes[0][idLabel]

        # pixmapImagen = QPixmap(imagen).scaled(ancho*0.9,alto*0.9, Qt.KeepAspectRatio,
        #                                     Qt.SmoothTransformation)

        pixmapImagen = QPixmap(self.direcImagenDefault).scaled(ancho * 0.95, alto * 0.95, Qt.IgnoreAspectRatio,
                                              Qt.SmoothTransformation)
        # Mostrar imagen por medio de los punteros labels...
        self.vectorRenglon_labels[0][idLabel].punteroQLabelGui.setAlignment(Qt.AlignCenter)
        self.vectorRenglon_labels[0][idLabel].punteroQLabelGui.setPixmap(pixmapImagen)







'''
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
'''
