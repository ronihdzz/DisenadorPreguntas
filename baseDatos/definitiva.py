import sqlite3

miConexion=sqlite3.connect("CreadorPreguntas")
miCursor=miConexion.cursor()

#CUANDO QUEREMOS QUE LAS CLAVES SEA AUTOMATICAS
#POR CONVENCION SE LES SUELE ASIGNAR EL NOMBRE DE ID..
#PRIMARY KEY==>ATRIBUTO QUE SERA LA LLAVE
#AUTOINCREMENT ==>Los id se iran enumerando

miCursor.execute('''
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
        RESPUESTAS VARCHAR(50)         
        )        
        ''')


miCursor.execute('''
        CREATE TABLE RESP_trueFalse(
        ID INTEGER PRIMARY KEY,
        TEXTO_RESPA   VARCHAR(20),
        IMAGEN_RESPA  VARCHAR(150),
        TEXTO_RESPB   VARCHAR(20),
        IMAGEN_RESPB  VARCHAR(150)
    )''')

miCursor.execute('''
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


miCursor.execute('''
        CREATE TABLE RESP_items(
        ID INTEGER PRIMARY KEY,
        NO_ITEMS INTEGER,
        TEXTO_ITEMS   VARCHAR(900)
    )''')

miCursor.execute('''
        CREATE TABLE RESP_abiertas(
        ID INTEGER PRIMARY KEY,
        TEXTO_ITEMS   VARCHAR(50)
    )''')


miConexion.close()




