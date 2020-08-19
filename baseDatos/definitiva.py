import sqlite3

miConexion=sqlite3.connect("Multiples")
miCursor=miConexion.cursor()

#CUANDO QUEREMOS QUE LAS CLAVES SEA AUTOMATICAS
#POR CONVENCION SE LES SUELE ASIGNAR EL NOMBRE DE ID..
#PRIMARY KEY==>ATRIBUTO QUE SERA LA LLAVE
#AUTOINCREMENT ==>Los id se iran enumerando
"""
miCursor.execute('''
        CREATE TABLE PREGUNTAS(
        ID_PREGUNTA INTEGER,
        MUTACION INTEGER,
        PREG_TEXT VARCHAR(50),
        PREG_IMAG VARCHAR(50),
        RESPA_TEXT VARCHAR(50),
        RESPA_IMAG VARCHAR(50),
        RESPB_TEXT VARCHAR(50),
        RESPB_IMAG VARCHAR(50),
        RESPC_TEXT VARCHAR(50),
        RESPC_IMAG VARCHAR(50),
        RESPD_TEXT VARCHAR(50),
        RESPD_IMAG VARCHAR(50) )
       '''
)
"""

miConexion.close()




