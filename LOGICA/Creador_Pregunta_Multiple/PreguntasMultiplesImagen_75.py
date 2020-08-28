from PyQt5 import QtWidgets
import numpy as np
from PyQt5.QtCore import pyqtSignal

###############################################################
#  IMPORTACION DEL DISEÑO...
##############################################################
from DISENO.Creador_Pregunta_Multiple.modRespMultiplesImagen75_d import  Ui_Form

###############################################################
#  MIS LIBRERIAS...
##############################################################
from LOGICA.Creador_MisPaquetes.comportSelectImagen_label import comportSelectImagen_label
from LOGICA.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntasMultiplesImagen75(QtWidgets.QWidget, Ui_Form):
    alguienEligioImagen = pyqtSignal(list)  # idLabelEscogioImagen/direcImagenGuardada/no_labels_imagen

    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)

        self.vectorRenglon_labelsImagen=np.array([[self.bel_imageRespA,self.bel_imageRespB,
                                                   self.bel_imageRespC,self.bel_imageRespD]]).reshape(1,4)

        self.NO_LABELS_IMAGEN = 4
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
    application = PreguntasMultiplesImagen75()
    application.show()
    app.exec()
    #sys.exit(app.exec())




'''

        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPosPreg = (self.btn_pregIzq, self.btn_pregCen, self.btn_pregDer)
        self.control = comporEdit_TextEdit(self.listBtnPosPreg, self.dSpin_pregTam, [self.txtEdit_preg])

        ## Comportamiento de las ediciones de un edit text...
        self.listBtnPosResp = (self.btn_respIzq, self.btn_respCen, self.btn_respDer)
        self.control2 = comporEdit_TextEdit(self.listBtnPosResp, self.dSpin_respTam,
                                            [self.txtEdit_respA, self.txtEdit_respB, self.txtEdit_respC,
                                             self.txtEdit_respD])


        # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.listBtnPunterosResp = (self.btn_respA, self.btn_respB, self.btn_respC, self.btn_respD)
        self.control3 = comporSelecBtnsResp(self.listBtnPunterosResp)






'''