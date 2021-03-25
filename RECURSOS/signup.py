import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

creds = credentials.Certificate('firebase-sdk.json')
baseDatos = 'https://delphiadata.firebaseio.com/'

firebase_admin.initialize_app(creds,{
    'databaseURL': baseDatos
})



#Dar de alta usuarios

"""
lis = auth.create_user(email="417lisettehg@gmail.com",password="contrasena",uid="lissetehg")
jorge = auth.create_user(email="jorgebra53@gmail.com",password="contrasena",uid="jorgebd")
roni = auth.create_user(email="ronaldo.runing_@hotmail.com",password="contrasena",uid="roniherbe")
bren = auth.create_user(email="navagarcia160a@gmail.com",password="contrasena",uid="brendagc")
dilan = auth.create_user(email="dilanemanuel@gmail.com",password="contrasena",uid="dilichili")
print(dilan)
print(lis)
print(jorge)
print(roni)
print(bren)"""


