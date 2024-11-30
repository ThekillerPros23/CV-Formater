from firebase_admin import firestore
from firebase_admin import credentials
import firebase_admin
import json  # Importar el módulo para manejar JSON

class FirebaseDataApplication:
    def __init__(self):
        # Inicializa Firebase con las credenciales proporcionadas
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        self.app = firebase_admin.initialize_app(self.cred, name='applications')
        self.db = firestore.client(self.app)
    
    def get_document_by_uid(self, uid):
        # Filtra el documento por UID directamente en la consulta
        try:
            users_ref = self.db.collection('applications')
            docs = list(users_ref.stream())

            if not docs:
                return json.dumps({"error": "No document found with the given UID"}, indent=2)
            
            # Retorna el documento encontrado como JSON
            document = {"id": docs[0].id, **docs[0].to_dict()}
            return json.dumps(document, indent=2)

        except Exception as e:
            # Manejo de errores y devuelve un mensaje en formato JSON
            return json.dumps({"error": str(e)}, indent=2)

# Bloque para ejecutar directamente y mostrar el JSON al ejecutar el archivo
if __name__ == "__main__":
    firebase_app = FirebaseDataApplication()
    uid = "UID_DEL_USUARIO"  # Cambia esto por el UID que quieras buscar
    result_json = firebase_app.get_document_by_uid(uid)
    print(result_json)  # Imprime el JSON directamente
