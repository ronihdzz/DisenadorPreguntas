from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
from PyQt5 import QtWidgets
import os
from PyQt5.QtCore import Qt
import ast
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana
import shutil


###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_TestDelphia.TestDescargar_d import Ui_Form

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.cuestionariosDelphi import CuestionariosDelphi
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
from CUERPO.LOGICA_creador.Creador_Ejecutador.VisualizadorTodoCuestionario import VisualizadorTodoCuestionario

class TestDescargar(QWidget,Ui_Form):
    senalTestDescargado = pyqtSignal(bool)  # comunicacion con la aplicacionn
    def __init__(self,nombreUsuario=""):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        self.nombreUsuario=nombreUsuario

        self.nombreUsuario = nombreUsuario

        # Configuraciones a la tabla...
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.COLOR_TABLA = "#EEF2F3"
        self.COLOR_RESPUESTA = "#9AE5E0"
        stylesheet = "QTableView{selection-background-color: " + self.COLOR_RESPUESTA + "};"
        # stylesheet += "background-color:" + self.COLOR_TABLA + ";}"
        self.tableWidget.setStyleSheet(stylesheet)

        # la tabla tiene 4 columnas
        # ("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE")
        header = self.tableWidget.horizontalHeader()
        for columna in range(0, 3):
            header.setSectionResizeMode(columna, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.itemDoubleClicked.connect(self.abrirCuestionario)
        self.noCuestionarios = 0
        self.listDatos_tests=[]
        self.mostrarTablaCuestionarios()



    def mostrarTablaCuestionarios(self):
        self.listDatos_tests = CuestionariosDelphi.getNombresCuestionarios(oficiales=True)
        listDictDatos_CUESTIONARIOS=self.listDatos_tests

        datosCuestionario = ("NOMBRE", "DATA_TIME", "PREGUNTAS")
        FILAS = len(listDictDatos_CUESTIONARIOS)
        COLUMNAS = len(datosCuestionario)
        print("holiwi",listDictDatos_CUESTIONARIOS)

        self.noCuestionarios = FILAS

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
            nombreCuestionario = self.listDatos_tests[indice]['NOMBRE']
            resultado = QMessageBox.question(self, "Delphi",
                                             "¿Esta seguro que quieres abrir,\n"
                                             f"el Test: "
                                             f"{nombreCuestionario}?",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                    # self.dictDatos = dictDatos  # "ConfirmacionMensaje","ConfirmacionClave","Accion","Explicacion"
                    indicaciones = " La descarga de TEST_DELPHI es muy rara sin embargo posible, pero solo la recomendamos "
                    indicaciones += "cuando necesitas trabajar con el contenido de un cuestionario...\n"
                    indicaciones += "Para poder descargar el TEST_DELPHIA debes repetir la siguiente frase:"

                    claveConfirmacion = "Descargar Test Delphia"
                    accion = "DESCARGAR TEST DELPHIA"
                    explicacion = "Te sugerimos que explores el contenido de este TEST_DELPHIA,para que estes mas  "
                    explicacion += "segur@ acerca de si es el que deseas DESCARGAR realmente.  "
                    dicDatos = {
                        "ConfirmacionMensaje": indicaciones,
                        "ConfirmacionClave": claveConfirmacion,
                        "Accion": accion,
                        "Explicacion": explicacion
                    }

                    self.cuestionarioCompartido = VisualizadorTodoCuestionario(nombreCuestionario=nombreCuestionario,
                                                                               dictDatos=dicDatos,
                                                                               oficiales=True)
                    self.setEnabled(False)
                    self.cuestionarioCompartido.senalTermino.connect(lambda x: self.setEnabled(True))
                    self.cuestionarioCompartido.senalCuestionarioConfirmado.connect(lambda x: self.descargarCuestionario(self.cuestionarioCompartido,
                                                                                                                                   nombreCuestionario))
                    self.cuestionarioCompartido.show()

    def descargarCuestionario(self,context,nombreCuestinoario):
        #VALUES==>{'COMPARTIDOS''ORDEN': '22817912834', 'DATA_TIME': '09/08/2020,21:18:32', 'PREGUNTAS': 2}
        tuplaCuestionariosCompartidos=CuestionariosDelphi.getNombresCuestionarios(descargados=True)
        cuestionarioYaDescargado=False
        #{'ORDEN': '22817912834', 'DATA_TIME': '09/08/2020,21:18:32', 'PREGUNTAS': 2}
        for datosCuestionario in tuplaCuestionariosCompartidos:
            if datosCuestionario["NOMBRE"]==nombreCuestinoario:
                cuestionarioYaDescargado=True
                break

        if cuestionarioYaDescargado:
            QMessageBox.critical(context, "Atencion",
                                 "El cuestionario que quieres\n"
                                 "descargar, ya ha sido descargado\n"
                                 "anteriormente...",
                                 QMessageBox.Ok)
        else:
            nombreCuestinoarioCompleto=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DELPHI_OFICIALES
            nombreCuestinoarioCompleto+=nombreCuestinoario
            destinoCuestinario=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS
            destinoCuestinario+=nombreCuestinoario
            # Copiando la carpeta del cuestionarios compartidos...
            shutil.copytree(nombreCuestinoarioCompleto,destinoCuestinario)
            QMessageBox.critical(context, "Felicidades n.n",
                                 "Cuestionario  DESCARGADO\n"
                                 "exitosamente\n",
                                 QMessageBox.Ok)
        self.senalTestDescargado.emit(True)

if __name__ == '__main__':
    app = QApplication([])
    application = TestDescargar(nombreUsuario="Roni")
    application.show()
    app.exit(app.exec())