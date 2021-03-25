from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox,QHeaderView
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
from PyQt5 import QtWidgets
import os
from PyQt5.QtCore import Qt
import ast
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Ventanas_Dialogo.PanelCuestionariosMios_d import Ui_Form

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_Ejecutador.VisualizadorTodoCuestionario import VisualizadorTodoCuestionario
from CUERPO.LOGICA_creador.Creador_MisPaquetes.cuestionariosDelphi import CuestionariosDelphi


class PanelCuestionariosMios(QWidget,Ui_Form):
    senalCuestionarioElegido = pyqtSignal(dict)  # comunicacion con la aplicacionn
    def __init__(self):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        header = self.tableWidget.horizontalHeader()

        self.COLOR_TABLA = "#EEF2F3"
        self.COLOR_RESPUESTA = "#9AE5E0"
        stylesheet = "QTableView{selection-background-color: " + self.COLOR_RESPUESTA + "};"
        # stylesheet += "background-color:" + self.COLOR_TABLA + ";}"
        self.tableWidget.setStyleSheet(stylesheet)

        for columna in range(0, 3):
            header.setSectionResizeMode(columna, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.tableWidget.itemDoubleClicked.connect(self.abrirCuestionario)
        self.noCuestionarios = 0
        self.listDictDatos_CUESTIONARIOS = []

    def mostrarTablaCuestionarios(self, listDictDatos_CUESTIONARIOS):

        datosCuestionario = ("NOMBRE", "DATA_TIME", "PREGUNTAS")
        FILAS = len(listDictDatos_CUESTIONARIOS)
        COLUMNAS = len(datosCuestionario)

        self.noCuestionarios = FILAS
        self.listDictDatos_CUESTIONARIOS = listDictDatos_CUESTIONARIOS

        self.tableWidget.setRowCount(FILAS)

        for f in range(FILAS):
            for c in range(COLUMNAS):
                string = str(listDictDatos_CUESTIONARIOS[f][datosCuestionario[c]])
                a = QtWidgets.QTableWidgetItem(string)
                a.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # change the alignment
                self.tableWidget.setItem(f, c, a)
        self.tableWidget.selectRow(0)

    def abrirCuestionario(self):
        if self.noCuestionarios > 0:
            indice = self.tableWidget.currentRow()
            print(indice)
            nombreCuestionario = self.listDictDatos_CUESTIONARIOS[indice]['NOMBRE']
            resultado = QMessageBox.question(self, "Delphi",
                                             "¿Esta seguro que quieres abrir,\n"
                                             f"el cuestionario: "
                                             f"{nombreCuestionario}?",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                dictInfo = {"NOMBRE": nombreCuestionario,
                            "TIPO": "MIOS"}
                self.senalCuestionarioElegido.emit(dictInfo)

if __name__ == '__main__':
    app = QApplication([])
    application = PanelCuestionariosMios()
    application.show()
    app.exit(app.exec())

