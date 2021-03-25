from PyQt5.QtCore import pyqtSignal,QObject
from functools import partial
import numpy as np

# Comportamiento de selecciones de botones....
class comportAutoguardado_textEdit(QObject):
    horaGuardarCambios= pyqtSignal(list) #[idResp,textResp]
    # listEditText,listBtn
    '''
    1)lisBtnResp ==> Lista de los botones que representan
    a la respuesta correcta...

    '''
    def __init__(self,matrizTextEdit):
        QObject.__init__(self)

        self.matrizTextEdit =matrizTextEdit
        self.vectorRenglon_noCambios = np.zeros([1, matrizTextEdit.shape[1]], dtype=int)
        self.GUARDAR_CADA = 10
        self.posTextEdit_estanEditando=[-1,-1]

        for c in range(self.matrizTextEdit.shape[1]): #columnas
            for r in range(self.matrizTextEdit.shape[0]): #renglones
                self.matrizTextEdit[r][c].textChanged.connect(partial(self.registrarRespuestas,True))
                self.matrizTextEdit[r][c].selectionChanged.connect(partial(self.cambioTextEdit,r,c))

    def registrarRespuestas(self,ordenAutomatica):
        renglon,columna=self.posTextEdit_estanEditando
        if renglon==-1  or columna==-1:
            pass #no ha habido ningun cambio..
        else:
            if self.vectorRenglon_noCambios[0][columna] > self.GUARDAR_CADA or not(ordenAutomatica):
                self.vectorRenglon_noCambios[0][columna] = 0
                self.horaGuardarCambios.emit( [ columna,
                                                self.matrizTextEdit[renglon][columna].toPlainText()
                                                ])
            self.vectorRenglon_noCambios[0][columna] += 1

    def cambioTextEdit(self,renglonNew,columnaNew):
        if [renglonNew,columnaNew] != self.posTextEdit_estanEditando:
            renglonPrev,columnaPrev=self.posTextEdit_estanEditando
            self.horaGuardarCambios.emit([   columnaPrev,
                                             self.matrizTextEdit[renglonPrev][columnaPrev].toPlainText()
                                          ])
            self.posTextEdit_estanEditando=[renglonNew,columnaNew]


