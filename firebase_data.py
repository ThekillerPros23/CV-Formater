import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

# Usar una cuenta de servicio.
class FirebaseData():
    def __init__(self):
        # Inicializa la app de Firebase con las credenciales
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()

    def export_collection_to_json(self, collection_name):
        users_ref = self.db.collection(collection_name)
        docs = users_ref.stream()
        
        # Crear una lista para almacenar los datos
        data_list = []
        
        # Recuperar datos de cada documento
        for doc in docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            doc_data['id'] = doc.id  # Añadir el ID del documento al diccionario
            data_list.append(doc_data)  # Agregar los datos a la lista

        # Guardar la lista en un archivo JSON
        with open(f'{collection_name}.json', 'w') as json_file:
            json.dump(data_list, json_file, indent=4)  # Guardar con formato legible

        print(f'Documentos exportados a {collection_name}.json')

# Crear una instancia y llamar a la función de exportación
data = FirebaseData()
data.export_collection_to_json('applications')