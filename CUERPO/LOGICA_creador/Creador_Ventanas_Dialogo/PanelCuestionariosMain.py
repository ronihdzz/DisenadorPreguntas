from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox,QHeaderView
from PyQt5.QtGui import QStandardItemModel,QStandardItem
from PyQt5.QtWidgets import  QMessageBox,QAction,QActionGroup,QWidget,QVBoxLayout,QTabWidget,QLabel
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSignal   #mandas senales a la otra ventana

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Ventanas_Dialogo.PanelCuestionariosMain_d import Ui_Dialog

###############################################################
#  IMPORTACIONES DE LAS DEMAS VENTANAS LOGICAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_Ventanas_Dialogo.PanelCuestionariosMios import PanelCuestionariosMios
from CUERPO.LOGICA_creador.Creador_Ventanas_Dialogo.PanelCuestionariosDescargados import PanelCuestionariosDescargados
from CUERPO.LOGICA_creador.Creador_MisPaquetes.comportSelect_btnsImagen import comporSelec_btnsImagen
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios
from CUERPO.LOGICA_creador.Creador_Ejecutador.VisualizadorTodoCuestionario import VisualizadorTodoCuestionario
from CUERPO.LOGICA_creador.Creador_MisPaquetes.cuestionariosDelphi import CuestionariosDelphi



class PanelCuestionariosMain(QDialog,Ui_Dialog):
    senalCuestionarioElegido = pyqtSignal(dict)  # comunicacion con la aplicacionn
    def __init__(self):
        Ui_Dialog.__init__(self)
        QDialog.__init__(self)
        self.setupUi(self)

        self.ventana_misCuestionarios = PanelCuestionariosMios()
        self.ventana_descargadosCuestionarios = PanelCuestionariosDescargados()

        # SENALES...
        self.ventana_misCuestionarios.senalCuestionarioElegido.connect(self.abrirCuestionario)
        self.ventana_descargadosCuestionarios.senalCuestionarioElegido.connect(self.abrirCuestionario)

        # VAMO A COLOCAR NOMBRES DE CUESTIONARIOS...
        self.refrescarDatosCuestionarios(descargas=True, mios=True)

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


    def verOtrosCuestionarios(self, idBtnFuePresionado):
        self.controlABSLUTO_tipoCuestionarios.marcarDesmarcarRespuesta_automatico(idBtnFuePresionado, False)
        if idBtnFuePresionado == 1:  # quiere ver los cuestionarios descargados...
            self.listWidget.setCurrentIndex(1)
        else:  # quiere ver su respuesta...
            self.listWidget.setCurrentIndex(0)


    def refrescarDatosCuestionarios(self, descargas=False, mios=False):
        if mios:
            self.listCuestionariosMios = CuestionariosDelphi.getNombresCuestionarios(mios=True)
            self.ventana_misCuestionarios.mostrarTablaCuestionarios(self.listCuestionariosMios)
            self.listNombresCuestionariosMios = [x["NOMBRE"] for x in self.listCuestionariosMios]
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(self.listCuestionariosMios)
        if descargas:
            self.listCuestionariosDescargados = CuestionariosDelphi.getNombresCuestionarios(descargados=True)
            self.ventana_descargadosCuestionarios.mostrarTablaCuestionarios(self.listCuestionariosDescargados)
            self.listNombresCuestionariosDescargados = [x["NOMBRE"] for x in self.listCuestionariosDescargados]
            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            print(self.listCuestionariosDescargados)

    def abrirCuestionario(self, dicInfo):
        # dictInfo==> llaves:NOMBRE y TIPO==>DESCARGADOS OR MIOS

        nombreCuestionario = dicInfo["NOMBRE"]

        # self.dictDatos = dictDatos  # "ConfirmacionMensaje","ConfirmacionClave","Accion","Explicacion"
        indicaciones = "En delphiApp nos preocupa que NO hagas cosas accidentalmente,"
        indicaciones += "y mas en acciones  trascedentales,por "
        indicaciones += "tal motivo empleamos este metodo de confirmacion, ¿en verdad "
        indicaciones += "estas seguro de que este cuestionario es el correcto?"

        claveConfirmacion = "estoy seguro"
        accion = "CONFIRMAR QUE ES EL CUESTIONARIO QUE QUIERO"
        explicacion = "Por favor, navega por el cuestionario para que corrobores acerca "
        explicacion += "de si es el cuestionario que deseas"

        dicDatos = {
            "ConfirmacionMensaje": indicaciones,
            "ConfirmacionClave": claveConfirmacion,
            "Accion": accion,
            "Explicacion": explicacion
        }

        if dicInfo["TIPO"] == "MIOS":

            self.cuestionarioMio = VisualizadorTodoCuestionario(nombreCuestionario=nombreCuestionario,
                                                                dictDatos=dicDatos,
                                                                mios=True)
            self.cuestionarioMio.senalCuestionarioConfirmado.connect(lambda x:self.cuestionarioElegido(dicInfo))
            self.setEnabled(False)
            self.cuestionarioMio.senalTermino.connect(lambda : self.setEnabled(True) )


            self.cuestionarioMio.show()
        else:
            self.cuestionarioDescargado = VisualizadorTodoCuestionario(nombreCuestionario=nombreCuestionario,
                                                                       dictDatos=dicDatos,
                                                                       descargados=True)
            self.cuestionarioDescargado.senalCuestionarioConfirmado.connect(lambda x: self.cuestionarioElegido(dicInfo))
            self.setEnabled(False)
            self.cuestionarioDescargado.senalTermino.connect(lambda: self.setEnabled(True))
            self.cuestionarioDescargado.show()

    def cuestionarioElegido(self,dictInformacion):
        self.senalCuestionarioElegido.emit(dictInformacion)#dictInfo==> llaves:NOMBRE y TIPO==>DESCARGADOS OR MIOS
        print(dictInformacion)
        self.close()





if __name__ == '__main__':
    app = QApplication([])
    application = PanelCuestionariosMain()
    application.show()
    app.exit(app.exec())

#FUENTE DE ICONOS:
#https://p.yusukekamiyamane.com/
#https://icons8.com/?utm_source=http%3A%2F%2Ficons8.com%2Fweb-app%2Fnew-icons%2Fall&utm_medium=link&utm_content=search-and-download&utm_campaign=yusuke

