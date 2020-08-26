from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit



from DISENOS.modRespAbiertaImagen0_d import  Ui_Form
#DISENOS DE LOS MULTIPLES TIPOS DE PREGUNTAS


#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class PreguntaAbiertaImagen_0(QtWidgets.QWidget, Ui_Form):
    quierePreguntaImagen = pyqtSignal()
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.NO_LABELS_IMAGEN =0



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = PreguntaAbiertaImagen_0()
    application.show()
    app.exec()
    #sys.exit(app.exec())

'''
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator


        respuestaTexto=QLineEdit()
        validator = QRegExpValidator(QRegExp("[^\n  ]{1,50}"))
        respuestaTexto.setValidator(validator)

        respuestaTexto.setMinimumSize(500,200)
        respuestaTexto.setMaximumSize(500,200)
        self.layoutRespuesta.addWidget(respuestaTexto)

setValidator()
Sets the validation rules. Available validators are
QIntValidator − Restricts input to integer
QDoubleValidator − Fraction part of number limited to specified decimals
QRegexpValidator − Checks input against a Regex expression
'''