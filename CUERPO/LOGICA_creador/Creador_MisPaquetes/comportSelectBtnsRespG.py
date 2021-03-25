from functools import partial

# Comportamiento de selecciones de botones....
class comporSelecBtnsResp():
    # quierePreguntaImagen = pyqtSignal()
    # listEditText,listBtn
    '''
    1)lisBtnResp ==> Lista de los botones que representan
    a la respuesta correcta...

    '''

    def __init__(self,matrizBotones,BORDER_RADIUS = "7",seleccionBotonesMultiple=True):

        self.COLOR_NORMAL = "#EEF2F3"
        self.COLOR_SELECCION = "#9AE5E0"
        self.BORDER_RADIUS = BORDER_RADIUS

        # Metodologia empleada para elegir las RESPUESTAS CORRECTAS
        self.matrizBotones =matrizBotones

        self.ultimoBotonPresionado=-1

        self.seleccionMultiple=seleccionBotonesMultiple # 1 puede seleccionar mas de un boton...
                                                    # 0  solo puede seleccionar uno...

        self.listRespCorrectas=[]
        # todas inicialmente son consideradas
        # incorrectas...
        for _ in range(self.matrizBotones.shape[1]):
            self.listRespCorrectas.append(0)#0=False,1=True


        for c in range(self.matrizBotones.shape[1]):  # columnas
            for r in range(self.matrizBotones.shape[0]):  # renglones
                self.matrizBotones[r][c].clicked.connect(partial(self.marcarDesmarcarRespuesta, c))

        self.incializar()

###################################################################################################
#   S E C C I O N     BOTONES SELECCIONADOS
####################################################################################################

    def dameTodoLoQueRespondio(self):
        return self.listRespCorrectas.copy()

    def dameLaRespuestaEscogio(self):
        posBotonEscogio=self.ultimoBotonPresionado
        return posBotonEscogio

    def getRespuesta(self):
        if self.seleccionMultiple==True: #1==>mas de uno  0==>solo uno
            return self.listRespCorrectas.copy()
        else:
            posBotonEscogio=self.ultimoBotonPresionado
            return posBotonEscogio


    def marcarDesmarcarRespuesta(self,idBtnRespuesta):
        if self.seleccionMultiple==True: #1==>mas de uno  0==>solo uno
            if self.listRespCorrectas[idBtnRespuesta] == True:  # 0=False,1=True
                self.listRespCorrectas[idBtnRespuesta] = 0  # 0=False,1=True
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                        f"border-radius:{self.BORDER_RADIUS}px;"
                                                                        "border: 1px solid #555;")
            else:
                self.listRespCorrectas[idBtnRespuesta] = 1  # 0=False,1=True
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                        f"border-radius:{self.BORDER_RADIUS}px;"
                                                                        "border: 1px solid #555;")
        else: #0==>mas de uno  1==>solo uno
            # si el boton que tratan de seleccionar no fue seleccionado
            if self.ultimoBotonPresionado != idBtnRespuesta and idBtnRespuesta >= 0:
                self.listRespCorrectas[idBtnRespuesta] = 1  # 0=False,1=True
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][self.ultimoBotonPresionado].setStyleSheet(
                        f"background-color:{self.COLOR_NORMAL};"
                        f"border-radius:{self.BORDER_RADIUS}px;"
                        "border: 1px solid #555;")
                self.ultimoBotonPresionado = idBtnRespuesta
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][self.ultimoBotonPresionado].setStyleSheet(
                        f"background-color:{self.COLOR_SELECCION};"
                        f"border-radius:{self.BORDER_RADIUS}px;"
                        "border: 1px solid #555;")
            elif self.ultimoBotonPresionado == idBtnRespuesta:
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][self.ultimoBotonPresionado].setStyleSheet(
                            f"background-color:{self.COLOR_NORMAL};"
                            f"border-radius:{self.BORDER_RADIUS}px;"
                            "border: 1px solid #555;")
                self.ultimoBotonPresionado=-1






    def incializar(self):
        for columna in range(self.matrizBotones.shape[1]):  # columnas...
            for renglon in range(self.matrizBotones.shape[0]): #renglones...
                self.matrizBotones[renglon][columna].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                   f"border-radius:{self.BORDER_RADIUS}px;"
                                                                   "border: 1px solid #555;")


    def setColor(self, newColor):
        self.COLOR_SELECCION=newColor #actualizando el color...
        for columna in range(self.matrizBotones.shape[1]):  # columnas...
            if self.listRespCorrectas[columna]==True:
                for renglon in range(self.matrizBotones.shape[0]): #renglones...
                    self.matrizBotones[renglon][columna].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                       f"border-radius:{self.BORDER_RADIUS}px;"
                                                                       "border: 1px solid #555;")


    def setAllRespuestas(self,newValue):
        self.listRespCorrectas=newValue

        #PONER AL CORRIENTE EL ULTIMO BOTON PRESIONADO...
        for a in range(len(newValue)):
            if newValue[a]==True:
                self.ultimoBotonPresionado=a
                break

        for idBtnRespuesta in range(len(self.listRespCorrectas)):
            if self.listRespCorrectas[idBtnRespuesta]==True:
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_SELECCION};"
                                                                        f"border-radius:{self.BORDER_RADIUS}px;"
                                                                       "border: 1px solid #555;")
            else:
                for r in range(self.matrizBotones.shape[0]):  # renglones
                    self.matrizBotones[r][idBtnRespuesta].setStyleSheet(f"background-color:{self.COLOR_NORMAL};"
                                                                        f"border-radius:{self.BORDER_RADIUS}px;"
                                                                        "border: 1px solid #555;")


'''
    def setAllRespuestas(self,newValue):
    #La siguiente funcion parte de que todo esta virgen, osea deseleccionado...
    #y por consiguiente si uno es True entonces lo seleccionara
    #funciona tanto para la seleccion multiple tanto para la seleccion
    #de una sola respuesta....
        for noBoton in range(len(newValue)):
            if newValue[noBoton]==True:
                self.marcarDesmarcarRespuesta(noBoton)

'''