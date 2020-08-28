'''
        #Preguntas binarias...
        self.ventanas[0]=PreguntasBinarias()
        self.ventanas[1] = PreguntasMultiplesImagen50()
        self.ventanas[2]=PreguntasMultiplesImagen100()

        #Preguntas multiples...
        self.ventanas[3]=PreguntasMultiples()
        self.ventanas[4] = PreguntasMultiplesImagen50()
        self.ventanas[5] = PreguntasMultiplesImagen100()

        #Preguntas especificias
        self.ventanas[6]=PreguntasEspecificas()
        self.ventanas[7] = PreguntasMultiplesImagen50()
        self.ventanas[8] = PreguntasMultiplesImagen100()

        #Preguntas codigo
        self.ventanas[9]=PreguntasMultiples() #preguntas codigo
        self.ventanas[10] = PreguntasMultiplesImagen50()
        self.ventanas[11] = PreguntasMultiplesImagen100()

'''


class constProgram():
    PREG_BINARIA=0
    PREG_MULTIPLES = 1
    PREG_ESPECIFICAS=2

