from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
#DISENO DE LOS MULTIPLES TIPOS DE PREGUNTAS
import numpy as np

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from CUERPO.DISENO_creador.Creador_Pregunta_Multiple.modRespMultiplesImagen50_d import     Ui_Form

###############################################################
#  MIS LIBRERIAS...
##############################################################
from CUERPO.LOGICA_creador.Creador_MisPaquetes.comportSelectImagen_label import comportSelectImagen_label
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiplesImagen50(QtWidgets.QWidget, Ui_Form):
    alguienEligioImagen = pyqtSignal(list)  # idLabelEscogioImagen/direcImagenGuardada/no_labels_imagen

    def __init__(self,nombreCreador="",direc_carpetaImagenes=""):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.NO_LABELS_IMAGEN = 1
        self.vectorRenglon_labelsImagen=np.array([[self.bel_pregImage]]).reshape(1,1)


        self.controlABSOLUTO_labelImagen=comportSelectImagen_label(self,
                                                                 self.vectorRenglon_labelsImagen,
                                                                 nombreCreador,
                                                                 direc_carpetaImagenes,
                                                                RecursosCreadorCuestionarios.ICONO_IMAGEN_DEFAULT)

        self.controlABSOLUTO_labelImagen.alguienEligioImagen.connect(self.notificarMain)

    def notificarMain(self,listaInformacion):
        listaInformacion.append(self.NO_LABELS_IMAGEN)
        self.alguienEligioImagen.emit(listaInformacion)
        idLabelEligioImagen=listaInformacion[0]
        direcGuardoImagen=listaInformacion[1]
        print("Label:",idLabelEligioImagen," Direc: ",direcGuardoImagen)

    def comePolvo(self,id):
        print("POLVO",id)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntasMultiplesImagen50()
    application.show()
    app.exec()
    #sys.exit(app.exec())

