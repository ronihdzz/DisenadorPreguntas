from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox,QHeaderView
from PyQt5.QtGui import QStandardItemModel,QStandardItem
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
from CUERPO.DISENO_creador.Creador_InteractuadorServidor.InteractuadorCompartidos_d import Ui_Form

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.StorageCuestionarios import StorageCuestionarios
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
from CUERPO.LOGICA_creador.Creador_Ejecutador.VisualizadorTodoCuestionario import VisualizadorTodoCuestionario
from CUERPO.LOGICA_creador.Creador_MisPaquetes.cuestionariosDelphi import CuestionariosDelphi

class InteractuadorCuestionariosCompartidos(QWidget,Ui_Form):
    senalCuestionarioDescargado = pyqtSignal(bool)  # comunicacion con la aplicacionn
    def __init__(self,nombreUsuario):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)

        self.nombreUsuario=nombreUsuario

        #Configuraciones a la tabla...
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        self.COLOR_TABLA="#EEF2F3"
        self.COLOR_DESCARGAR= "#9AE5E0"
        self.COLOR_BORRAR="#F42303"


        #la tabla tiene 4 columnas
        #("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE")
        header = self.tableWidget.horizontalHeader()
        for columna in range(0,4):
            header.setSectionResizeMode(columna,QtWidgets.QHeaderView.ResizeToContents)
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)


        #Radio button...
        self.rdBtn_descargar.toggled.connect(lambda :self.estadoCuestionariosCompartidosCambiado(descargar=True))
        self.rdBtn_borrar.toggled.connect(lambda : self.estadoCuestionariosCompartidosCambiado(descargar=False))

        self.alAbrirCuestionarioQuiereDescargarlo=True

        self.rdBtn_descargar.setChecked(True)

        self.tableWidget.itemDoubleClicked.connect(self.abrirCuestionario)
        self.noCuestionarios=1

        self.refrescarCompartidos()


    def refrescarCompartidos(self):
        # llaves de datos que contiene cada cuestionario:
        # ("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE")

        controlABSOLUTO_storageCuestionarios = StorageCuestionarios(self,
                                                                    RecursosCreadorCuestionarios.DIRE_JSON)
        # iniciamos comunicacion con el servidor
        comunicacion = controlABSOLUTO_storageCuestionarios.iniciarComunicacion(mensajeActivado=True)
        if comunicacion:  # si la primera comunicacion fue exitosa..
            datosCuestionariosCompartidos= controlABSOLUTO_storageCuestionarios.getDatosCuestionarios(autor=self.nombreUsuario,
                                                                                                      mensajeActivado=True)
            if datosCuestionariosCompartidos!=None:
                self.datosCuestionariosCompartidos=datosCuestionariosCompartidos
                self.mostrarTablaCuestionarios(self.datosCuestionariosCompartidos)


    def estadoCuestionariosCompartidosCambiado(self,descargar):
        if descargar:
            stylesheet = "QTableView{selection-background-color: " + self.COLOR_DESCARGAR + "};"
            # stylesheet += "background-color:" + self.COLOR_TABLA + ";}"
            self.tableWidget.setStyleSheet(stylesheet)
            self.alAbrirCuestionarioQuiereDescargarlo = True
        else:
            stylesheet = "QTableView{selection-background-color: " + self.COLOR_BORRAR + "};"
            # stylesheet += "background-color:" + self.COLOR_TABLA + ";}"
            self.tableWidget.setStyleSheet(stylesheet)
            self.alAbrirCuestionarioQuiereDescargarlo = False

    def mostrarTablaCuestionarios(self, listDictDatos_CUESTIONARIOS):
        #datos de los cuestionarios compartidos...
        #datosCuestionario = ("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE")
        #datos que unicamente visualizaremos
        datosCuestionario = ("NOMBRE","DATA_TIME", "PREGUNTAS", "CLAVE")
        FILAS = len(listDictDatos_CUESTIONARIOS)
        COLUMNAS = len(datosCuestionario)

        self.noCuestionarios=FILAS
        self.listDictDatos_CUESTIONARIOS=listDictDatos_CUESTIONARIOS

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
                if self.alAbrirCuestionarioQuiereDescargarlo:
                    # self.dictDatos = dictDatos  # "ConfirmacionMensaje","ConfirmacionClave","Accion","Explicacion"
                    indicaciones = " La descarga de cuestionarios compartidos solo la recomendamos "
                    indicaciones += "cuando haz eliminado  de TUS CUESTIONARIOS LOCALES este cuestionario "
                    indicaciones += "que compartiste en el servidor de Delphia.Si este cuestionario que compartiste "
                    indicaciones += "ya no lo tienes en TUS CUESTIONARIOS LOCALES, y necesitas trabajar con su contenido "
                    indicaciones += "te recomendamos descargarlo.\n"
                    indicaciones += "Para poder descargar el cuestionario debes repetir la siguiente frase:"

                    claveConfirmacion = "Descargar cuestionario"
                    accion = "DESCARGAR CUESTIONARIO COMPARTIDO"
                    explicacion = "Te sugerimos que explores el contenido de este cuestionario que has compartido  "
                    explicacion += "con el servidor de Delphia, para que estes mas segur@ acerca de si es el que "
                    explicacion += "deseas DESCARGAR realmente. "

                    dicDatos = {
                        "ConfirmacionMensaje": indicaciones,
                        "ConfirmacionClave": claveConfirmacion,
                        "Accion": accion,
                        "Explicacion": explicacion
                    }

                    self.cuestionarioCompartido = VisualizadorTodoCuestionario(nombreCuestionario=nombreCuestionario,
                                                                               dictDatos=dicDatos,
                                                                               compartidos=True)
                    self.setEnabled(False)
                    self.cuestionarioCompartido.senalTermino.connect(lambda x: self.setEnabled(True))
                    self.cuestionarioCompartido.senalCuestionarioConfirmado.connect(lambda x: self.descargarCuestionarioCompartido(self.cuestionarioCompartido,
                                                                                                                                   nombreCuestionario))
                    self.cuestionarioCompartido.show()
                else:#al abrir el cuestionario quiere eliminarlo...
                    # self.dictDatos = dictDatos  # "ConfirmacionMensaje","ConfirmacionClave","Accion","Explicacion"
                    indicaciones = "Debes estar consciente que al eliminar este cuestionario  que "
                    indicaciones += "compartiste  con el servidor de Delphia, ocacionara que  ya nadie lo pueda ver y descargar, solo si lo vuelves "
                    indicaciones += "a compartir, pero de igual forma lo recomendamos hacer si ya no es necesario que este en el servidor,ya  que "
                    indicaciones += "al eliminarlo del servidor, liberaras mas recursos de este.\n"
                    indicaciones += "Para eliminar el cuestionario de la seccion de 'MIS CUESTIONARIOS COMPARTIDOS CON EL SERVIDOR', repite "
                    indicaciones += "la siguiente frase:"

                    claveConfirmacion = "Eliminar cuestionario"
                    accion = "ELIMINAR ESTE CUESTIONARIO QUE COMPARTI "
                    explicacion = "Te sugerimos que explores el contenido de este cuestionario que has compartido "
                    explicacion += "con el servidor de Delphia, para que estes mas segur@ acerca de si es el que "
                    explicacion += "deseas ELIMINAR realmente."

                    dicDatos = {
                        "ConfirmacionMensaje": indicaciones,
                        "ConfirmacionClave": claveConfirmacion,
                        "Accion": accion,
                        "Explicacion": explicacion
                    }

                    self.cuestionarioCompartido = VisualizadorTodoCuestionario(nombreCuestionario=nombreCuestionario,
                                                                               dictDatos=dicDatos,
                                                                               compartidos=True)
                    self.setEnabled(False)
                    self.cuestionarioCompartido.senalTermino.connect(lambda x: self.setEnabled(True))
                    self.cuestionarioCompartido.senalCuestionarioConfirmado.connect(lambda x: self.eliminarCuestionarioCompartido(self.cuestionarioCompartido,
                                                                                                                                  nombreCuestionario))
                    self.cuestionarioCompartido.show()

    def descargarCuestionarioCompartido(self,context,nombreCuestinoario):
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
            nombreCuestinoarioCompleto=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_COMPARTIDOS
            nombreCuestinoarioCompleto+=nombreCuestinoario
            destinoCuestinario=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS
            destinoCuestinario+=nombreCuestinoario
            # Copiando la carpeta del cuestionarios compartidos...
            shutil.copytree(nombreCuestinoarioCompleto,destinoCuestinario)
            QMessageBox.critical(context, "Felicidades n.n",
                                 "Cuestionario  DESCARGADO\n"
                                 "exitosamente\n",
                                 QMessageBox.Ok)

        self.senalCuestionarioDescargado.emit(True)

    def eliminarCuestionarioCompartido(self,context,nombreCuestionario):

        controlABSOLUTO_storageCuestionarios = StorageCuestionarios(context,
                                                                    RecursosCreadorCuestionarios.DIRE_JSON)
        # iniciamos comunicacion con el servidor
        comunicacion = controlABSOLUTO_storageCuestionarios.iniciarComunicacion(mensajeActivado=True)
        if comunicacion:  # si la primera comunicacion fue exitosa..
            exitoAlEliminar = controlABSOLUTO_storageCuestionarios.eliminarCuestionario(autor=self.nombreUsuario,
                                                                 nombreCuestionarioEliminar=nombreCuestionario,
                                                                 mensajeActivado=True)

            if exitoAlEliminar != None:  # sin errores al eliminar cuestionario...
                nombreCuestionarioCompleto=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_COMPARTIDOS
                nombreCuestionarioCompleto+=nombreCuestionario
                shutil.rmtree(nombreCuestionarioCompleto)  # borramos la carpeta que se paso en donde estamos...
                self.refrescarCompartidos() #refrescamos los cuestionarios compartidos....



if __name__ == '__main__':
    app = QApplication([])
    application = InteractuadorCuestionariosCompartidos(nombreUsuario="Roni")
    application.show()
    app.exit(app.exec())