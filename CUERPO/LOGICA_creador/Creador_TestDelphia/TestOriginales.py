from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox,QHeaderView
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
from PyQt5 import QtWidgets
import os
from PyQt5.QtCore import Qt
import ast
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana
from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
import random
from PyQt5 import QtCore, QtGui, QtWidgets
###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_TestDelphia.TestOriginales_d import Ui_Form

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.cuestionariosDelphi import CuestionariosDelphi
from CUERPO.LOGICA_creador.Creador_Ejecutador.CreadorCuestionarios import EjecutadorCuestionario
from CUERPO.LOGICA_creador.Creador_MisPaquetes.StorageCuestionarios import StorageCuestionarios
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
from CUERPO.LOGICA_creador.Creador_Main.main import CreadorPreguntas
from CUERPO.LOGICA_creador.Creador_MisPaquetes.FirebaseCuestionarios import FirebaseCuestionarios

class TestOriginales(QWidget,Ui_Form):
    senalActualizacionTest = pyqtSignal(bool)  # comunicacion con la aplicacionn
    def __init__(self,nombreUsuario=""):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        self.nombreUsuario=nombreUsuario

        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        header = self.tableWidget.horizontalHeader()

        self.COLOR_TABLA = "#EEF2F3"
        self.COLOR_RESPUESTA = "#9AE5E0"
        self.COLOR_MALO="#E22E1C"
        self.COLOR_REGULAR="#DCE21C"
        self.COLOR_BUENO="#1CE285"
        self.COLOR_EXCELENTE="#0DDEFF"

        stylesheet = "QTableView{selection-background-color: " + self.COLOR_RESPUESTA + "};"
        # stylesheet += "background-color:" + self.COLOR_TABLA + ";}"
        self.tableWidget.setStyleSheet(stylesheet)

        self.noColumnasTabla=4
        for columna in range(0, 4):
            header.setSectionResizeMode(columna, QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.tableWidget.itemDoubleClicked.connect(self.abrirCuestionario)
        self.noCuestionarios = 0
        self.listDatos_tests=[]
        self.mostrarTablaCuestionarios()

        self.btn_verCuestionarios.clicked.connect(self.actualizarTest)
        self.btn_campachenoTest.clicked.connect(self.jugarCampacheano)



    def clasificarCuestionario(self,noRenglon,califPorcentaje):
        if califPorcentaje<60:
            self.colorearRenglon(noRenglon,self.COLOR_MALO)
        elif 60<=califPorcentaje<80:
            self.colorearRenglon(noRenglon, self.COLOR_REGULAR)
        elif 80<=califPorcentaje<95:
            self.colorearRenglon(noRenglon, self.COLOR_BUENO)
        else:
            self.colorearRenglon(noRenglon,self.COLOR_EXCELENTE)


    def colorearRenglon(self,noRenglon,color):
        for c in range(self.noColumnasTabla):
            self.tableWidget.item(noRenglon,c).setBackground(QtGui.QColor(color))

    def jugarCampacheano(self):
        resultado = QMessageBox.question(self, "Delphi",
                                         "¿Estas SEGURO de jugar un\n"
                                         f"CAMPECHANO?",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            self.nonerias() #a ver que pasa...



    def mostrarTablaCuestionarios(self):
        self.listDatos_tests = CuestionariosDelphi.getNombresCuestionarios(oficiales=True)

        listDictDatos_CUESTIONARIOS=self.listDatos_tests
        self.senalActualizacionTest.emit(True)

        datosCuestionario = ("PREGUNTAS","NOMBRE","DATA_TIME")
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
                self.tableWidget.setItem(f,c+1, a)

        controlFirebaseCuestionarios = FirebaseCuestionarios(self)
        exito = controlFirebaseCuestionarios.iniciarComunicacion(mensajeActivado=True)
        if exito:
            calif=controlFirebaseCuestionarios.getAllCalifTest(nombreUsuario=self.nombreUsuario,
                                                        mensajeActivado=True)
            if calif!=None:
                for f in range(FILAS):
                    califTest=calif[f]
                    a = QtWidgets.QTableWidgetItem(str(califTest))
                    a.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # change the alignment
                    self.tableWidget.setItem(f,0, a)
                    #Coloreando el renglon en funcion de la calif...
                    self.clasificarCuestionario(f,califTest)
        self.tableWidget.selectRow(0)



    def subirCalifTestOriginal(self,context,nombreTest,calif,renglonTabla):
        calif_prev=float(self.tableWidget.item(renglonTabla,0).text())
        if calif_prev<calif:
            # actualizando calif en la tabla...
            a = QtWidgets.QTableWidgetItem(str(calif))
            a.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)  # change the alignment
            self.tableWidget.setItem(renglonTabla, 0, a)
            #coloremamos el cuestionario en funcion de la calificacion obtenida...
            self.clasificarCuestionario(renglonTabla,calif)
            controlFirebaseCuestionarios = FirebaseCuestionarios(context)
            exito = controlFirebaseCuestionarios.iniciarComunicacion(mensajeActivado=True)
            if exito:
                print("INTENTANDO SUBIENDO RESPUESTA....")
                controlFirebaseCuestionarios.subirCalifTest(nombreUsuario=self.nombreUsuario,
                                                            nombreTest=nombreTest,
                                                            calif=calif,
                                                            mensajeActivado=True)
        else:#si no sacas una calificacion mayor no se actualiza...
            pass



    def abrirCuestionario(self):
        if self.noCuestionarios > 0:
            indice = self.tableWidget.currentRow()
            print(indice)
            nombreCuestionario = self.listDatos_tests[indice]['NOMBRE']
            resultado = QMessageBox.question(self, "Delphi",
                                             "¿Esta SEGURO de realizar\n"
                                             f"el test: {nombreCuestionario}?",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                self.cuestionarioTest = EjecutadorCuestionario(nombreCuestionario=nombreCuestionario,
                                                                     ordenAleatorio=True,
                                                                     oficiales=True)
                self.cuestionarioTest.senalCalificacionObtenida.connect(lambda calif: self.subirCalifTestOriginal(context=self.cuestionarioTest,
                                                                                                              nombreTest=nombreCuestionario,
                                                                                                              calif=calif,
                                                                                                              renglonTabla=indice))
                self.cuestionarioTest.show()


    def actualizarTest(self):
        controlABSOLUTO_storageCuestionarios = StorageCuestionarios(self,
                                                                    RecursosCreadorCuestionarios.DIRE_JSON)
        # iniciamos comunicacion con el servidor
        comunicacion = controlABSOLUTO_storageCuestionarios.iniciarComunicacion(mensajeActivado=True)
        if comunicacion:  # si la primera comunicacion fue exitosa..
            exitoOperacion = controlABSOLUTO_storageCuestionarios.ponerteAlCorriente_test(True)
            if exitoOperacion != None:  # el prefijo del cuestionario se obtuvo con exito...
                QMessageBox.critical(self, "Felicidades n.n",
                                     "Los TEST_DELPHIA\n"
                                     "estan actualizados.",
                                     QMessageBox.Ok)
            self.mostrarTablaCuestionarios() #que se actualice...


    def nonerias(self):
        #("NOMBRE", "DATA_TIME", "PREGUNTAS")... llaves de los datos de cada test...
        listNombresTest=[x["NOMBRE"] for x in self.listDatos_tests]
        noTest=len(listNombresTest)

        if noTest>1:
            if noTest>=3: #si hay mas de 3 cuestionarios...
                listNombresTest=random.sample(listNombresTest,3)
            print("CUESTIONARIOS ELEGIDOS...", listNombresTest)
            for nombreTest in listNombresTest:
                self.cuestionarioCampechano = CreadorPreguntas(nombreCreador="noImporta",
                                                               listNombresExistentes=[],
                                                               nombreCuestionario="CAMPECHANO_123")
                #jalaremos 5 preguntas de cada cuestionario...
                self.cuestionarioCampechano.importarCuestionario({"NOMBRE":nombreTest,
                                                                  "TIPO":"OFICIALES"},
                                                                  numberQuestionRandom=5
                                                                 )

            #ya que creamos el cuestionario campechao ahora hay que ejecutarlo...
            self.cuestionarioTestHibrido = EjecutadorCuestionario(nombreCuestionario='CAMPECHANO_123',
                                                                     mios=True,
                                                                     ordenAleatorio=True)

            self.cuestionarioTestHibrido.senalCalificacionObtenida.connect(lambda calif: self.subirCalifTestCampechano(self.cuestionarioTestHibrido,calif) )
            #Eliminamos el cuestionario campechano que hicimos...
            self.cuestionarioTestHibrido.senalEjecutadorCerrado.connect(lambda x: self.cuestionarioCampechano.eliminarTodoCuestionario())

            self.cuestionarioTestHibrido.show()

    def subirCalifTestCampechano(self,context,calif):
        controlFirebaseCuestionarios = FirebaseCuestionarios(context)
        exito = controlFirebaseCuestionarios.iniciarComunicacion(mensajeActivado=True)
        if exito:
            print("INTENTANDO SUBIENDO RESPUESTA....")
            controlFirebaseCuestionarios.subirCalifCampechano(nombreUsuario=self.nombreUsuario,
                                                              calif=calif)

if __name__ == '__main__':
    app = QApplication([])
    application = TestOriginales(nombreUsuario="Roni")
    application.show()
    app.exit(app.exec())