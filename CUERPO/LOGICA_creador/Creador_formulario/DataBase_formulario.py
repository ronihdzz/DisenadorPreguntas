import sqlite3
import os

class DataBase_formulario():
    NAME_TABLA = "DATOS_GENERALES"

    SECCIONES_DATOS_GENERALES = (
        "NOMBRE_USUARIO",
        "EDAD",
        "CLAVE",
        "AMIGO")

    def __init__(self,nameCuestionario):
        self.nameCuestionario=nameCuestionario
        self.BASE_CREADA = False # variable booleana que nos dira
                                 # si ya existe dicha base

    def crearBaseDatos(self):
        '''
        Esta funcion creara la base de datos con el nombre y las secciones
        requeridas
        return:true si hubo exito/false si ocurrio algun error
        '''
        if self.BASE_CREADA:
            return False  # returna false si ocurrio algun error al crear la base
        else:
            my_path =self.nameCuestionario+".db"
            if os.path.isfile(my_path):
               return True #ya esta creada la base de datos...
            else:
                conexion = self.iniciarConexion_sql()
                if conexion==None:
                    print("Error a la hora de crear la base de datos, vuelva a intentarlo....")
                    return False
                else:
                    cursor = conexion.cursor()
                    cursor.execute('''
                            CREATE TABLE DATOS_GENERALES(
                            NOMBRE_USUARIO VARCHAR(150) PRIMARY KEY,
                            EDAD INTEGER,
                            CLAVE VARCHAR(150),
                            AMIGO VARCHAR(150),
                            FOTO_PERFIL  VARCHAR(150),
                            CORREO VARCHAR(150)
                            )        
                            ''')

                    conexion.commit()
                    conexion.close()
                    return True

    def iniciarConexion_sql(self):
        try:
            con = sqlite3.connect(self.nameCuestionario+".db")
            return con
        except:
            return False

    def addUsuario(self,NOMBRE_USUARIO,EDAD,CLAVE,AMIGO,FOTO_PERFIL="",CORREO=""):
        tuplaDatos=(NOMBRE_USUARIO,EDAD,CLAVE,AMIGO,FOTO_PERFIL,CORREO)
        '''
        tuplaDatos: (edad,clave,amigo)
        return False si hubo algun error/True si se agrego correctamente al usuario
        '''
        conexion=self.iniciarConexion_sql()
        if conexion==None:
            print("Error a la hora de agregar al usuario con los datos: ",tuplaDatos)
            return False
        else:
            cursor = conexion.cursor()
            sqlOrden = "INSERT INTO " + self.NAME_TABLA + " VALUES " + str(tuplaDatos)
            cursor.execute(sqlOrden)
            conexion.commit()
            conexion.close()
            return True

    def actualizarDatos(self,DE,NOMBRE_USUARIO=None,EDAD=None,CLAVE=None,AMIGO=None,FOTO_PERFIL=None,CORREO=None):
        '''
        nombre_usuario= Es el ID con el cual ubicaremos de quien queremos editar
                        sus datos
        todas las palabras con el antecedente 'new' son opccionales y solo si se les
        un valor significa que se dea modificar su valor
        return False si no se realizo correctamente/ True hubo algun error
        '''

        dict={
        "EDAD":EDAD,
        "CLAVE":CLAVE,
        "AMIGO":AMIGO,
        "FOTO_PERFIL":FOTO_PERFIL,
        "CORREO":CORREO
        }

        conexion=self.iniciarConexion_sql()
        if conexion==None:
            print("Error a la hora de actualizar los, vuelva a intentarlo....")
            return False
        else:
            cursor = conexion.cursor()
            for elemento,nuevoValor in dict.items():
                if nuevoValor!=None:
                    if type(nuevoValor)==str:
                        nuevoValor="'"+ nuevoValor + "'"
                    sql=f"UPDATE {self.NAME_TABLA} SET {elemento}={nuevoValor} WHERE NOMBRE_USUARIO='{DE}'"
                    cursor.execute(sql)
            # ¿Quiere modificar el valor de la llave?
            if NOMBRE_USUARIO!=None:
                sql = f"UPDATE {self.NAME_TABLA} SET NOMBRE_USUARIO='{NOMBRE_USUARIO}' WHERE NOMBRE_USUARIO='{DE}'"
                cursor.execute(sql)

            #ahora actualizamos la informacion de la base de respuesta..
            conexion.commit()
            conexion.close()
            return True


    def eliminar(self,A):
        conexion=self.iniciarConexion_sql()
        if conexion==None:
            print("Error al eliminar los datos del usuario....")
            return False
        else:
            cursor = conexion.cursor()

            #eliminando la pregunta de la base de datos...
            sql = f"DELETE FROM  {self.NAME_TABLA}  WHERE NOMBRE_USUARIO='{A}'"
            cursor.execute(sql)

            #ejecutando y cerrando base de datos..
            conexion.commit()
            conexion.close()
            return True

    def getDatos(self,DE,EDAD=False,CLAVE=False,AMIGO=False,FOTO_PERFIL=False,CORREO=False):
        dictDatos={
        "EDAD":EDAD,
        "CLAVE":CLAVE,
        "AMIGO":AMIGO,
        "FOTO_PERFIL":FOTO_PERFIL,
        "CORREO":CORREO
        }
        tupla_datosQueQuiere=tuple([ x for x in tuple(dictDatos.keys()) if dictDatos[x]  ])
        str_datosQueQuiere= ",".join(tupla_datosQueQuiere)

        if len(tupla_datosQueQuiere) > 0:
            conexion=self.iniciarConexion_sql()
            if conexion==None:
                print("Error a la hora de obtener los datos de la pregunta....")
                return False
            else:
                cursor = conexion.cursor()

                sql = f"SELECT {str_datosQueQuiere} FROM  {self.NAME_TABLA}  WHERE NOMBRE_USUARIO='{DE}'"
                cursor.execute(sql)

                informacionPregunta=tuple(cursor.fetchall())[0] # la primera de la lista es la informacion .
                dictInformacion={}
                dictInformacion[DE] = dict(zip(tupla_datosQueQuiere,informacionPregunta))

                conexion.commit()
                conexion.close()
                return  dictInformacion
        return {}


    def getAll_datos(self,EDAD=False,CLAVE=False,AMIGO=False,FOTO_PERFIL=False,CORREO=False):
        dictDatos={
        "EDAD":EDAD,
        "CLAVE":CLAVE,
        "AMIGO":AMIGO,
        "FOTO_PERFIL":FOTO_PERFIL,
        "CORREO":CORREO
        }
        tupla_datosQueQuiere=tuple([ x for x in tuple(dictDatos.keys()) if dictDatos[x]  ])
        str_datosQueQuiere= "NOMBRE_USUARIO," +",".join(tupla_datosQueQuiere)

        print(tupla_datosQueQuiere)
        print(str_datosQueQuiere)

        '''
        return False si ocurrio algun error/ tupla  [ (edad,clave,amigo),(edad,clave,amigo),(edad,clave,amigo)...]
        '''
        if len(tupla_datosQueQuiere) > 0:
            conexion = self.iniciarConexion_sql()
            if conexion == None:
                print("Error a la hora de dar los ids....")
                return False
            else:
                cursor = conexion.cursor()
                # necesitamos obtener el tipo de respuesta de la pregunta...
                sqlOrden = f"SELECT  {str_datosQueQuiere} FROM  "+self.NAME_TABLA
                cursor.execute(sqlOrden)
                todosLosDatos= tuple(cursor.fetchall())  # devuelve una lista con

                dictDatos={}
                #listDatos=todosLosDatos
                for x in todosLosDatos:
                    dictDatos[x[0]] = dict(zip(tupla_datosQueQuiere,x[1:]))

                #conexion.commit()
                #conexion.close()
                return dictDatos

        return {}



# Buenas referencias....

#https://likegeeks.com/es/tutorial-de-python-sqlite3/
#https://www.tutorialspoint.com/sqlite/sqlite_python.htm
#https://www.sqlitetutorial.net/sqlite-python/
#https://python-para-impacientes.blogspot.com/2014/02/bases-de-datos-sqlite3.html