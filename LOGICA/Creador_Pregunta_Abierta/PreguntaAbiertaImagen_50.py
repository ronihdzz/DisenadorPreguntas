from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import numpy as np

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from DISENO.Creador_Pregunta_Abierta.modRespAbiertaImagen50_d import  Ui_Form

###############################################################
#  MIS LIBRERIAS...
##############################################################
from LOGICA.Creador_MisPaquetes.comportSelectImagen_label import comportSelectImagen_label
from LOGICA.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaAbiertaImagen_50(QtWidgets.QWidget, Ui_Form):
    alguienEligioImagen = pyqtSignal(list) # idLabelEscogioImagen/direcImagenGuardada/NO_LABELS_IMAGEN

    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.vectorRenglon_labelsImagen=np.array([[self.bel_pregImage]]).reshape(1,1)

        self.NO_LABELS_IMAGEN = 1
        self.controlABSOLUTO_labelImagen=comportSelectImagen_label(self,
                                                                 self.vectorRenglon_labelsImagen,
                                                                 "Roni",
                                                                 "HOLA",
                                                                 RecursosCreadorCuestionarios.ICONO_IMAGEN_DEFAULT)

        self.controlABSOLUTO_labelImagen.alguienEligioImagen.connect(self.notificarMain)

    def notificarMain(self,listaInformacion):
        listaInformacion.append(self.NO_LABELS_IMAGEN)
        self.alguienEligioImagen.emit(listaInformacion)
        idLabelEligioImagen=listaInformacion[0]
        direcGuardoImagen=listaInformacion[1]
        print("Label:",idLabelEligioImagen," Direc: ",direcGuardoImagen)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaAbiertaImagen_50()
    application.show()
    app.exec()
    #sys.exit(app.exec())
