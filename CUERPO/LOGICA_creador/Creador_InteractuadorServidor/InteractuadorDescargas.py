from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox,QHeaderView
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QCompleter
#from PyQt5.QtGui import Qt

from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana
###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_InteractuadorServidor.InteractuadorDescargas import Ui_Form

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.StorageCuestionarios import StorageCuestionarios
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
from CUERPO.LOGICA_creador.Creador_MisPaquetes.cuestionariosDelphi import CuestionariosDelphi


class InteractuadorParaDescargarCuestionarios(QWidget,Ui_Form):
    senalCuestionarioDescargado = pyqtSignal(bool)  # comunicacion con la aplicacionn

    def __init__(self):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)


#BREVES CONFIGURACIONES DE DISEÑO DE LA TABLA...

        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)
        header =self.tableWidget.horizontalHeader()

        self.COLOR_TABLA="#EEF2F3"
        self.COLOR_RESPUESTA="#9AE5E0"
        stylesheet = "QTableView{selection-background-color: " +self.COLOR_RESPUESTA+ "};"
        #stylesheet += "background-color:" + self.COLOR_TABLA + ";}"
        self.tableWidget.setStyleSheet(stylesheet)

        #la tabla tiene 3 columnas
        #("NOMBRE","DATA_TIME", "PREGUNTAS")
        header = self.tableWidget.horizontalHeader()
        for columna in range(0,3):
            header.setSectionResizeMode(columna,QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)


#DATOS QUE ESTARAN CAMBIANDO CONSTANTEMENTE EN FUNCION DE QUIEN SON LOS CUESTIONARIOS...
        self.listDictDatos_CUESTIONARIOS={} #almacenara los datos de cuestionarios
                                            #del usuario que se haya escogido...
        self.indiceCreadorElegido = -1
        self.autorCuestionariosVisualizando="" #almacenara el nombre del autor del cual
                                   #cargamos sus cuestionarios...


#DATOS QUE DEBEMOS TENER DESDE EL COMIENZO...
        fileJSON=RecursosCreadorCuestionarios.DIRE_JSON
        controlAbsoluto_storageCuestionario=StorageCuestionarios(self,fileJSON)
        # debemos inciar comunicacion,pero no queremos que nos muestre mensaje si falla
        controlAbsoluto_storageCuestionario.iniciarComunicacion(mensajeActivado=False)
        self.listaCreadores = controlAbsoluto_storageCuestionario.getNamesAllCreadores()
        self.noCreadores=len(self.listaCreadores)
        self.noCuestionarios=0

#CONFIGRUACION DEL COMBOX PARA FACILITAR LA BUSQUEDA DE AUTORES DE CUESTIONARIOS..
        acompletador=QCompleter(self.listaCreadores)
        acompletador.setCaseSensitivity(Qt.CaseInsensitive)
        self.comboBox.setEditable(True)
        self.comboBox.addItems(self.listaCreadores)
        self.comboBox.setCompleter(acompletador)


#SENALES DE LOS OBJETOS DE ESTA VENTANA...
        self.comboBox.currentIndexChanged.connect(self.eligioUnCreador)
        self.btn_verCuestionarios.clicked.connect(self.verCuestionariosCreador)
        self.tableWidget.itemDoubleClicked.connect(self.descargarCuestionario)


    def verCuestionariosCreador(self):
        if self.indiceCreadorElegido>=0:
            self.btn_verCuestionarios.setEnabled(False)
            index=self.indiceCreadorElegido
            creadorCuestionarios=self.listaCreadores[index]

            # iniciamos comunicacion con el servidor
            fileJSON = RecursosCreadorCuestionarios.DIRE_JSON
            controlAbsoluto_storageCuestionario = StorageCuestionarios(self, fileJSON)
            # debemos inciar comunicacion,pero no queremos que nos muestre mensaje si falla
            comunicacion = controlAbsoluto_storageCuestionario.iniciarComunicacion(mensajeActivado=True)
            if comunicacion:  # si la primera comunicacion fue exitosa..
                listaCuestionarios=controlAbsoluto_storageCuestionario.getDatosCuestionarios(creadorCuestionarios)
                if listaCuestionarios!=None: #si la segunda comunicion fue exitosa...
                    self.listDictDatos_CUESTIONARIOS=listaCuestionarios #ya que es el cuestionario que
                                                                        #ahora estamos viendo....
                    self.mostrarTablaCuestionarios(self.listDictDatos_CUESTIONARIOS)
                    self.noCuestionarios=len(self.listDictDatos_CUESTIONARIOS)
                    QMessageBox.critical(self, "Felicidades n.n",
                                         "Los cuestionarios mas recientes \n"
                                         f"compartidos de... '{creadorCuestionarios}'\n"
                                         "han sido cargados exitosamente\n"
                                         f"y son un total de {self.noCuestionarios}.\n",
                                         QMessageBox.Ok)
                    self.bel_autorCuestionarios.setText(creadorCuestionarios)
                    self.autorCuestionariosVisualizando=creadorCuestionarios

            self.btn_verCuestionarios.setEnabled(True)


    def descargarCuestionario(self,index):
        print("***************",index.text())
        print("***************",index.row())
        index=index.row()
        if index<self.noCuestionarios:
            nombreCuestionario=self.listDictDatos_CUESTIONARIOS[index]["NOMBRE"]
            nombreCuestionario_storage=self.listDictDatos_CUESTIONARIOS[index]["NOMBRE_FIREBASE"]


            autorCuestionario=self.autorCuestionariosVisualizando
            # VALUES==>{'COMPARTIDOS''ORDEN': '22817912834', 'DATA_TIME': '09/08/2020,21:18:32', 'PREGUNTAS': 2}
            tuplaCuestionariosCompartidos = CuestionariosDelphi.getNombresCuestionarios(descargados=True)
            cuestionarioYaDescargado = False
            # {'ORDEN': '22817912834', 'DATA_TIME': '09/08/2020,21:18:32', 'PREGUNTAS': 2}
            for datosCuestionario in tuplaCuestionariosCompartidos:
                if datosCuestionario["NOMBRE"] == nombreCuestionario:
                    cuestionarioYaDescargado = True
                    break

            if cuestionarioYaDescargado:
                QMessageBox.critical(self, "Atencion",
                                     "El cuestionario que quieres\n"
                                     "descargar, ya ha sido descargado\n"
                                     "anteriormente...",
                                     QMessageBox.Ok)
                self.senalCuestionarioDescargado.emit(True)
            else:
                # iniciamos comunicacion con el servidor
                fileJSON = RecursosCreadorCuestionarios.DIRE_JSON
                controlAbsoluto_storageCuestionario = StorageCuestionarios(self, fileJSON)
                comunicacion = controlAbsoluto_storageCuestionario.iniciarComunicacion(mensajeActivado=True)
                if comunicacion:  # si la primera comunicacion fue exitosa..
                    #destinoCuestinario = nombreCuestionario#SERA AHI MISMO...
                    print("DIOS....",nombreCuestionario)
                    existeAun=controlAbsoluto_storageCuestionario.existeCuestionario(autorCuestionario=autorCuestionario,
                                                                           nombreCuestionario=nombreCuestionario,
                                                                           mensajeActivado=True
                                                                           )
                    if existeAun!=None: #No ocurrio ningun eeror
                        if existeAun: #Si existe aun el cuestionario...
                            # La clave almacena lo que responde el usuario...
                            # resultado responde si si respondio algo o no!!!!!1
                            clave=self.listDictDatos_CUESTIONARIOS[index]["CLAVE"]
                            claveIngresada, escribioAlgo = QInputDialog.getText(self, "Clave cuestionario", "Ingresa su clave de descarga:")
                            if escribioAlgo:
                                if claveIngresada!=clave:
                                    QMessageBox.critical(self, "Atencion",
                                                         "Clave de cuestionario\n"
                                                         "incorrecta.",
                                                         QMessageBox.Ok)
                                else:
                                    estado=controlAbsoluto_storageCuestionario.descargarCuestionario(
                                                                                                     autor=autorCuestionario,
                                                                                                     nombreCuestionarioLocal=nombreCuestionario,
                                                                                                     nombreCuestionarioStorage=nombreCuestionario_storage,
                                                                                                     mensajeActivado=True
                                                                                                     )
                                    if estado != None:  # si la segunda comunicion fue exitosa...
                                        #self.listDictDatos_CUESTIONARIOS = listaCuestionarios  # ya que es el cuestionario que
                                        # ahora estamos viendo....
                                        self.mostrarTablaCuestionarios(self.listDictDatos_CUESTIONARIOS)
                                        self.noCuestionarios = len(self.listDictDatos_CUESTIONARIOS)
                                        self.senalCuestionarioDescargado.emit(True)
                        else: #Ya no existe el cuestionario...
                            QMessageBox.critical(self, "Atencion",
                                                 "El cuestionario que quieres\n"
                                                 "descargar, ya NO esta en el \n"
                                                 "servidor debido a que el usuario\n"
                                                 "que lo compartio ya lo elimino,\n"
                                                 "te recomendamos actualizar los\n"
                                                 "cuestionarios de este usuario\n"
                                                 "para que puedas ver realmente \n"
                                                 "cuales cuestionarios son los \n"
                                                 "sus cuestionarios compartidos\n",
                                                 QMessageBox.Ok)

    def mostrarTablaCuestionarios(self, listDictDatos_CUESTIONARIOS):
        #datos de los cuestionarios compartidos...
        #datosCuestionario = ("NOMBRE", "ORDEN", "DATA_TIME", "PREGUNTAS", "CLAVE")
        #datos que unicamente visualizaremos...
        datosCuestionario = ("NOMBRE","DATA_TIME", "PREGUNTAS")
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



    def eligioUnCreador(self,index):
        if index>=self.noCreadores:
            QMessageBox.critical(self, "Atencion",
                                 "No existe usuario cuyo \n"
                                 f"nombre sea:{self.comboBox.currentText()}",
                                 QMessageBox.Ok)
            self.comboBox.removeItem(index)
        elif self.indiceCreadorElegido!=index:
            self.indiceCreadorElegido=index
            print("Creador elegido: ",self.listaCreadores[index])
















if __name__ == '__main__':
    app = QApplication([])
    application = InteractuadorParaDescargarCuestionarios()
    application.show()
    app.exit(app.exec())