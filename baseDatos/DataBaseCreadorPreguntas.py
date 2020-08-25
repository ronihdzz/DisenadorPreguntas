import sqlite3
import os

class DataBaseCreadorPreguntas():
    def __init__(self,nameCuestionario):
        self.nameCuestionario=nameCuestionario
        self.crearConstantesDataBase()
        self.BASE_CREADA = False





    def crearConstantesDataBase(self):
        self.NAMES_DATABASE_RESPUESTAS=(("RESP_trueFalse", 5),
                                        ("RESP_multiples", 9),
                                        ("RESP_items", 3),
                                        ("RESP_abiertas", 2)
                                        )
        self.NAMES_DATABASE_PREGUNTAS = ("TABLA_PREGUNTAS", 12)


        self.SECCIONES_DATABASE_PREGUNTAS= """
                GRADO_IMAGENES=?,
                TIEMPO_SEGUNDOS=?,
                TEXTO_PREGUNTA=?,
                IMAGEN_PREGUNTA=?,
                TAMANO_PREGUNTA=?,
                POSICION_PREGUNTA=?,
                TAMANO_RESPUESTA=?,
                POSICION_RESPUESTA=?,
                FORMA_EVALUAR=?,
                RESPUESTAS=?
            """

        self.SECCIONES_DATABASE_RESPUESTAS=(
            """
                    TEXTO_RESPA=?,
                    IMAGEN_RESPA=?,
                    TEXTO_RESPB=?,
                    IMAGEN_RESPB=?
            """,
            """
                    TEXTO_RESPA=?,
                    IMAGEN_RESPA=?,
                    TEXTO_RESPB=?,
                    IMAGEN_RESPB=?,
                    TEXTO_RESPC=?,
                    IMAGEN_RESPC=?,
                    TEXTO_RESPD=?,
                    IMAGEN_RESPD=?
            """,
            """
                    NO_ITEMS=?,
                    TEXTO_ITEMS=?
            """
        )

    def crearBaseDatos(self):
        if self.BASE_CREADA:
            pass # no la vamos a crear porque ya fue creada la base de datos....
        else:
            my_path =self.nameCuestionario+".db"
            if os.path.isfile(my_path):
               pass #ya esta creada la base de datos...
            else:
                conexion = self.iniciarConexion_sql()
                if conexion==None:
                    print("Error a la hora de crear la base de datos, vuelva a intentarlo....")
                    return False
                else:
                    cursor = conexion.cursor()
                    cursor.execute('''
                            CREATE TABLE TABLA_PREGUNTAS(
                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            TIPO_RESPUESTA INTEGER,
                            GRADO_IMAGENES INTEGER,
                            TIEMPO_SEGUNDOS INTEGER,
                            TEXTO_PREGUNTA VARCHAR(300),
                            IMAGEN_PREGUNTA VARCHAR(150),
                            TAMANO_PREGUNTA INTEGER,
                            POSICION_PREGUNTA INTEGER,
                            TAMANO_RESPUESTA INTEGER,
                            POSICION_RESPUESTA INTEGER,
                            FORMA_EVALUAR INTEGER,
                            RESPUESTAS VARCHAR(60)         
                            )        
                            ''')

                    cursor.execute('''
                            CREATE TABLE RESP_trueFalse(
                            ID INTEGER PRIMARY KEY,
                            TEXTO_RESPA   VARCHAR(20),
                            IMAGEN_RESPA  VARCHAR(150),
                            TEXTO_RESPB   VARCHAR(20),
                            IMAGEN_RESPB  VARCHAR(150)
                        )''')

                    cursor.execute('''
                            CREATE TABLE RESP_multiples(
                            ID INTEGER PRIMARY KEY,
                            TEXTO_RESPA   VARCHAR(300),
                            IMAGEN_RESPA  VARCHAR(150),
                            TEXTO_RESPB   VARCHAR(300),
                            IMAGEN_RESPB  VARCHAR(150),
                            TEXTO_RESPC   VARCHAR(300),
                            IMAGEN_RESPC  VARCHAR(150),
                            TEXTO_RESPD   VARCHAR(300),
                            IMAGEN_RESPD  VARCHAR(150)
                        )''')

                    cursor.execute('''
                            CREATE TABLE RESP_items(
                            ID INTEGER PRIMARY KEY,
                            NO_ITEMS INTEGER,
                            TEXTO_ITEMS   VARCHAR(900)
                        )''')
                    conexion.commit()
                    conexion.close()

    def iniciarConexion_sql(self):
        try:
            con = sqlite3.connect(self.nameCuestionario+".db")
            return con
        except:
            return False


    def addNewQuestion(self,tipoRespuesta):
        conexion=self.iniciarConexion_sql()
        if conexion==None:
            print("Error a la hora de crear la pregunta, vuelva a intentarlo....")
            return False
        else:
            cursor = conexion.cursor()

            datosDataBase_respuestas=self.NAMES_DATABASE_RESPUESTAS[tipoRespuesta]
            datosDataBase_preguntas=self.NAMES_DATABASE_PREGUNTAS

            #Almenos debe valer 2, ya que todos tienen
            #por default el ID, y aparte tan siquiera
            #deben tener un dato que es el que almacenan
            #datosNull_pregunta = "( NULL,"
            datosNull_pregunta = "( NULL," + str(tipoRespuesta) + ","
            for i in range(datosDataBase_preguntas[1]-3):
                datosNull_pregunta+="NULL,"
            datosNull_pregunta+="NULL)"

            #A continuacion registramos la creacion de una pregunta en la base de datos...
            sqlOrden = "INSERT INTO "+datosDataBase_preguntas[0]+ " VALUES " + datosNull_pregunta
            cursor.execute(sqlOrden)
            idAsignado=cursor.lastrowid #obteniendo el link asignado...

            if tipoRespuesta!=3: #las respuestas abiertas no tienen
                #A continuacion registramos las respuestas en su respectiva tabla....
                datosNull_respuestas = "(" + str(idAsignado) + ","
                for i in range(datosDataBase_respuestas[1] - 2):
                    datosNull_respuestas += "NULL,"
                datosNull_respuestas += "NULL)"
                sqlOrden = "INSERT INTO " + datosDataBase_respuestas[0] + " VALUES " + datosNull_respuestas
                cursor.execute(sqlOrden)

            conexion.commit()
            conexion.close()
            return idAsignado


    def actualizarDatosPregunta(self,idPregunta,newValuePregunta,newValueRespuesta):
        conexion=self.iniciarConexion_sql()
        if conexion==None:
            print("Error a la hora de actualizar la pregunta, vuelva a intentarlo....")
            return False
        else:
            cursor = conexion.cursor()
            #le agregamos a la tupla de nuevos valores el id
            #de la pregunta de la cual queremos modificar,ya que
            #con ese dato se llena el apartado de WHERE ID...
            newDataPregunta = newValuePregunta+(idPregunta,)
            print(newDataPregunta)
            elemetosEditar=self.SECCIONES_DATABASE_PREGUNTAS
            elemetosEditar+=" WHERE ID=?"
            sqlOrden = "UPDATE " + self.NAMES_DATABASE_PREGUNTAS[0] + " SET "
            sqlOrden+=elemetosEditar
            cursor.execute(sqlOrden, newDataPregunta)

            #necesitamos obtener el tipo de respuesta de la pregunta...
            sqlOrden = "SELECT * FROM " + self.NAMES_DATABASE_PREGUNTAS[0] + " WHERE "
            sqlOrden+=" ID="+str(idPregunta)
            cursor.execute(sqlOrden)
            infoPregunta= cursor.fetchall()  # devuelve una lista con
            tipoRespuesta = infoPregunta[0][1]  # ahi se encuentra almacenada el tipo de respuesta
            print(tipoRespuesta)
            if tipoRespuesta != 3:  # las respuestas abiertas no tienen
                newDataRespuesta = newValueRespuesta + (idPregunta,)
                print(newDataPregunta)
                elemetosEditar = self.SECCIONES_DATABASE_RESPUESTAS[tipoRespuesta]
                elemetosEditar += " WHERE ID=?"
                sqlOrden = "UPDATE " + self.NAMES_DATABASE_RESPUESTAS[tipoRespuesta][0]+" SET "
                sqlOrden += elemetosEditar
                print(sqlOrden)
                cursor.execute(sqlOrden,newDataRespuesta)

            #ahora actualizamos la informacion de la base de respuesta..
            conexion.commit()
            conexion.close()

    def eliminarPregunta(self,idPregunta):
        conexion=self.iniciarConexion_sql()
        if conexion==None:
            print("Error al eliminar la pregunta....")
            return False
        else:
            cursor = conexion.cursor()
            #necesitamos obtener el tipo de respuesta de la pregunta...
            sqlOrden = "SELECT * FROM " + self.NAMES_DATABASE_PREGUNTAS[0] + " WHERE "
            sqlOrden+=" ID="+str(idPregunta)
            cursor.execute(sqlOrden)
            infoPregunta= cursor.fetchall()  # devuelve una lista con una tupla de informacion de
                                             # la pregunta...
            tipoRespuesta = infoPregunta[0][1]  # ahi se encuentra almacenada el tipo de respuesta
            print("RESPUESTA ELIMINAR... ",tipoRespuesta)

            #eliminando la pregunta de la base de datos...
            sqlOrden = "DELETE FROM " + self.NAMES_DATABASE_PREGUNTAS[0] + " WHERE "
            sqlOrden += " ID=" + str(idPregunta)
            cursor.execute(sqlOrden)

            if tipoRespuesta != 3:  # las respuestas abiertas no tienen
                #eliminando la repuesta de la base de datos...
                sqlOrden = "DELETE FROM " + self.NAMES_DATABASE_RESPUESTAS[tipoRespuesta][0]+ " WHERE "
                sqlOrden += " ID=" + str(idPregunta)
                cursor.execute(sqlOrden)

            #ejecutando y cerrando base de datos..
            conexion.commit()
            conexion.close()



    def getData(self,idPregunta):
        conexion=self.iniciarConexion_sql()
        if conexion==None:
            print("Error a la hora de actualizar la pregunta, vuelva a intentarlo....")
            return False
        else:
            cursor = conexion.cursor()
            sqlOrden = "SELECT * FROM " + self.NAMES_DATABASE_PREGUNTAS[0] + " WHERE "
            sqlOrden+=" ID="+str(idPregunta)
            cursor.execute(sqlOrden)
            listInformacion=[None,None]
            informacionPregunta= cursor.fetchall()  # devuelve una lista de tuplas....
            listInformacion[0]=informacionPregunta[0]


            #necesitamos obtener el tipo de respuesta de la pregunta...
            sqlOrden = "SELECT * FROM " + self.NAMES_DATABASE_PREGUNTAS[0] + " WHERE "
            sqlOrden+=" ID="+str(idPregunta)
            cursor.execute(sqlOrden)
            infoPregunta= cursor.fetchall()  # devuelve una lista con
            tipoRespuesta = infoPregunta[0][1]  # ahi se encuentra almacenada el tipo de respuesta
            print("RESPUESTA ELIMINAR... ",tipoRespuesta)

            if tipoRespuesta != 3:  # las respuestas abiertas no tienen
                sqlOrden = "SELECT * FROM " + self.NAMES_DATABASE_RESPUESTAS[tipoRespuesta][0]+ " WHERE "
                sqlOrden += " ID=" + str(idPregunta)
                cursor.execute(sqlOrden)
                informacionRespuesta=cursor.fetchall()  # devuelve una lista de tuplas....
                listInformacion[1] = informacionRespuesta[0]
            conexion.commit()
            conexion.close()
            return  listInformacion


    def actualizarImagenPregunta(self, idPregunta, newValue):
        conexion = self.iniciarConexion_sql()
        if conexion == None:
            print("Error a la hora de actualizar la pregunta, vuelva a intentarlo....")
            return False
        else:
            cursor = conexion.cursor()
            # le agregamos a la tupla de nuevos valores el id
            # de la pregunta de la cual queremos modificar,ya que
            # con ese dato se llena el apartado de WHERE ID...
            newDataImagen = (newValue,) + (idPregunta,)

            elemetosEditar = "  IMAGEN_PREGUNTA=?"
            elemetosEditar += " WHERE ID=?"
            sqlOrden = "UPDATE " + self.NAMES_DATABASE_PREGUNTAS[0] + " SET "
            sqlOrden += elemetosEditar
            cursor.execute(sqlOrden, newDataImagen)
        conexion.commit()
        conexion.close()

    def actualizarImagenRespuesta(self, idPregunta, nombreRespuesta, newValor):
        conexion = self.iniciarConexion_sql()
        if conexion == None:
            print("Error a la hora de actualizar la pregunta, vuelva a intentarlo....")
            return False
        else:
            cursor = conexion.cursor()
            # necesitamos obtener el tipo de respuesta de la pregunta...
            sqlOrden = "SELECT * FROM " + self.NAMES_DATABASE_PREGUNTAS[0] + " WHERE "
            sqlOrden += " ID=" + str(idPregunta)
            cursor.execute(sqlOrden)
            infoPregunta = cursor.fetchall()  # devuelve una lista con
            tipoRespuesta = infoPregunta[0][1]  # ahi se encuentra almacenada el tipo de respuesta

            if tipoRespuesta !=2 and tipoRespuesta!=3:  # las respuestas 'items' y 'abiertas'
                                                        #no tienen respuesta imagen...
                newDataImage = (newValor,idPregunta)
                elemetosEditar = "IMAGEN_RESP"+nombreRespuesta+"=?"  # IMAGEN_RESPA OR IMAGEN_RESPB...
                elemetosEditar += " WHERE ID=?"
                sqlOrden = "UPDATE " + self.NAMES_DATABASE_RESPUESTAS[tipoRespuesta][0] + " SET "
                sqlOrden += elemetosEditar
                cursor.execute(sqlOrden, newDataImage)

            # ahora actualizamos la informacion de la base de respuesta..
            conexion.commit()
            conexion.close()

#gradoImagenes,tiempo_segundos,texto_pregunta,imagen_pregunta,tam_pregunta,pos_pregunta,
#tam_respuesta,pos_respuesta,forma_evaluar,respuestas

#roni=DataBaseCreadorPreguntas("CORAZON")
#roni.crearBaseDatos()
#print(roni.addNewQuestion(0))
#print(roni.getData(1))

#roni.actualizarImagenPregunta(4,"PENES_GRANDEStJugosos.png")

# P R O B A N D O   L A    E D I C I O N    D E    I M A G E N E S :
#roni.actualizarImagenRespuesta(4,'A',"MAMARpenesSEMES.png")


#roni.eliminarPregunta(1)

#  P R O B A N D O    Q U E   T O D O   T I P O    D E     A C T U A L I Z A C I O N E S   F U N C I O N E :

#Actualizar datos de tipo de respuesta true/false...
#newDatosPregunta=(3,120,'¿Me dejas mamar tu pene, y despues me penetras ?','PENEGRANDE.png',10,0,15,0,0,'peneNoPenepeneNoPene')
#newDatosRespuesta=("10","RONI.png","40","elroni.png")
#roni.actualizarDatosPregunta(2,newDatosPregunta,newDatosRespuesta)


#Actualizar datos de tipo de respuesta multiples...
#newDatosPregunta=(4,120,'¿Me dejas mamar tu pene, y despues me penetras ?','PENEGRANDE.png',10,0,15,0,0,'peneNoPenepeneNoPene')
#newDatosRespuesta=("10","RONI.png","40","elroni.png","20","quetal.png","30","nolose.png")
#roni.actualizarDatosPregunta(3,newDatosPregunta,newDatosRespuesta)

#Actualizar datos de tipo de respuesta items...
#newDatosPregunta=(1,120,'¿Me dejas mamar tu pene, y despues me penetras ?','PENEGRANDE.png',10,0,15,0,0,'peneNoPenepeneNoPene')
#newDatosRespuesta=(5,"[hola bla,blablabla,blabla,blabla,blabla]")
#roni.actualizarDatosPregunta(4,newDatosPregunta,newDatosRespuesta)


#Actualizar datos de tipo de respuestas abiertas...
#newDatosPregunta=(1,120,'¿Me dejas mamar tu pene, y despues me penetras ?','PENEGRANDE.png',10,0,15,0,0,'peneNoPenepeneNoPene')
#newDatosRespuesta=("")
#roni.actualizarDatosPregunta(6,newDatosPregunta,newDatosRespuesta)




# Buenas referencias....

#https://likegeeks.com/es/tutorial-de-python-sqlite3/
#https://www.tutorialspoint.com/sqlite/sqlite_python.htm
#https://www.sqlitetutorial.net/sqlite-python/
#https://python-para-impacientes.blogspot.com/2014/02/bases-de-datos-sqlite3.html