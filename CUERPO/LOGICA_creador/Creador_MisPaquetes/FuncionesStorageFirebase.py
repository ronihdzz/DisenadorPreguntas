#documentacion...
#https://cloud.google.com/storage/docs/deleting-objects#storage-delete-object-python
from CUERPO.LOGICA_creador.Creador_MisPaquetes.RecursosCuestionario import RecursosCreadorCuestionarios

class FuncionesStorageFirebase():
    def __init__(self,objetoStorageClient):
        self.objetoStorageClient=objetoStorageClient
        self.nombreStorage=RecursosCreadorCuestionarios.NOMBRE_STORAGE
        self.bucket=self.objetoStorageClient.get_bucket(RecursosCreadorCuestionarios.NOMBRE_STORAGE)

    def subirDocumento(self,nameFull_documentSubir,nameFull_destino):
        try:
            blob =self.bucket.blob(nameFull_destino)
            blob.upload_from_filename(nameFull_documentSubir)
            return  True
        except:
            print("Error a la hora de subir documento")
            return None

    def getListNombresDocumentos(self,direccionStorage,prefix=None):
        try:
            blobs = self.objetoStorageClient.list_blobs(
                self.nombreStorage, prefix=direccionStorage,delimiter='/')
            listNombres=[]#agregamos el nombre de la ruta principal

            if prefix==None:
                for blob in blobs:#si no itero esto los prefijos no funcionan
                    dato=blob.name
                    dato=dato.replace(direccionStorage,"")#quitamo el prefijo de la direccion
                    listNombres.append(dato)
                listNombres=listNombres[1:] #quitamos el prefijo de la lista...
            else:
                for blob in blobs:#si no itero esto los prefijos no funcionan
                    pass
                for prefix in blobs.prefixes:
                    prefix=prefix.replace(direccionStorage,"")#quitamo el prefijo de la direccion
                    listNombres.append(prefix)
            return listNombres

        except:
            print("Error al obtener la lista de nombre de los documento del storage...")
            return None

    def descargarDocumento(self,nameFull_documentDescargar,nameFull_destino):
        try:
            blob = self.bucket.blob(nameFull_documentDescargar)
            blob.download_to_filename(nameFull_destino)
            return True
        except:
            print("Error a la hora de descargar documentos del storage")
            return None

    def borrarDocumento(self,nameFull_documentDelete):
        try:
            blob = self.bucket.blob(nameFull_documentDelete)
            blob.delete()
            return True
        except:
            print("Error a la hora de eliminar el documento del storage")
            return None


'''
# INICIALIZACION DE FIREBASE-ADMIN...
direccionJson = RecursosMenuDelphiApp.DIRE_JSON
#creds = credentials.Certificate(direccionJson)
#baseDatos = 'https://delphiadata.firebaseio.com/'
direccionJson = RecursosMenuDelphiApp.DIRE_JSON
nombreStorage='delphiadata.appspot.com'

#firebase_admin.initialize_app(creds, {
#   'databaseURL': baseDatos,
#    'storageBucket': nombreStorage
#})

storage_client = storage.Client.from_service_account_json(direccionJson)
bucket=storage_client.get_bucket(nombreStorage)


'''