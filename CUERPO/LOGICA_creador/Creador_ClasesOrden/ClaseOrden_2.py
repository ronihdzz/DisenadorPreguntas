import os

class ClaseOrden_2():



    direc_normal="../../../RECURSOS/"

    direc_DataUsuario=direc_normal+"/USUARIOS/"

    # crea estos directorios, en caso dE ya existir no hacer nada...
    os.makedirs(direc_DataUsuario, exist_ok=True)

    #esta direccion dira donde se encuentra la base de datos
    #que almacena los datos del usuario...
    BASE_DATOS_DATOS_GENERALES=direc_DataUsuario+"DatosGenerales"



    def __init__(self):
        pass


    @staticmethod
    def cambiarDireccion(newDirec=""):
        '''
        newDirec==>es la nueva direccion, no olvidar que debe terminar
        en........................... '/'
        '''

        ClaseOrden_2.BASE_DATOS_DATOS_GENERALES = newDirec + "DatosGenerales"

        direc_normal = "../../../RECURSOS/"

        direc_DataUsuario = direc_normal + "/USUARIOS/"

        # crea estos directorios, en caso dE ya existir no hacer nada...
        os.makedirs(direc_DataUsuario, exist_ok=True)

        # esta direccion dira donde se encuentra la base de datos
        # que almacena los datos del usuario...
        BASE_DATOS_DATOS_GENERALES = direc_DataUsuario + "DatosGenerales"