import sqlite3

def getNameBaseAlmaPreg(tipoRespuesta):
    tuplaNombresBases=( ("RESP_trueFalse",5),
                        ("RESP_multiples",9),
                        ("RESP_items",3),
                        ("RESP_abiertas",2)
                     )
    numeroBases = len(tuplaNombresBases)
    if 0<=tipoRespuesta<numeroBases:
        return tuplaNombresBases[tipoRespuesta]

def saveDataRespPreg(basePrincipal,nombreBaseRespuestas,datos):
    miConexion = sqlite3.connect(basePrincipal)
    miCursor = miConexion.cursor()
    sqlOrden = "INSERT INTO "+nombreBaseRespuestas+" VALUES "+datos
    print(sqlOrden)
    miCursor.execute(sqlOrden)
    miConexion.commit()
    miConexion.close()


def addNewQuestion(basePrincipal,nombreBasePreguntas,datos,tipoRespuesta):
    miConexion=sqlite3.connect(basePrincipal)
    miCursor=miConexion.cursor()
    sqlOrden = "INSERT INTO " + nombreBasePreguntas + " VALUES " + datos
    miCursor.execute(sqlOrden)
    idAsignado=miCursor.lastrowid #obteniendo el link asignado...
    print(idAsignado)
    miConexion.commit()
    miConexion.close()
    baseResp=getNameBaseAlmaPreg(tipoRespuesta)
    datosNull="("+str(idAsignado)+","
    #Almenos debe valer 2, ya que todos tienen
    #por default el ID, y aparte tan siquiera
    #deben tener un dato que es el que almacenan
    for i in range(baseResp[1]-2):
        datosNull+="NULL,"
    datosNull+="NULL)"
    print(datosNull)
    saveDataRespPreg(basePrincipal,baseResp[0],datosNull)

def getQuestion(basePrincipal,nombreBasePreguntas,idPregunta):
    miConexion=sqlite3.connect(basePrincipal)
    miCursor=miConexion.cursor()
    sqlOrden = "SELECT * FROM " + nombreBasePreguntas + " WHERE ID="+str(idPregunta)
    miCursor.execute(sqlOrden)
    datosPregunta = miCursor.fetchall()  # devuelve una lista con
    # todos los registros que devuelve
    # la instruccion sql

    #Obteniendo el dato de las preguntas....
    baseResp = getNameBaseAlmaPreg(datosPregunta[0][1]) #ahi esta el tipo de pregunta....
    sqlOrden = "SELECT * FROM " + baseResp[0] + " WHERE ID=" + str(idPregunta)
    miCursor.execute(sqlOrden)
    datosRespuesta = miCursor.fetchall()  # devuelve una lista con
    miConexion.commit()
    miConexion.close()
    return datosPregunta,datosRespuesta



#(gradoImagenes,tiempoSegundos,textoPregunta,imagenPregunta,tamPregunta,posicionPregunta,tipoRespuesta
# tamanoRespuesta,posicionRespuesta,formaEvaluar,respuestas)
#DATOS="(NULL,2,0,120,'¿Cual es tu item?','pene.png',10,0,15,0,0,'00011')"
#addNewQuestion("CreadorPreguntas","TABLA_PREGUNTAS",DATOS,2)

print(getQuestion("CreadorPreguntas","TABLA_PREGUNTAS",5))

