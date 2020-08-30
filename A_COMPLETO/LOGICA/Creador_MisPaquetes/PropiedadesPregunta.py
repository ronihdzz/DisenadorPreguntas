class PropiedadesPregunta():

    def __init__(self):
        self.PROPIEDADES_PREGUNTA={
            "GRADO_IMAGENES":0,#0=sin imagen 1=con imagen en pregunta....
            "TIEMPO_SEGUNDOS":0,
            "TEXTO_PREGUNTA":"NULL",
            "IMAGEN_PREGUNTA":"NULL",
            "TAMANO_PREGUNTA":15,
            "POSICION_PREGUNTA":1, #0=left 1=center  2=rigth
            "TAMANO_RESPUESTA":0,
            "POSICION_RESPUESTA":1, #0=left 1=center  2=rigth
            "FORMA_EVALUAR":0, #0=cualquiera  1=todas
            "RESPUESTAS": "NULL"
        }


'''
Es importante recordar que debemos poner en estado default
de preguntas, al gradosImagenes=0 ya que para que la imagen
guardada se pueda ver se tiene que cambiar aunque sea una
vez de widget, y si quieres ver una imagen ¿tendras que
cambiarla a una widget con imagen?claro que si
'''