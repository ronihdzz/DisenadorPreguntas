# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       guardarImagen.py
# Autor:        Miguel Andres Garcia Niño
# Creado:       09 de Mayo 2018
# Modificado:   09 de Mayo 2018
# Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# License:      Apache License 2.0
# ----------------------------------------------------------------------------

__versión__ = "1.0"

"""
El módulo *guardarImagen* permite guardar en una una base de datos (SQLite) nombres
de usuarios y en una carpeta aparte guardar la foto con el ID del usuario.
"""

from os import getcwd, makedirs
from sqlite3 import connect

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QFile
from PyQt5.QtWidgets import (QApplication, QDialog, QLabel, QPushButton, QFileDialog,
                             QLabel, QLineEdit, QMessageBox)


# ===================== CLASE QLabelClickable ======================

class QLabelClickable(QLabel):
    clicked = pyqtSignal()
    
    def __init__(self, parent=None):
        super(QLabelClickable, self).__init__(parent)

    def mousePressEvent(self, event):
        self.clicked.emit()


# ==================== CLASE recuperarImagen =======================

class guardarImagen(QDialog):
    def __init__(self, parent=None):
        super(guardarImagen, self).__init__(parent)
        
        self.setWindowTitle("Guardar imagen en una carpeta por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("icono.png"))
        self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(400, 511)

        self.initUI()

    def initUI(self):

      # ==================== WIDGET QLABEL =======================
        
        self.labelImagen = QLabelClickable(self)
        self.labelImagen.setGeometry(15, 15, 168, 180)
        self.labelImagen.setToolTip("Imagen")
        self.labelImagen.setCursor(Qt.PointingHandCursor)

        self.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid "
                                       "#01DFD7; border-radius: 2px;}")
        
        self.labelImagen.setAlignment(Qt.AlignCenter)

      # ==================== WIDGETS QLABEL ======================

        labelNombre = QLabel("Nombre de usuario", self)
        labelNombre.move(193, 15)

      # ================== WIDGETS QLINEEDIT =====================

        self.lineEditNombre = QLineEdit(self)
        self.lineEditNombre.setGeometry(193, 30, 192, 25)

      # ================= WIDGETS QPUSHBUTTON ====================

        buttonSeleccionar = QPushButton("Seleccionar", self)
        buttonSeleccionar.setToolTip("Seleccionar imagen")
        buttonSeleccionar.setCursor(Qt.PointingHandCursor)
        buttonSeleccionar.setGeometry(15, 200, 168, 25)

        buttonBuscar = QPushButton("Buscar", self)
        buttonBuscar.setToolTip("Buscar usuario")
        buttonBuscar.setCursor(Qt.PointingHandCursor)
        buttonBuscar.setGeometry(193, 60, 93, 25)

        buttonGuardar = QPushButton("Guardar", self)
        buttonGuardar.setToolTip("Guardar usuario")
        buttonGuardar.setCursor(Qt.PointingHandCursor)
        buttonGuardar.setGeometry(292, 60, 93, 25)

      # ===================== EVENTO QLABEL ======================

      # Llamar función al hacer clic sobre el label
        self.labelImagen.clicked.connect(self.seleccionarImagen)

      # ================== EVENTOS QPUSHBUTTON ===================

        buttonSeleccionar.clicked.connect(self.seleccionarImagen)
        buttonGuardar.clicked.connect(self.Guardar)
     

  # ======================= FUNCIONES ============================

    def seleccionarImagen(self):
        imagen, extension = QFileDialog.getOpenFileName(self, "Seleccionar imagen", getcwd(),
                                                        "Archivos de imagen (*.png *.jpg)",
                                                        options=QFileDialog.Options())
          
        if imagen:
            # Adaptar imagen
            pixmapImagen = QPixmap(imagen).scaled(166, 178, Qt.KeepAspectRatio,
                                                  Qt.SmoothTransformation)

            # Mostrar imagen
            self.labelImagen.setPixmap(pixmapImagen)


    def Guardar(self):
        # Obtener el nombre de usuario y la foto
        foto = self.labelImagen.pixmap()  #obteniendo la imagen de la label

        if foto:
            # Verificar si existe la carpeta Fotos, sino existe la creamos
            if not QFile.exists("Fotos"):
                makedirs("Fotos")

            # Guardar la foto
            #cabe aclarar que la variable foto en un objeto de pixmap
            #estamos guardando la imagen en la carpeta fotos con la extension .png
            #conservando toda su calidad...
            foto.save("Fotos/{}.png".format("1"), quality = 100)

            self.labelImagen.clear()

            QMessageBox.information(self, "Guardar imagen", "Usuario guardado con éxito.",
                                    QMessageBox.Ok)




# ================================================================

if __name__ == '__main__':
    
    import sys
    
    aplicacion = QApplication(sys.argv)
    
    ventana = guardarImagen()
    ventana.show()
    
    sys.exit(aplicacion.exec_())
