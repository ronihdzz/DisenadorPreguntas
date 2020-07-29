from PyQt5 import QtWidgets,QtGui,Qt,QtCore
from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QPushButton,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem #para las tablas...
from diseno1_d import Ui_Form

#https://www.youtube.com/watch?v=P-SZn5eSDp8&list=PL7Euic11sPg_OYLhPN3QUh3BZINlhFApE
class evalEqui_1(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        Ui_Form.__init__(self)
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)



        self.widgetTipoPreguntas=QWidget()
        self.hbox=QHBoxLayout()
        for i in range(1,4):
            object = QPushButton(str(i))
            object.setStyleSheet( "margin: 1px;" )
            object.setMinimumSize(50,30)
            object.setMaximumSize(50,30)
            self.hbox.addWidget(object)
        self.widgetTipoPreguntas.setLayout(self.hbox)

        #Scroll Area Properties
        self.scroll_tipoPregunta.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_tipoPregunta.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_tipoPregunta.setWidgetResizable(False)
        self.scroll_tipoPregunta.setWidget(self.widgetTipoPreguntas)





        self.widget = QWidget()                 # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()               # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for i in range(1,50):
            object = QPushButton(str(i))
            object.setStyleSheet( "margin: 1px;" )
            object.setMinimumSize(50,50)
            object.setMaximumSize(50,50)
            self.vbox.addWidget(object)


        self.widget.setLayout(self.vbox)

        #Scroll Area Properties
        self.scroll_barra.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_barra.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_barra.setWidgetResizable(True)
        self.scroll_barra.setWidget(self.widget)

        #
        self.btn_aplicarTam.clicked.connect(self.changedSize)

    def changedSize(self):
        #Cambiando el tamaño
        newTam=self.lineEdit_tamano.text()
        font = QtGui.QFont()
        font.setPointSize(int(newTam))
        self.txtEdit_preg.setFont(font)




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = evalEqui_1()
    application.show()
    app.exec()
    #sys.exit(app.exec())

