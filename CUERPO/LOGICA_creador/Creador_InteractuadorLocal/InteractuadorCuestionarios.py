from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox,QHeaderView
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal,QObject
import shutil, os


###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_InteractuardorLocal.InteractuadorCuestionarios_d import Ui_Form

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################

from CUERPO.LOGICA_creador.Creador_InteractuadorLocal.InteractuadorMisCuestionarios import InteractuadorMisCuestionarios
from CUERPO.LOGICA_creador.Creador_InteractuadorLocal.InteractuadorMisDescargas import InteractuadorMisDescargas
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
from CUERPO.LOGICA_creador.Creador_MisPaquetes.comportSelect_btnsImagen import comporSelec_btnsImagen
from CUERPO.LOGICA_creador.Creador_Main.main import CreadorPreguntas
from CUERPO.LOGICA_creador.Creador_Ventanas_Dialogo.EditorNombreArchivo import EditarNombre
from CUERPO.LOGICA_creador.Creador_Ejecutador.VisualizadorTodoCuestionario import VisualizadorTodoCuestionario

from CUERPO.LOGICA_creador.Creador_MisPaquetes.cuestionariosDelphi import CuestionariosDelphi

class InteractuadorCuestionarios(QWidget,Ui_Form):
    senalCuestionarioCompartido = pyqtSignal(bool)
    senalUsuarioCerro=pyqtSignal(bool)
    senalTestCompartido=pyqtSignal(bool)
    def __init__(self,nombreUsuario):
        Ui_Form.__init__(self)
        QWidget.__init__(self)
        self.setupUi(self)
        self.nombreUsuario=nombreUsuario
        self.ventana_misCuestionarios=InteractuadorMisCuestionarios()
        self.ventana_descargadosCuestionarios=InteractuadorMisDescargas()

        #SENALES...
        self.ventana_misCuestionarios.senalCuestionarioElegido.connect(self.abrirCuestionario)
        self.ventana_descargadosCuestionarios.senalCuestionarioElegido.connect(self.abrirCuestionario)

        #VAMO A COLOCAR NOMBRES DE CUESTIONARIOS...
        self.refrescarDatosCuestionarios(descargas=True,mios=True)



        self.listWidget.addWidget(self.ventana_misCuestionarios)
        self.listWidget.addWidget(self.ventana_descargadosCuestionarios)

        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPunteros_yoDijeElDijo = (self.btn_proceso, self.btn_descargados)
        self.listImagen_yoDijeElDijo = (RecursosCreadorCuestionarios.ICON_CUESTIONARIOS_PROCESO,
                                        RecursosCreadorCuestionarios.ICON_CUESTIONARIOS_DESCARGADOS,)

        self.controlABSLUTO_tipoCuestionarios = comporSelec_btnsImagen(self.listBtnPunteros_yoDijeElDijo,
                                                                       self.listImagen_yoDijeElDijo)
        self.controlABSLUTO_tipoCuestionarios.COLOR_SELECCION = "#FF69B4"
        self.controlABSLUTO_tipoCuestionarios.BORDER_RADIUS = "4"

        self.controlABSLUTO_tipoCuestionarios.botonFuePresionado.connect(self.verOtrosCuestionarios)
        self.controlABSLUTO_tipoCuestionarios.botonPresionado(0)

        self.btn_nuevo.clicked.connect(self.nuevoCuestionario)
        self.btn_nuevo.clicked.connect(lambda: self.controlABSLUTO_tipoCuestionarios.botonPresionado(0))

        self.setWindowTitle(f"USUARI(@): {nombreUsuario}")


    def verOtrosCuestionarios(self, idBtnFuePresionado):
            self.controlABSLUTO_tipoCuestionarios.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado, False)
            if idBtnFuePresionado==1: #quiere ver los cuestionarios descargados...
                self.listWidget.setCurrentIndex(1)
            else: #quiere ver su respuesta...
                self.listWidget.setCurrentIndex(0)



    def refrescarDatosCuestionarios(self,descargas=False,mios=False):
        if mios:
            self.listCuestionariosMios=CuestionariosDelphi.getNombresCuestionarios(mios=True)
            self.ventana_misCuestionarios.mostrarTablaCuestionarios(self.listCuestionariosMios)
            self.listNombresCuestionariosMios = [x["NOMBRE"] for x in self.listCuestionariosMios]
        if descargas:
            self.listCuestionariosDescargados=CuestionariosDelphi.getNombresCuestionarios(descargados=True)
            self.ventana_descargadosCuestionarios.mostrarTablaCuestionarios(self.listCuestionariosDescargados)
            self.listNombresCuestionariosDescargados = [x["NOMBRE"] for x in self.listCuestionariosDescargados]


    def abrirCuestionario(self,dicInfo):
        #dictInfo==> llaves:NOMBRE y TIPO==>DESCARGADOS OR MIOS

        nombreCuestionario=dicInfo["NOMBRE"]

        if dicInfo["TIPO"]=="MIOS":

            self.cuestionario = CreadorPreguntas(nombreCreador=self.nombreUsuario,
                                                 nombreCuestionario=nombreCuestionario,
                                                 listNombresExistentes=self.listNombresCuestionariosMios)
            self.setEnabled(False)
            #mandaremos la senal con los otros para decir que el cuestionario ha sido compartido....
            self.cuestionario.senalCuestionarioCompartido.connect(lambda x: self.senalCuestionarioCompartido.emit(True) )
            self.cuestionario.senalTestCompartido.connect(lambda x: self.senalTestCompartido.emit(True) )

            self.cuestionario.senalTermino.connect(lambda x: self.setEnabled(True))
            self.cuestionario.senalTermino.connect(lambda x: self.refrescarDatosCuestionarios(mios=True))
            self.cuestionario.show()
        else:
            # self.dictDatos = dictDatos  # "ConfirmacionMensaje","ConfirmacionClave","Accion","Explicacion"
            indicaciones = "Debes estar consciente que al eliminar este cuestionario de tu "
            indicaciones += "carpeta de descargas ya no lo podra abrir, solo si lo vuelves "
            indicaciones += "a descargar, aunque corres el riesgo de que ya no este en la base "
            indicaciones += "de datos para volverlo a descargar ¿en realidad estas seguro de querer eliminarlo?"

            claveConfirmacion = "lo quiero eliminar"
            accion = "ELIMINAR CUESTIONARIO DE MI CARPETA DE DESCARGAS"
            explicacion = "Los cuestionarios descargados no se pueden editar, solo sirven para ser importados, "
            explicacion += "de cualquier forma puedes explorar su contenido"

            dicDatos = {
                "ConfirmacionMensaje": indicaciones,
                "ConfirmacionClave": claveConfirmacion,
                "Accion": accion,
                "Explicacion": explicacion
            }

            self.cuestionarioDescargado=VisualizadorTodoCuestionario(nombreCuestionario=nombreCuestionario, dictDatos=dicDatos,
                                                       descargados=True)
            self.setEnabled(False)
            self.cuestionarioDescargado.senalTermino.connect(lambda x: self.setEnabled(True))
            #si se confirma la accion significa que desea eliminarlo de la carpeta de descargas...
            self.cuestionarioDescargado.senalCuestionarioConfirmado.connect(lambda x: self.eliminarCuestionarioDescargado(nombreCuestionario))

            self.cuestionarioDescargado.show()

    def eliminarCuestionarioDescargado(self,nombreCuestionario):
        nombreCompleto=RecursosCreadorCuestionarios.DIREC_CUESTIONARIOS_DESCARGADOS
        nombreCompleto+=nombreCuestionario
        shutil.rmtree(nombreCompleto)  # borramos la carpeta que se paso en donde estamos...
        self.refrescarDatosCuestionarios(descargas=True)


    def nuevoCuestionario(self):
        self.elegidorNombre = EditarNombre(self.listNombresCuestionariosMios)
        self.elegidorNombre.senalNombreElegido.connect(self.crearNuevoCuestionario)
        self.elegidorNombre.show()

    def crearNuevoCuestionario(self, nombreCuestionario):
        self.cuestionario = CreadorPreguntas(nombreCreador=self.nombreUsuario,
                                             nombreCuestionario=nombreCuestionario,
                                             listNombresExistentes=self.listNombresCuestionariosMios)
        self.setEnabled(False)
        self.cuestionario.senalTermino.connect(lambda x: self.setEnabled(True))
        self.cuestionario.senalTermino.connect(lambda x: self.refrescarDatosCuestionarios(mios=True))
        self.cuestionario.show()

    def closeEvent(self, event):
            resultado = QMessageBox.question(self, "RonTest",
                                             "¿Seguro que quieres salir?\n",
                                             QMessageBox.Yes | QMessageBox.No)
            if resultado == QMessageBox.Yes:
                self.senalUsuarioCerro.emit(True)
                event.accept()
            else:
                event.ignore()  # No saldremos del evento



if __name__ == '__main__':
    app = QApplication([])
    application = InteractuadorCuestionarios(nombreUsuario="Roni")
    application.show()
    app.exit(app.exec())






