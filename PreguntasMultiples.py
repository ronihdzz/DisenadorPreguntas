from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...

from PyQt5.QtGui import QIcon, QPixmap
from DISENOS.modRespMultiples_d import Ui_Form
from menuTipoPreguntas import menuTipoPreguntas

#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS
from PreguntasMultiplesImagen_0 import PreguntasMultiplesImagen_0
from PreguntasMultiplesImagen_50 import PreguntasMultiplesImagen50
from PreguntasMultiplesImagen_100 import PreguntasMultiplesImagen100
from PyQt5.QtWidgets import  QMessageBox


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiples(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        # creando multiples ventanas...
        self.ventanas = []

        self.ventanas.append(PreguntasMultiplesImagen_0())  # pregunta binaria
        self.ventanas.append(PreguntasMultiplesImagen50())  # preguntas multiples
        self.ventanas.append(PreguntasMultiplesImagen100())  # preguntas especificas

        # Cargando todos los disenos
        for i in range(len(self.ventanas)):
            self.listWidget_panelVersion.addWidget(self.ventanas[i])

        # VENTANA CON LA QUE SE INICIA POR DEFAULT...
        self.listWidget_panelVersion.setCurrentIndex(0)
        self.listWidget_panelVersion.showFullScreen()

        self.btn_pregImag0.clicked.connect(self.abrirPreg_normal)
        self.btn_pregImag50.clicked.connect(self.abrirPreg_imagen)
        self.btn_pregImag100.clicked.connect(self.abrirPregResp_imagen)



    def abrirPreg_normal(self):
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quiere cambiar de formato: \n"
                                         "de preguntas?\n",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.listWidget_panelVersion.setCurrentIndex(0)

    def abrirPreg_imagen(self):
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quiere cambiar de formato: \n"
                                         "de preguntas?\n",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.listWidget_panelVersion.setCurrentIndex(1)

    def abrirPregResp_imagen(self):
        resultado = QMessageBox.question(self, "DelphiPreguntas",
                                         "¿Esta seguro que quiere cambiar de formato: \n"
                                         "de preguntas?\n",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.listWidget_panelVersion.setCurrentIndex(2)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiples()
    application.show()
    app.exec()
    #sys.exit(app.exec())
