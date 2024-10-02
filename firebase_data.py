import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


# Usar una cuenta de servicio.
class FirebaseData():
    def __init__(self):
        # Inicializa la app de Firebase con las credenciales
        self.cred = credentials.Certificate('dev-portal-logistic-firebase-adminsdk-mtvp2-bbadfb4ad5.json')
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        users_ref = self.db.collection('applications')
        self.docs = users_ref.stream()
        
    def marine_name(self):   
        name = []
        for doc in self.docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            #nombre de los aplicantes
            for datos in doc_data['versions']:
                  name.append(datos['applicationProfile']['profile']['firstName'])
        new_name = name[0].split()
        print(new_name)

    def marine_name(self):   
        name = []
        for doc in self.docs:
            doc_data = doc.to_dict()  # Convertir el documento a un diccionario
            #nombre de los aplicantes
            for datos in doc_data['versions']:
                  name.append(datos['applicationProfile']['profile']['firstName'])
        new_name = name[0].split()
        print(new_name)
data = FirebaseData
data.marine_name()
data.marine_name()