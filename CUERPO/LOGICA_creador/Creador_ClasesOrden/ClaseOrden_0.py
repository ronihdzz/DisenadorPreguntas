import os

class ClaseOrden_0():
    NOMBRE_APLICACION="RonTest"

    direc_normal = "../../../RECURSOS/"

    direc_DataUsuario = direc_normal + "/USUARIOS/"
    direc_FotosUsuario=direc_DataUsuario+"/FOTOS/"

    # crea estos directorios, en caso dE ya existir no hacer nada...
    os.makedirs(direc_DataUsuario, exist_ok=True)
    # crea estos directorios, en caso dE ya existir no hacer nada...
    os.makedirs(direc_FotosUsuario, exist_ok=True)

    # esta direccion dira donde se encuentra la base de datos
    BASE_DATOS_DATOS_GENERALES = direc_DataUsuario + "DatosGenerales"

    IMAGEN_DEFAULT_USUARIO=direc_FotosUsuario+"default.png"


    def __init__(self):
        pass

    @staticmethod
    def cambiarDireccion(newDirec=""):
        '''
        newDirec==>es la nueva direccion, no olvidar que debe terminar
        en........................... '/'
        '''
        ClaseOrden_0.direc_normal=newDirec
        ClaseOrden_0.direc_DataUsuario=ClaseOrden_0.direc_normal + "/USUARIOS/"
        ClaseOrden_0.direc_FotosUsuario=ClaseOrden_0.direc_DataUsuario  + "/FOTOS/"


        # crea estos directorios, en caso dE ya existir no hacer nada...
        os.makedirs(ClaseOrden_0.direc_DataUsuario, exist_ok=True)
        # crea estos directorios, en caso dE ya existir no hacer nada...
        os.makedirs(ClaseOrden_0.direc_FotosUsuario, exist_ok=True)

        # esta direccion dira donde se encuentra la base de datos
        # que almacena los datos del usuario...
        ClaseOrden_0.BASE_DATOS_DATOS_GENERALES =  ClaseOrden_0.direc_DataUsuario + "DatosGenerales"

        ClaseOrden_0.IMAGEN_DEFAULT_USUARIO = "default.png"
